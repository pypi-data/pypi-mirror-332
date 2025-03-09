from typing import Any, Dict, Set, Tuple
from .schema_io import write_file, dict_to_json_string, function_schema_file_name, template_schema_file_name, graph_file_name
import os
from .schema_io import get_schemas, update_code_files_with_schema

def generate_graph_code() -> Tuple[str, Dict[str, str], Dict[str, str]]:
    schema, function_schema, template_schema = get_schemas()

    graph_code_data = _generate_graph_code_recursive(schema)
    (
        function_definitions_code,
        step_definitions_code,
        main_graph_code,
        import_lines,
        template_definitions_code,
        function_filepath_to_schema_map,
        template_filepath_to_schema_map,
        function_name_map,
        template_name_map
    ) = graph_code_data

    consolidated_imports_code = _consolidate_imports_to_string(import_lines)

    # Handle function schemas and files
    updated_function_name_dict: Dict[str, str] = function_schema if function_schema else {}
    current_function_names = set(updated_function_name_dict.keys())
    generated_function_names = set(function_definitions_code.keys())
    functions_to_remove = current_function_names - generated_function_names

    for function_file_name in generated_function_names:
        file_path = f"functions/{function_file_name}.py"
        updated_function_name_dict[function_file_name] = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file_exists = os.path.exists(file_path)
        if not file_exists:
            write_file(file_path, function_definitions_code[function_file_name])

    # Handle template schemas and files
    updated_template_name_dict: Dict[str, str] = template_schema if template_schema else {}
    current_template_names = set(updated_template_name_dict.keys())
    generated_template_names = set(template_definitions_code.keys())
    templates_to_remove = current_template_names - generated_template_names

    for template_file_name in generated_template_names:
        file_path = f"templates/{template_file_name}.py"
        updated_template_name_dict[template_file_name] = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        file_exists = os.path.exists(file_path)
        if not file_exists:
            write_file(file_path, template_definitions_code[template_file_name])

    for function_file_name in functions_to_remove:
        if function_file_name in updated_function_name_dict:
            del updated_function_name_dict[function_file_name]

    functions = dict_to_json_string(updated_function_name_dict)
    write_file(function_schema_file_name, functions)

    for template_file_name in templates_to_remove:
        if template_file_name in updated_template_name_dict:
            del updated_template_name_dict[template_file_name]

    templates = dict_to_json_string(updated_template_name_dict)
    write_file(template_schema_file_name, templates)

    update_code_files_with_schema(function_filepath_to_schema_map, template_filepath_to_schema_map)

    # Generate final code with imports and graph definition
    final_code_parts = [consolidated_imports_code]
    for function_file_name in generated_function_names:
        import_path = updated_function_name_dict.get(function_file_name)
        module_name = os.path.splitext(os.path.basename(import_path))[0]
        actual_function_name = function_name_map[function_file_name] # Use the actual function name from the map
        final_code_parts.append(f"from .functions.{module_name} import {actual_function_name}")
    for template_file_name in generated_template_names:
        import_path = updated_template_name_dict.get(template_file_name)
        module_name = os.path.splitext(os.path.basename(import_path))[0]
        actual_template_var_name = template_name_map[template_file_name] # Use the actual template name from the map
        final_code_parts.append(f"from .templates.{module_name} import {actual_template_var_name}")

    final_code_parts.append(step_definitions_code)
    final_code_parts.append(main_graph_code)

    final_code = "\n\n".join(final_code_parts)
    write_file(graph_file_name, final_code)

    return final_code, updated_function_name_dict, updated_template_name_dict

def _generate_graph_code_recursive(schema: Dict[str, Any], collected_import_lines: Set[str] = None) -> Tuple[Dict[str, str], str, str, Set[str], Dict[str, str], Dict[str, Dict[str, Any]], Dict[str, Dict[str, Any]], Dict[str, str], Dict[str, str]]:
    """
    Recursively generates code components for a StepGraph and its subgraphs, referencing LLM client definitions.
    Returns code components, consolidating function and template data.

    Args:
        schema (Dict[str, Any]): Schema for the current graph level.
        collected_import_lines (Set[str], optional): Set to accumulate import lines.

    Returns:
        Tuple[Dict[str, str], str, str, Set[str], Dict[str, str], Dict[str, Dict[str, Any]], Dict[str, Dict[str, Any]], Dict[str, str], Dict[str, str]]:
        Function definitions, step definitions, main graph code, collected import lines, template definitions,
        function filepath to schema map, template filepath to schema map, function name map, template name map
    """
    if collected_import_lines is None:
        collected_import_lines = set()

    function_definitions_code: Dict[str, str] = {}
    template_definitions_code: Dict[str, str] = {}
    function_name_map: Dict[str, str] = {}
    template_name_map: Dict[str, str] = {}
    function_filepath_to_schema_map: Dict[str, Dict[str, Any]] = {}
    template_filepath_to_schema_map: Dict[str, Dict[str, Any]] = {}


    graph_name = schema.get("graph_name")
    required_inputs = schema.get("required_inputs")
    required_outputs = schema.get("required_outputs")
    config = schema.get("configuration")
    steps_schema = config.get("steps")
    dependencies_schema = config.get("dependencies")
    llm_clients_schema = schema.get("llm_clients", {})

    step_definitions_code = ""
    step_instantiations_code = ""
    dependencies_code = "    dependencies = {\n"


    collected_import_lines.update([
        "from promptgraphtools.core.step_graph import StepGraph",
        "from promptgraphtools.core.step import Step",
        "from promptgraphtools.core.fan_out_step import FanOutStep",
        "from promptgraphtools.core.conditional_router_step import ConditionalRouterStep",
        "from promptgraphtools.core.base_classes.step_like import StepLike"
    ])


    immediate_step_definitions = []
    deferred_step_definitions: Dict[str, Dict[str, Any]] = {}

    for step_def in steps_schema:
        step_name = step_def.get("step_name")
        step_type = step_def.get("step_type")
        required_inputs_step = step_def.get("required_inputs")
        required_outputs_step = step_def.get("required_outputs")
        step_config = step_def.get("configuration")

        if step_type == "Step":
            function_ref = step_config.get("function")
            llm_client = step_config.get("llm_client")
            end_tag = step_config.get("end_tag")
            end_instructions = step_config.get("end_instructions")

            if function_ref:
                function_file_name = f"{graph_name.replace(' ', '_').replace('-', '_').replace('.', '_')}_{function_ref}_function"
                file_path = f"functions/{function_file_name}.py"
                function_filepath_to_schema_map[file_path] = step_def

                if function_file_name not in function_definitions_code: # Check if already generated
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

                    input_id_lines = "# Inputs:\n"
                    if required_inputs_step:
                        for input_name in required_inputs_step:
                            input_id_lines += f"{input_name} = \"{input_name}\"\n"

                    output_id_lines = "# Outputs:\n"
                    if required_outputs_step:
                        for output_name in required_outputs_step:
                            output_id_lines += f"{output_name} = \"{output_name}\"\n"

                    function_code_content = f"""\
from typing import Any, Dict

# INPUT_IDS_START
{input_id_lines.strip()}
# INPUT_IDS_END
# OUTPUT_IDS_START
{output_id_lines.strip()}
# OUTPUT_IDS_END
def {function_ref}(inputs: Dict[str, Any]) -> Dict[str, Any]:
    # INPUT_VARS_START
    {input_extraction_lines.strip()}
    # INPUT_VARS_END
    # OUTPUT_VARS_START
    return {output_dict_return}
    # OUTPUT_VARS_END
    # END_OF_FUNCTION
"""
                    function_definitions_code[function_file_name] = function_code_content
                    function_name_map[function_file_name] = function_ref

                step_instantiation = f"""\
    {step_name} = Step(
        step_name='{step_name}',
        required_inputs={required_inputs_step},
        required_outputs={required_outputs_step},
        function={function_ref},
    )
"""
                immediate_step_definitions.append(step_instantiation)
            elif llm_client:
                template_var_name = f"{step_name.replace(' ', '_').replace('-', '_').replace('.', '_')}_template"
                template_file_name = f"{graph_name.replace(' ', '_').replace('-', '_').replace('.', '_')}_{template_var_name}"
                file_path = f"templates/{template_file_name}.py"
                template_filepath_to_schema_map[file_path] = step_def

                if template_file_name not in template_definitions_code: # Check if already generated
                    input_vars = ""
                    if required_inputs_step:
                        for input_name in required_inputs_step:
                            input_vars += f'{input_name} = "{input_name}"\n'

                    template_code_content = f"""\
# INPUT_VARS_START
{input_vars.strip()}
# INPUT_VARS_END
{template_var_name} = f\"\"\"
# Define your template string for step: {step_name} here
\"\"\"
"""
                    template_definitions_code[template_file_name] = template_code_content
                    template_name_map[template_file_name] = template_var_name

                step_instantiation = f"""\
    {step_name} = Step(
        step_name='{step_name}',
        required_inputs={required_inputs_step},
        required_outputs={required_outputs_step},
        template={template_var_name},
        llm_client={llm_client},
"""
                if end_tag:
                    step_instantiation += f"        end_tag='{end_tag}',\n"
                if end_instructions:
                    step_instantiation += f"        end_instructions='{end_instructions}',\n"
                step_instantiation += f"    )\n"
                immediate_step_definitions.append(step_instantiation)
            else:
                raise ValueError(f"Step '{step_name}' configuration is invalid.")

        elif step_type == "FanOutStep":
            input_key = step_config.get("input_key")
            output_key = step_config.get("output_key", "results")
            llm_client = step_config.get("llm_client")
            step_graph_ref = step_config.get("step_graph")
            concurrency = step_config.get("concurrency", 5)
            batch_mode = step_config.get("batch_mode", True)

            if step_graph_ref:
                step_graph_function_name = f"build_{step_graph_ref.replace(' ', '_').replace('-', '_').replace('.', '_')}_graph"
                step_instantiation = f"""\
    {step_name} = FanOutStep(
        step_name='{step_name}',
        required_inputs={required_inputs_step},
        required_outputs={required_outputs_step},
        input_key='{input_key}',
        output_key='{output_key}',
        step_graph={step_graph_function_name}(),
        concurrency={concurrency},
        batch_mode={batch_mode},
    )
"""
                deferred_step_definitions[step_name] = {'code_blob': step_instantiation, 'depends_on': [step_graph_ref]}

        elif step_type == "ConditionalRouterStep":
            steps_config = step_config.get("steps")
            default_step_ref = step_config.get("default")

            steps_route_map_code = "{"
            route_steps = []
            depends_on_steps = []
            for route_key, route_step_name in steps_config.items():
                step_ref_name = route_step_name.get('step_name')
                if step_ref_name:
                    route_steps.append(f"'{route_key}': {step_ref_name}")
                    depends_on_steps.append(step_ref_name)
                else:
                    raise ValueError(f"ConditionalRouterStep '{step_name}' route is missing 'step_name'.")

            steps_route_map_code += ", ".join(route_steps) + "}"

            default_step_code = f"{default_step_ref}" if default_step_ref else "None"

            step_instantiation = f"""\
    {step_name} = ConditionalRouterStep(
        name='{step_name}',
        required_inputs={required_inputs_step},
        required_outputs={required_outputs_step},
        steps={steps_route_map_code},
        default={default_step_code},
    )
"""
            deferred_step_definitions[step_name] = {'code_blob': step_instantiation, 'depends_on': depends_on_steps}

        elif step_type == "StepGraph":
            subgraph_step_name = step_name
            subgraph_required_inputs = required_inputs_step
            subgraph_required_outputs = required_outputs_step

            sub_graph_code_data = _generate_graph_code_recursive(
                schema={ "configuration": step_config, "graph_name": subgraph_step_name, "required_inputs": subgraph_required_inputs, "required_outputs": subgraph_required_outputs, "llm_clients": llm_clients_schema},
                collected_import_lines=collected_import_lines,
            )
            (
                sub_function_definitions_code,
                sub_step_defs,
                sub_main_graph_code,
                sub_imports,
                sub_template_definitions_code,
                sub_function_filepath_to_schema_map,
                sub_template_filepath_to_schema_map,
                sub_function_name_map,
                sub_template_name_map
            ) = sub_graph_code_data


            function_definitions_code.update(sub_function_definitions_code)
            template_definitions_code.update(sub_template_definitions_code)
            step_definitions_code += sub_step_defs
            step_definitions_code += f"\n{sub_main_graph_code}\n"
            collected_import_lines.update(sub_imports)
            function_name_map.update(sub_function_name_map)
            template_name_map.update(sub_template_name_map)
            function_filepath_to_schema_map.update(sub_function_filepath_to_schema_map) # Propagate filepath maps upwards
            template_filepath_to_schema_map.update(sub_template_filepath_to_schema_map) # Propagate filepath maps upwards


            subgraph_function_name = f"build_{subgraph_step_name.replace(' ', '_').replace('-', '_').replace('.', '_')}_graph"
            step_instantiation = f"    {step_name} = {subgraph_function_name}()\n"
            deferred_step_definitions[step_name] = {'code_blob': step_instantiation, 'depends_on': []}

        else:
            raise ValueError(f"Unknown step type: {step_type}")

    step_instantiations_code += "".join(immediate_step_definitions)

    ordered_deferred_steps = sorted(deferred_step_definitions.items(), key=lambda item: len(item[1]['depends_on']))
    for step_name, step_data in ordered_deferred_steps:
        step_instantiations_code += step_data['code_blob']

    for step_name, deps in dependencies_schema.items():
        deps_str = "[" + ", ".join([f"'{dep}'" for dep in deps]) + "]" if deps else "[]"
        dependencies_code += f"        '{step_name}': {deps_str},\n"
    dependencies_code += "    }\n"

    llm_client_definitions_for_this_graph = ""
    if llm_clients_schema:
        collected_import_lines.add("from promptgraphtools.core.llm_clients.gemini import Gemini")
        for client_name, client_config in llm_clients_schema.items():
            llm_client_definitions_for_this_graph += f"    {client_name} = Gemini(\n"
            llm_client_definitions_for_this_graph += f"        model=Gemini.Models.{client_config['model'].upper().replace('-', '_')},\n"
            llm_client_definitions_for_this_graph += f"        max_output_tokens={client_config['max_output_tokens']},\n"
            llm_client_definitions_for_this_graph += f"        temperature={client_config['temperature']},\n"
            llm_client_definitions_for_this_graph += f"        top_p={client_config['top_p']},\n"
            llm_client_definitions_for_this_graph += f"        use_tools={client_config['use_tools']},\n"
            llm_client_definitions_for_this_graph += f"    )\n\n"


    main_graph_code = f"""
def build_{graph_name.replace(' ', '_').replace('-', '_').replace('.', '_')}_graph() -> StepLike:
    \"\"\"
    Builds the {graph_name} StepGraph.
    \"\"\"
{llm_client_definitions_for_this_graph}{step_instantiations_code}
{dependencies_code}

    return StepGraph(
        graph_name='{graph_name}',
        steps=[{', '.join([step_name for step_name in dependencies_schema.keys()])}],
        dependencies=dependencies,
        required_inputs={required_inputs},
        required_outputs={required_outputs},
    )
"""
    return (
        function_definitions_code,
        step_definitions_code,
        main_graph_code,
        collected_import_lines,
        template_definitions_code,
        function_filepath_to_schema_map,
        template_filepath_to_schema_map,
        function_name_map,
        template_name_map
    )

def _consolidate_imports_to_string(import_lines: Set[str]) -> str:
    return "\n".join(sorted(list(import_lines))) + "\n\n"
