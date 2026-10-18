"""Databricks notebook equivalent for DP700.

This script mirrors the logic in Dp700/DP700.ipynb and is intended to run in a
Databricks notebook environment where `dbutils` is available.
"""

try:
    # This will exist in Databricks notebooks.
    dbutils  # noqa: F821
except NameError:
    dbutils = None


def show_dbutils_overview():
    """Display dbutils help sections used in the notebook."""
    if dbutils is None:
        print("This script is designed to run in a Databricks notebook environment.")
        print("`dbutils` is not available in a standard local Python session.")
        return

    # Databricks Utilities (dbutils) - Overview
    print("# Databricks Utilities (dbutils) - Overview")
    print("# dbutils is a utility module available in Databricks notebooks that provides")
    print("# helper functions for working with object storage, chaining notebooks,")
    print("# managing secrets, and configuring widgets.")
    print()
    print("# List all available dbutils modules")
    dbutils.help()

    print("\n=== File System Utilities (dbutils.fs) ===")
    dbutils.fs.help()

    print("\n" + "=" * 80 + "\n")

    print("=== Widget Utilities (dbutils.widgets) ===")
    dbutils.widgets.help()


def create_widget_examples():
    """Create example widgets used in the notebook."""
    if dbutils is None:
        return

    # Text widget
    try:
        dbutils.widgets.text('FILE', "")
        file_value = dbutils.widgets.get('FILE')
        print(f"FILE widget value: {file_value}")
    except Exception as exc:
        print(f"Unable to create/get FILE widget: {exc}")

    # Multi-select widget
    try:
        dbutils.widgets.multiselect('MULTI_SELECT', 'option1', ['option1', 'option2', 'option3', 'option4'], 'Select one or more options')
        selected_values = dbutils.widgets.get('MULTI_SELECT')
        print(f"Selected values: {selected_values}")
        selected_list = [v.strip() for v in selected_values.split(',')]
        print(f"Selected as list: {selected_list}")
    except Exception as exc:
        print(f"Unable to create/get MULTI_SELECT widget: {exc}")

    # Dropdown widget
    try:
        dbutils.widgets.dropdown('Dropdown', 'OP1', ['OP1', 'OP2', 'OP3'], 'Select one or more options')
        select_value = dbutils.widgets.get('Dropdown')
        print(f"Selected value: {select_value}")
        dropdown_list = [v.strip() for v in select_value.split(',')]
        print(f"Selected list: {dropdown_list}")
    except Exception as exc:
        print(f"Unable to create/get Dropdown widget: {exc}")

    # Multi-select widget with a different name
    try:
        dbutils.widgets.multiselect('MULTI', 'OP1', ['OP1', 'OP2', 'OP3'], 'Select one or more options')
        multi_value = dbutils.widgets.get('MULTI')
        print(f"Selected value: {multi_value}")
        multi_list = [v.strip() for v in multi_value.split(',')]
        print(f"Selected list: {multi_list}")
    except Exception as exc:
        print(f"Unable to create/get MULTI widget: {exc}")


if __name__ == "__main__":
    show_dbutils_overview()
    create_widget_examples()
