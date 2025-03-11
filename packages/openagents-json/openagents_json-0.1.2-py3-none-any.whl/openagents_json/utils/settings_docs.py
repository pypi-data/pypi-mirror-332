"""
Utility for generating settings documentation.

This module provides tools for generating documentation for the settings system
based on the actual settings classes and their fields.
"""

import inspect
import json
from typing import Any, Dict, List, Optional, Union

from pydantic import Field
from pydantic_settings import BaseSettings

from openagents_json.settings import (
    AgentSettings,
    AppSettings,
    DatabaseSettings,
    JobSettings,
    RegistrySettings,
    Settings,
    StorageSettings,
    WorkflowSettings,
)


def get_setting_docs() -> Dict[str, Any]:
    """
    Generate comprehensive documentation for all settings.

    Returns:
        A dictionary with documentation for all settings
    """
    settings_classes = {
        "app": AppSettings,
        "registry": RegistrySettings,
        "workflow": WorkflowSettings,
        "agent": AgentSettings,
        "job": JobSettings,
        "storage": StorageSettings,
        "database": DatabaseSettings,
    }

    docs = {}

    for section_name, settings_class in settings_classes.items():
        # Skip database as it's nested under storage
        if section_name == "database":
            continue

        section_docs = _get_section_docs(settings_class)

        # Special handling for storage.database
        if section_name == "storage":
            # Add database fields as nested
            database_docs = _get_section_docs(DatabaseSettings)
            section_docs["fields"]["database"] = {
                "description": "Database connection settings",
                "default": "DatabaseSettings()",
                "type": "DatabaseSettings",
                "fields": database_docs["fields"],
            }

        docs[section_name] = section_docs

    # Add main Settings class for reference
    docs["_meta"] = {
        "description": inspect.getdoc(Settings),
        "env_prefix": "OPENAGENTS_",
        "env_nested_delimiter": "__",
    }

    return docs


def _get_section_docs(settings_class: BaseSettings) -> Dict[str, Any]:
    """
    Generate documentation for a settings section.

    Args:
        settings_class: The settings class to document

    Returns:
        A dictionary with documentation for the settings section
    """
    # Get class description from docstring
    description = inspect.getdoc(settings_class)

    # Get class fields
    fields = {}
    for name, field in settings_class.model_fields.items():
        # Skip private fields
        if name.startswith("_"):
            continue

        # Get field info
        field_info = {
            "description": field.description or "",
            "default": str(field.default) if field.default is not None else None,
            "type": _get_type_name(field.annotation),
        }

        # Add validation info if available
        if hasattr(field, "ge") and field.ge is not None:
            field_info["min"] = field.ge
        if hasattr(field, "le") and field.le is not None:
            field_info["max"] = field.le
        if hasattr(field, "pattern") and field.pattern is not None:
            field_info["pattern"] = field.pattern

        fields[name] = field_info

    return {
        "description": description,
        "fields": fields,
    }


def _get_type_name(annotation: Any) -> str:
    """
    Get a human-readable name for a type annotation.

    Args:
        annotation: The type annotation

    Returns:
        A string representation of the type
    """
    if annotation is None:
        return "Any"

    if hasattr(annotation, "__origin__"):
        # Handle generic types like List[str], Optional[int], etc.
        origin = annotation.__origin__
        args = annotation.__args__

        if origin is Union:
            # Handle Optional[T] (Union[T, None])
            if len(args) == 2 and args[1] is type(None):
                return f"Optional[{_get_type_name(args[0])}]"
            else:
                return f"Union[{', '.join(_get_type_name(arg) for arg in args)}]"

        # Handle other generic types
        return f"{origin.__name__}[{', '.join(_get_type_name(arg) for arg in args)}]"

    # Handle Literal types
    if getattr(annotation, "__name__", "") == "Literal":
        values = getattr(annotation, "__args__", [])
        return f"Literal[{', '.join(repr(v) for v in values)}]"

    # Handle classes and basic types
    if hasattr(annotation, "__name__"):
        return annotation.__name__

    # Fallback
    return str(annotation)


def generate_markdown_docs() -> str:
    """
    Generate Markdown documentation for all settings.

    Returns:
        Markdown string with documentation
    """
    docs = get_setting_docs()
    meta = docs.pop("_meta")

    md_lines = [
        "# OpenAgents JSON Settings Reference",
        "",
        meta["description"],
        "",
        "## Environment Variables",
        "",
        f"All settings can be configured using environment variables with the prefix `{meta['env_prefix']}` ",
        f"and nested delimiter `{meta['env_nested_delimiter']}`. For example:",
        "",
        "```",
        "OPENAGENTS_APP__DEBUG=true",
        "OPENAGENTS_AGENT__OPENAI_API_KEY=sk-your-api-key",
        "OPENAGENTS_STORAGE__DATABASE__HOST=localhost",
        "```",
        "",
    ]

    for section_name, section_docs in docs.items():
        md_lines.extend(
            [
                f"## {section_name.title()} Settings",
                "",
                section_docs["description"],
                "",
                "| Name | Type | Default | Description |",
                "| ---- | ---- | ------- | ----------- |",
            ]
        )

        for field_name, field_info in section_docs["fields"].items():
            # Handle nested fields (like database)
            if "fields" in field_info:
                # Add section row as a header
                md_lines.append(
                    f"| **{field_name}** | {field_info['type']} | - | {field_info['description']} |"
                )

                # Add nested fields with dot notation
                for sub_name, sub_info in field_info["fields"].items():
                    default_val = (
                        sub_info["default"]
                        if sub_info["default"] not in (None, "None")
                        else "-"
                    )
                    md_lines.append(
                        f"| {field_name}.{sub_name} | {sub_info['type']} | {default_val} | {sub_info['description']} |"
                    )
            else:
                default_val = (
                    field_info["default"]
                    if field_info["default"] not in (None, "None")
                    else "-"
                )
                md_lines.append(
                    f"| {field_name} | {field_info['type']} | {default_val} | {field_info['description']} |"
                )

        md_lines.append("")

    return "\n".join(md_lines)


def generate_json_docs() -> str:
    """
    Generate JSON documentation for all settings.

    Returns:
        JSON string with documentation
    """
    docs = get_setting_docs()
    return json.dumps(docs, indent=2)


if __name__ == "__main__":
    # When run as a script, generate and print markdown docs
    print(generate_markdown_docs())
