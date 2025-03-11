import os
import ast
import re


# Function to parse environment variables into a dictionary
def parse_env_to_dict(prefix):
    result = dict()
    for key, value in os.environ.items():
        if key.startswith(prefix):
            # Split the key by double underscores "__"

            parts = key[len(prefix) + 2:].lower().split("__")
            current_dict = result
            for part in parts[:-1]:
                if part not in current_dict:
                    current_dict[part] = {}
                current_dict = current_dict[part]

            # Handle specific cases
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            elif re.match(r'^[+-]?\d+$', value):
                value = int(value)
            elif re.match(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$', value):
                value = float(value)
            # Evaluate the value
            try:
                current_dict[parts[-1]] = ast.literal_eval(value)
            except Exception as e:
                current_dict[parts[-1]] = value
    return result


# Merge the template dictionary with the parsed environment variables
def merge_template_with_env(template, env):
    result = template.copy()
    for key, value in env.items():
        if isinstance(value, dict):
            if key in result and isinstance(result[key], dict):
                result[key] = merge_template_with_env(result[key], value)
            else:
                result[key] = value
        else:
            result[key] = value
    return result


def parse_env_to_list(prefix,default=None, separator=','):
    result = default
    for key, value in os.environ.items():
        if key.startswith(prefix):
            result = value.split(separator)
    return result


def final_model_name(name):
    name = name.replace('/', '--')
    return f'trec--{name}'