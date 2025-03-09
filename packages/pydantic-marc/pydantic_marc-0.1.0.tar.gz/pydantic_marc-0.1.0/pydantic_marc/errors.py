"""Exceptions raised during the validation of a `MarcRecord` model.

Exceptions in this module are based off of errors identified when using the MarcEdit
Validate MARC Records tool. Each exception inherits from `MarcCustomError` which
inherits from `PydanticCustomError`. The `MarcCustomError` exception and includes
an `error_details` property to will create an `InitErrorDetails` object from the
exception. An `InitErrorDetails` object is required in order to wrap an exception
within a `pydantic.ValidationError` object.
"""

from __future__ import annotations

from typing import Any, Dict

from pydantic_core import InitErrorDetails, PydanticCustomError


class MarcCustomError(PydanticCustomError):
    """Base Exception for MARC validation errors."""

    @property
    def error_details(self) -> InitErrorDetails:
        """Return the exception as an `InitErrorDetails` object."""
        context = {} if not self.context else self.context
        loc = context.get("loc", context.get("tag", context.get("input")))
        input = context.get("input", {})
        if isinstance(loc, str):
            return InitErrorDetails(type=self, input=input, loc=(loc,))
        return InitErrorDetails(type=self, input=input, loc=loc)


class InvalidIndicator(MarcCustomError):
    """Exception raised if an indicator does not match the field's rules."""

    def __new__(cls, context: Dict[str, Any]) -> InvalidIndicator:
        """
        Create a new `InvalidIndicator` object.

        Args:
            context: A dictionary containing:
                loc:
                    A tuple with the tag and indicator number. example: (100, ind1).
                input:
                    The value passed to the indicator.
                valid:
                    A list of valid values for the indicator.

        """
        context["tag"], context["ind"] = context["loc"]
        instance = super().__new__(
            cls,
            "invalid_indicator",
            "{tag} {ind}: Invalid data ({input}). Indicator should be {valid}.",
            context,
        )
        return instance


class InvalidSubfield(MarcCustomError):
    """Exception raised if a subfield is not defined for the field is it a part of."""

    def __new__(cls, context: Dict[str, Any]) -> InvalidSubfield:
        """
        Create a new `InvalidIndicator` object.

        Args:
            context: A dictionary containing:
                loc:
                    A tuple containing the tag and subfield code. example: (100, a).
                input:
                    A list of subfields with the invalid subfield code.
        """
        context["tag"], context["code"] = context["loc"]
        instance = super().__new__(
            cls,
            "subfield_not_allowed",
            "{tag} ${code}: Subfield cannot be defined in this field.",
            context,
        )
        return instance


class ControlFieldLength(MarcCustomError):
    """Exception raised if the a control field does not match its expected length."""

    def __new__(cls, context: Dict[str, Any]) -> ControlFieldLength:
        """
        Create a new `InvalidIndicator` object.

        Args:
            context: A dictionary containing:
                tag: The field's tag.
                input: Value passed to the control field's data attribute.
                valid: The valid length for the field.
        """
        context["length"] = len(context["input"])
        instance = super().__new__(
            cls,
            "control_field_length_invalid",
            "{tag}: Length appears to be invalid. Reported length is: {length}. Expected length is: {valid}",  # noqa: E501
            context,
        )
        return instance


class MultipleMainEntryValues(MarcCustomError):
    """Exception raised if a record contains multiple main entry (1xx) values."""

    def __new__(cls, context: Dict[str, Any]) -> MultipleMainEntryValues:
        """
        Create a new `InvalidIndicator` object.

        Args:
            context: A dictionary containing:
                input: The field's tag.
        """
        instance = super().__new__(
            cls,
            "multiple_1xx_fields",
            "1XX: Only one 1XX tag is allowed. Record contains: {input}",
            context,
        )
        return instance


class MissingRequiredField(MarcCustomError):
    """Exception raised if a record is missing a required field (245)."""

    def __new__(cls, context: Dict[str, Any]) -> MissingRequiredField:
        """
        Create a new `InvalidIndicator` object.

        Args:
            context: A dictionary containing:
                input: The field's tag.
        """
        instance = super().__new__(
            cls,
            "missing_required_field",
            "One {input} field must be present in a MARC21 record.",
            context,
        )
        return instance


class NonRepeatableField(MarcCustomError):
    """Exception raised if a non-repeatable field is repeated in a record."""

    def __new__(cls, context: Dict[str, Any]) -> NonRepeatableField:
        """
        Create a new `InvalidIndicator` object.

        Args:
            context: A dictionary containing:
                input: The field's tag.
        """
        instance = super().__new__(
            cls,
            "non_repeatable_field",
            "{input}: Has been marked as a non-repeating field.",
            context,
        )
        return instance


class NonRepeatableSubfield(MarcCustomError):
    """Exception raised if a non-repeatable subfield is repeated in a field."""

    def __new__(cls, context: Dict[str, Any]) -> NonRepeatableSubfield:
        """
        Create a new `InvalidIndicator` object.

        Args:
            context: A dictionary containing:
                loc:
                    A tuple containing the tag and subfield code. example: (100, a).
                input:
                    A list of subfields with the invalid subfield code.
        """
        context["tag"], context["code"] = context["loc"]
        instance = super().__new__(
            cls,
            "non_repeatable_subfield",
            "{tag} ${code}: Subfield cannot repeat.",
            context,
        )
        return instance
