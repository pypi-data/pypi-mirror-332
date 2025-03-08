import re
from collections.abc import Mapping, Sequence
from itertools import product
from typing import Any, Literal, TypeVar, Union, cast

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)
from pydantic.alias_generators import to_camel

T = TypeVar("T")


def _expand_jinja(s: str, **fmt_keys) -> str:
    try:
        import jinja2  # type: ignore
    except ImportError as e:
        msg = (
            "jinja2 is required for jinja strings templates. "
            "Did you install with [jinja2] extra?"
        )
        raise RuntimeError(msg) from e

    return jinja2.Template(s).render(**fmt_keys)


def _expand_string(s: str, **fmt_keys: str) -> str:
    match = re.match(r"^\{\s*jinja\s*\}(.*)", s)
    if match:
        return _expand_jinja(match[1], **fmt_keys)

    try:
        return s.format(**fmt_keys)
    except KeyError as e:
        msg = f"unknown key {e} in format string: {s}"
        raise ValueError(msg) from None


def _format_json_strings(obj: T, **fmt_keys: str) -> T:
    r: Any

    if isinstance(obj, str):
        r = _expand_string(obj, **fmt_keys)
        return r

    if isinstance(obj, Sequence):
        r = [_format_json_strings(v, **fmt_keys) for v in obj]
        return r

    if isinstance(obj, Mapping):
        r = {}
        for k, v in obj.items():
            if isinstance(k, str):
                k = _expand_string(k, **fmt_keys)
            r[k] = _format_json_strings(v, **fmt_keys)
        return r

    # obj is another type, return as-is
    return obj


class _Model(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)


class ParameterValue(_Model):
    name: str
    value: str


def _expand_param_template(
    template: dict, param_value: ParameterValue
) -> dict:
    return _format_json_strings(
        template,
        value=param_value.value,
        name=param_value.name,
    )


def _base_preset_name(
    prefix: str,
    sep: str,
    param_name: str,
    param_value: ParameterValue,
) -> str:
    return sep.join((prefix, param_name, param_value.name))


ParameterValuesList = Union[dict[str, str], list[str], list[ParameterValue]]


def _validate_parameter_list(
    parameters: ParameterValuesList,
) -> list[ParameterValue]:
    """
    Convert parameter to a list of ParameterValues, checking that the
    parameter names are unique.

    Each parameter has a 'name' and a 'value'. The name is used for generating
    preset names and prefixes, and the value is used for generating the actual
    configuration value. It may be useful to have a separate name and value if,
    for example, the parameter value is long or contains special characters.

    Parameters may be specified in JSON as either:

    - An object mapping parameter name to value.
    - An array of strings, where each string doubles as the parameter name and
      value.
    - An array of ParameterValue objects.
    """

    if isinstance(parameters, dict):
        return [ParameterValue(name=k, value=v) for k, v in parameters.items()]

    unique_names = set()
    converted: list[ParameterValue] = []
    for val in parameters:
        if isinstance(val, str):
            val = ParameterValue(name=val, value=val)
        if val.name in unique_names:
            raise ValueError(f"duplicate parameter name '{val.name}'")
        unique_names.add(val.name)
        converted.append(val)
    return converted


class PresetGroup(_Model):
    type: str = Field(
        ...,
        min_length=1,
        description="Type of configuration preset, "
        "e.g. configure, build, test.",
    )
    inherits: list[str] = Field(
        [],
        description="Name of pre-existing configuration presets to inherit "
        "in all generated presets.",
    )
    parameters: dict[str, ParameterValuesList] = Field(
        ...,
        min_length=1,
        description="Parameters to generate presets from.",
    )
    templates: dict[str, Union[dict, str]] = Field(
        {},
        description="Template for generating configuration options.",
    )

    _sep = "-"

    @field_validator("parameters", mode="after")
    @classmethod
    def _validate_parameters(
        cls,
        parameters: dict[str, ParameterValuesList],
    ) -> dict[str, list[ParameterValue]]:
        """
        Narrow the type of the `parameters` member to
        `dict[str, list[ParameterValue]]`. We keep the `ParameterValuesList`
        in the type annotation so that the JSON schema type is correctly
        specified.
        """
        return {k: _validate_parameter_list(v) for k, v in parameters.items()}

    def _parameters_dict(self) -> dict[str, list[ParameterValue]]:
        """
        Returns `self.parameters`, casted to `dict[str, list[ParameterValue]]`.
        The `parameters` attribute will have already been narrowed to this type
        by `_validate_parameters`, so safe to cast.
        """
        return cast(dict[str, list[ParameterValue]], self.parameters)

    @model_validator(mode="after")
    def _validate_template_parameters(self) -> "PresetGroup":
        missing = []
        for param_name in self.templates:
            if param_name not in self.parameters:
                missing.append(param_name)

        if missing:
            s = "" if len(missing) == 1 else "s"
            missing_str = ", ".join(missing)
            msg = f"Missing parameter{s} for template keys: {missing_str}"
            raise ValueError(msg)

        return self

    def _get_template(self, param_name: str) -> dict[str, Any]:
        template = self.templates.get(param_name)
        param_name = param_name.replace("{", "{{").replace("}", "}}")
        if template is None:
            return {param_name: "{value}"}

        if isinstance(template, str):
            return {param_name: template}

        return template

    def _generate_presets_for_single_parameter(self, prefix: str) -> list:
        param_name, param_values = self._parameters_dict().popitem()
        template = self._get_template(param_name)
        return [
            {
                "name": self._sep.join((prefix, param_value.name)),
                **({"inherits": self.inherits} if self.inherits else {}),
                **_expand_param_template(template, param_value),
            }
            for param_value in param_values
        ]

    def _generate_base_presets(self, prefix: str) -> list:
        """
        Generate base presets for all individual parameters.
        """
        presets: list[dict] = []
        for param_name, param_values in self._parameters_dict().items():
            template = self._get_template(param_name)
            presets.extend(
                {
                    "name": _base_preset_name(
                        prefix,
                        self._sep,
                        param_name,
                        param_value,
                    ),
                    "hidden": True,
                    **_expand_param_template(template, param_value),
                }
                for param_value in param_values
            )

        return presets

    def generate_presets(self, prefix: str) -> list:
        if len(self.parameters) == 1:
            return self._generate_presets_for_single_parameter(prefix)

        presets = self._generate_base_presets(prefix)
        parameters = self._parameters_dict()
        for param_values in product(*parameters.values()):
            bases = (
                _base_preset_name(prefix, self._sep, param_name, param_value)
                for param_name, param_value in zip(
                    parameters.keys(), param_values
                )
            )
            name = self._sep.join([prefix, *(v.name for v in param_values)])
            preset = {
                "name": name,
                "inherits": [*self.inherits, *bases],
            }
            presets.append(preset)

        return presets


class Exploder(_Model):
    version: Literal[0]
    preset_groups: dict[str, PresetGroup] = Field(
        ...,
        description="Preset groups. Presets are generated from the Cartesian "
        "product of the parameters in each group.",
    )


def explode_presets(
    template_json: Any,
    *,
    vendor_name: str = "exploder",
    include_vendor: bool = False,
    copy: bool = True,
) -> dict:
    if not isinstance(template_json, dict):
        raise ValueError("template must be a dictionary")

    if copy:
        template_json = template_json.copy()

    vendor_json = template_json.get("vendor")
    if not vendor_json:
        raise ValueError("template missing 'vendor' property")
    exploder_json = vendor_json.get(vendor_name)
    if not exploder_json:
        raise ValueError(f"vendor object missing '{vendor_name}' property")

    try:
        exploder = Exploder.model_validate(exploder_json)
    except ValueError as e:
        raise ValueError(f"invalid '{vendor_name}' object: {e}") from e

    for name, group in exploder.preset_groups.items():
        presets = group.generate_presets(name)
        template_json.setdefault(f"{group.type}Presets", []).extend(presets)

    if not include_vendor:
        del template_json["vendor"][vendor_name]
        if not template_json["vendor"]:
            del template_json["vendor"]

    return template_json
