import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

graph_file_name = "execution_graph.py"
template_schema_file_name = "templates.json"
function_schema_file_name = "functions.json"
schema_file_name = "schema.json"

def json_string_to_dict(json_string: str) -> Dict[str, Any]:
    return json.loads(json_string)

def dict_to_json_string(dict: Dict[str, Any]) -> str:
     return json.dumps(dict)

def read_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path: str, content: str) -> str:
    with open(file_path, 'w') as f:
        return f.write(content)

def get_schemas() -> Tuple[Dict[str, Any], Optional[Dict[str, str]], Optional[Dict[str, str]]]:
    schema_file_path = Path(schema_file_name)
    schema = None

    if schema_file_path.exists():
        schema = json_string_to_dict(read_file(str(schema_file_path)))
    
    template_schema_file_path = Path(template_schema_file_name)
    template_schema = None

    if template_schema_file_path.exists():
        template_schema = json_string_to_dict(read_file(str(template_schema_file_path)))

    function_schema_file_path = Path(function_schema_file_name)
    function_schema = None

    if function_schema_file_path.exists():
        function_schema = json_string_to_dict(read_file(str(function_schema_file_path)))

    return schema, function_schema, template_schema

def prune_unused_files():
    """
    Prunes unused function and template files by checking the file system against the schemas.
    If a file exists in functions/ or templates/ but its path is not in the schema, it's deleted.
    """
    _, function_schema, template_schema = get_schemas()

    # Prune functions
    if function_schema is not None:
        functions_dir = Path("functions")
        if functions_dir.exists() and functions_dir.is_dir():
            for file_name in os.listdir(functions_dir):
                if file_name.endswith(".py"):
                    file_path = str(functions_dir / file_name)
                    if file_path not in function_schema.values():
                        full_file_path = functions_dir / file_name
                        if full_file_path.exists():
                            os.remove(full_file_path)
                            print(f"Removed function file: {full_file_path}")

    # Prune templates
    if template_schema is not None:
        templates_dir = Path("templates")
        if templates_dir.exists() and templates_dir.is_dir():
            for file_name in os.listdir(templates_dir):
                if file_name.endswith(".py"):
                    file_path = str(templates_dir / file_name)
                    if file_path not in template_schema.values():
                        full_file_path = templates_dir / file_name
                        if full_file_path.exists():
                            os.remove(full_file_path)
                            print(f"Removed template file: {full_file_path}")

def get_new_keys(old_function_schema: Optional[Dict[str, str]], new_function_schema: Optional[Dict[str, str]],
                 old_template_schema: Optional[Dict[str, str]], new_template_schema: Optional[Dict[str, str]]) -> Tuple[Optional[set], Optional[set]]:
    """
    Compares old and new function/template schemas and returns the sets of new keys.

    Args:
        old_function_schema: The old function schema dictionary.
        new_function_schema: The new function schema dictionary.
        old_template_schema: The old template schema dictionary.
        new_template_schema: The new template schema dictionary.

    Returns:
        A tuple containing sets of new function keys and new template keys.
    """
    new_function_keys = None
    new_template_keys = None

    if new_function_schema and old_function_schema:
        new_function_keys = set(new_function_schema.keys()) - set(old_function_schema.keys())
    elif new_function_schema:
        new_function_keys = set(new_function_schema.keys())

    if new_template_schema and old_template_schema:
        new_template_keys = set(new_template_schema.keys()) - set(old_template_schema.keys())
    elif new_template_schema:
        new_template_keys = set(new_template_schema.keys())

    return new_function_keys, new_template_keys

def get_function_file_content(function_schema: Dict[str, str], key: str) -> Optional[str]:
    """Retrieves the content of a function file based on its key in the function schema."""
    if key in function_schema:
        file_path = function_schema[key]
        if os.path.exists(file_path):
            return read_file(file_path)
    return None

def set_function_file_content(function_schema: Dict[str, str], key: str, content: str) -> None:
    """Sets the content of a function file based on its key in the function schema."""
    if key in function_schema:
        file_path = function_schema[key]
        write_file(file_path, content)

def get_template_file_content(template_schema: Dict[str, str], key: str) -> Optional[str]:
    """Retrieves the content of a template file based on its key in the template schema."""
    if key in template_schema:
        file_path = template_schema[key]
        if os.path.exists(file_path):
            return read_file(file_path)
    return None

def set_template_file_content(template_schema: Dict[str, str], key: str, content: str) -> None:
    """Sets the content of a template file based on its key in the template schema."""
    if key in template_schema:
        file_path = template_schema[key]
        write_file(file_path, content)

def update_code_files_with_schema(function_filepath_to_schema_map: Dict[str, Dict[str, Any]], template_filepath_to_schema_map: Dict[str, Dict[str, Any]]):
    """
    Updates sections of function and template files based on the provided filepath to schema maps.

    Args:
        function_filepath_to_schema_map: Dictionary mapping function file paths to their schemas.
        template_filepath_to_schema_map: Dictionary mapping template file paths to their schemas.
    """
    for function_file_path, step_schema in function_filepath_to_schema_map.items():
        if Path(function_file_path).exists():
            _update_function_section(function_file_path, step_schema)

    for template_file_path, step_schema in template_filepath_to_schema_map.items():
        if Path(template_file_path).exists():
            _update_template_section(template_file_path, step_schema)


def _update_function_section(function_file_path: str, schema: Dict[str, Any]):
    """Updates sections of a function file."""
    file_content = read_file(function_file_path)

    required_inputs_step = schema.get("required_inputs", [])
    required_outputs_step = schema.get("required_outputs", [])

    input_extraction_lines = ""
    if required_inputs_step:
        for input_name in required_inputs_step:
            input_extraction_lines += f"    {input_name}_input = inputs[{input_name}]\n"

    output_dict_return = "{"
    if required_outputs_step:
        output_items = []
        for output_name in required_outputs_step:
            output_items.append(f"{output_name}: ''")
        output_dict_return += ", ".join(output_items)
    output_dict_return += "}"

    input_ids_lines = "# Inputs:\n"
    if required_inputs_step:
        for input_name in required_inputs_step:
            input_ids_lines += f"{input_name} = \"{input_name}\"\n"

    output_ids_lines = "# Outputs:\n"
    if required_outputs_step:
        for output_name in required_outputs_step:
            output_ids_lines += f"{output_name} = \"{output_name}\"\n"

    sections_to_update = {
        'input_ids': {
            'start_marker': '# INPUT_IDS_START',
            'end_marker': '# INPUT_IDS_END',
            'new_content': input_ids_lines.strip()
        },
        'output_ids': {
            'start_marker': '# OUTPUT_IDS_START',
            'end_marker': '# OUTPUT_IDS_END',
            'new_content': output_ids_lines.strip()
        },
        'input_vars': {
            'start_marker': '# INPUT_VARS_START',
            'end_marker': '    # INPUT_VARS_END',
            'new_content': f"    {input_extraction_lines.strip()}"
        },
        'output_vars': {
            'start_marker': '# OUTPUT_VARS_START',
            'end_marker': '    # OUTPUT_VARS_END',
            'new_content': f"    {output_dict_return}"
        }
    }

    updated_content = file_content
    for section_name, section_data in sections_to_update.items():
        start_marker = section_data['start_marker']
        end_marker = section_data['end_marker']
        new_content = section_data['new_content']

        start_index = updated_content.find(start_marker)
        end_index = updated_content.find(end_marker)

        if start_index != -1 and end_index != -1:
            start_replace_index = start_index + len(start_marker)
            updated_content = updated_content[:start_replace_index] + "\n" + new_content + "\n" + updated_content[end_index:]

    write_file(function_file_path, updated_content)

def _update_template_section(template_file_path: str, schema: Dict[str, Any]):
    """Updates sections of a template file."""
    file_content = read_file(template_file_path)
    required_inputs_step = schema.get("required_inputs", [])

    input_vars_lines = ""
    if required_inputs_step:
        for input_name in required_inputs_step:
            input_vars_lines += f'{input_name} = "{input_name}"\n'

    sections_to_update = {
        'input_vars': {
            'start_marker': '# INPUT_VARS_START',
            'end_marker': '# INPUT_VARS_END',
            'new_content': input_vars_lines.strip()
        }
    }

    updated_content = file_content
    for section_name, section_data in sections_to_update.items():
        start_marker = section_data['start_marker']
        end_marker = section_data['end_marker']
        new_content = section_data['new_content']

        start_index = updated_content.find(start_marker)
        end_index = updated_content.find(end_marker)

        if start_index != -1 and end_index != -1:
            start_replace_index = start_index + len(start_marker)
            updated_content = updated_content[:start_replace_index] + "\n" + new_content + "\n" + updated_content[end_index:]

    write_file(template_file_path, updated_content)
