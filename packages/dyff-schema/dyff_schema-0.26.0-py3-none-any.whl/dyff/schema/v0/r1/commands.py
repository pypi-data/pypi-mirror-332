# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0
"""The command schemas describe the API for the command model.

These are used internally by the platform and users typically won't encounter them.
"""

from __future__ import annotations

from typing import Any, Literal, Optional, Union

import pydantic

from .base import DyffSchemaBaseModel, Null
from .platform import (
    DyffEntityType,
    EntityKindLiteral,
    FamilyMember,
    FamilyMembers,
    LabelKeyType,
    LabelValueType,
    SchemaVersion,
    Status,
    TagNameType,
    summary_maxlen,
    title_maxlen,
)

# ----------------------------------------------------------------------------


# mypy gets confused because 'dict' is the name of a method in DyffBaseModel
_ModelAsDict = dict[str, Any]


class EntityIdentifier(DyffSchemaBaseModel):
    """Identifies a single entity."""

    @staticmethod
    def of(entity: DyffEntityType) -> EntityIdentifier:
        """Create an identifier that identifies the given entity."""
        return EntityIdentifier(kind=entity.kind, id=entity.id)

    kind: EntityKindLiteral = pydantic.Field(description="The .kind of the entity.")
    id: str = pydantic.Field(description="The .id of the entity.")


class FamilyIdentifier(EntityIdentifier):
    """Identifies a single Family entity."""

    kind: Literal["Family"] = "Family"


class Command(SchemaVersion):
    """Base class for Command messages.

    Commands define the API of the "command model" in our CQRS architecture.
    """

    command: Literal[
        "CreateEntity",
        "EditEntityDocumentation",
        "EditEntityLabels",
        "EditFamilyMembers",
        "ForgetEntity",
        "UpdateEntityStatus",
    ]

    # TODO: (DYFF-223) I think that exclude_unset=True should be the default
    # for all schema objects, but I'm unsure of the consequences of making
    # this change and we'll defer it until v1.
    def dict(
        self, *, by_alias: bool = True, exclude_unset=True, **kwargs
    ) -> _ModelAsDict:
        return super().dict(by_alias=by_alias, exclude_unset=exclude_unset, **kwargs)

    def json(self, *, by_alias: bool = True, exclude_unset=True, **kwargs) -> str:
        return super().json(by_alias=by_alias, exclude_unset=exclude_unset, **kwargs)


# ----------------------------------------------------------------------------


class CreateEntity(Command):
    """Create a new entity."""

    command: Literal["CreateEntity"] = "CreateEntity"

    data: DyffEntityType = pydantic.Field(
        description="The full spec of the entity to create."
    )


# ----------------------------------------------------------------------------


class EditEntityDocumentationPatch(DyffSchemaBaseModel):
    """Same properties as DocumentationBase, but generates a JSON Schema that allows
    fields to be set to JSON 'null'.

    This is needed to get JSON Merge Patch semantics, where explicit 'null' means
    "delete that field".
    """

    title: Optional[Union[pydantic.constr(max_length=title_maxlen()), Null]] = (  # type: ignore
        pydantic.Field(
            default=None,
            description='A short plain string suitable as a title or "headline".',
        )
    )

    summary: Optional[Union[pydantic.constr(max_length=summary_maxlen()), Null]] = (  # type: ignore
        pydantic.Field(
            default=None,
            description="A brief summary, suitable for display in"
            " small UI elements. Interpreted as Markdown. Excessively long"
            " summaries may be truncated in the UI, especially on small displays.",
        )
    )

    fullPage: Optional[Union[str, Null]] = pydantic.Field(
        default=None,
        description="Long-form documentation. Interpreted as"
        " Markdown. There are no length constraints, but be reasonable.",
    )


class EditEntityDocumentationAttributes(DyffSchemaBaseModel):
    documentation: EditEntityDocumentationPatch = pydantic.Field(
        description="Edits to make to the documentation."
    )


class EditEntityDocumentationData(EntityIdentifier):
    """Payload data for the EditEntityDocumentation command."""

    attributes: EditEntityDocumentationAttributes = pydantic.Field(
        description="The command attributes"
    )


class EditEntityDocumentation(Command):
    """Edit the documentation associated with an entity.

    Setting a documentation field to null/None deletes the corresponding value. To
    preserve the existing value, leave the field *unset*.
    """

    command: Literal["EditEntityDocumentation"] = "EditEntityDocumentation"

    data: EditEntityDocumentationData = pydantic.Field(description="The edit data.")


# ----------------------------------------------------------------------------


class EditEntityLabelsAttributes(DyffSchemaBaseModel):
    labels: dict[LabelKeyType, Optional[Union[LabelValueType, Null]]] = pydantic.Field(
        default_factory=dict,
        description="A set of key-value labels for the resource. Used to"
        " specify identifying attributes of resources that are meaningful to"
        " users but do not imply semantics in the dyff system.\n\n"
        "The keys are DNS labels with an optional DNS domain prefix."
        " For example: 'my-key', 'your.com/key_0'. Keys prefixed with"
        " 'dyff.io/', 'subdomain.dyff.io/', etc. are reserved.\n\n"
        "The label values are alphanumeric characters separated by"
        " '.', '-', or '_'.\n\n"
        "We follow the kubernetes label conventions closely."
        " See: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels",
    )


class EditEntityLabelsData(EntityIdentifier):
    """Payload data for the EditEntityLabels command."""

    attributes: EditEntityLabelsAttributes = pydantic.Field(
        description="The command attributes"
    )


class EditEntityLabels(Command):
    """Edit the labels associated with an entity.

    Setting a label field to null/None deletes the corresponding value. To preserve the
    existing value, leave the field *unset*.
    """

    command: Literal["EditEntityLabels"] = "EditEntityLabels"

    data: EditEntityLabelsData = pydantic.Field(description="The edit data.")


# ----------------------------------------------------------------------------


class EditFamilyMembersAttributes(DyffSchemaBaseModel):
    """Payload data for the EditFamilyMembers command."""

    members: dict[TagNameType, Optional[Union[FamilyMember, Null]]] = pydantic.Field(
        description="Mapping of names to IDs of member resources.",
    )


class EditFamilyMembersData(FamilyMembers, FamilyIdentifier):
    """Payload data for the EditFamilyMembers command."""

    attributes: EditFamilyMembersAttributes = pydantic.Field(
        description="The command attributes"
    )


class EditFamilyMembers(Command):
    """Edit the labels associated with an entity.

    Setting a tag value to null/None deletes the corresponding value. To preserve the
    existing value, leave the field *unset*.
    """

    command: Literal["EditFamilyMembers"] = "EditFamilyMembers"

    data: EditFamilyMembersData = pydantic.Field(description="The edit data.")


# ----------------------------------------------------------------------------


class ForgetEntity(Command):
    """Forget (permanently delete) an entity."""

    command: Literal["ForgetEntity"] = "ForgetEntity"

    data: EntityIdentifier = pydantic.Field(description="The entity to forget.")


# ----------------------------------------------------------------------------


class UpdateEntityStatusAttributes(DyffSchemaBaseModel):
    status: str = pydantic.Field(
        description=Status.__fields__["status"].field_info.description
    )

    reason: Union[str, Null] = pydantic.Field(
        description=Status.__fields__["reason"].field_info.description
    )


class UpdateEntityStatusData(EntityIdentifier):
    """Payload data for the UpdateEntityStatus command."""

    attributes: UpdateEntityStatusAttributes = pydantic.Field(
        description="The command attributes"
    )


class UpdateEntityStatus(Command):
    """Update the status fields of an entity."""

    command: Literal["UpdateEntityStatus"] = "UpdateEntityStatus"

    data: UpdateEntityStatusData = pydantic.Field(description="The status update data.")


# ----------------------------------------------------------------------------


DyffCommandType = Union[
    CreateEntity,
    EditEntityDocumentation,
    EditEntityLabels,
    EditFamilyMembers,
    ForgetEntity,
    UpdateEntityStatus,
]


__all__ = [
    "Command",
    "CreateEntity",
    "DyffCommandType",
    "EditEntityDocumentation",
    "EditEntityDocumentationAttributes",
    "EditEntityDocumentationData",
    "EditEntityDocumentationPatch",
    "EditEntityLabels",
    "EditEntityLabelsAttributes",
    "EditEntityLabelsData",
    "EditFamilyMembers",
    "EditFamilyMembersAttributes",
    "EditFamilyMembersData",
    "EntityIdentifier",
    "FamilyIdentifier",
    "ForgetEntity",
    "UpdateEntityStatus",
    "UpdateEntityStatusAttributes",
    "UpdateEntityStatusData",
]
