import os

from google.protobuf.json_format import MessageToJson, Parse
from google.protobuf.message import Message


def read_config_from_file(
    config: Message,
    file: str,
):
    """Read json-based config file into protobuf message

    Args:
        config (google.protobuf.message): Protobuf message to merge into
        file (str): Config file to read
    """
    with open(file) as config_stream:
        config_text = config_stream.read()
        return Parse(config_text, config, ignore_unknown_fields=True)


def write_config_to_file(
    config: Message,
    file: str,
):
    """Write json-based config file from protobuf message

    Args:
        config (google.protobuf.message): Protobuf message to write
        file (str): Config file to write
    """
    config_text = MessageToJson(
        config,
        indent=2,
        always_print_fields_with_no_presence=True,
    )
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, mode="w") as config_stream:
        config_stream.write(config_text)


def read_config_from_environ(
    config: Message,
    environ_mapping: dict,
):
    """Read environ variables into protobuf message

    Args:
        config (google.protobuf.message): Protobuf message to merge into
        environ_mapping (dict): Environ mapping in { "env_name", ("field_name", "field_type", "default_value") }
    """
    for env_name, (field_name, field_type, *default_value) in environ_mapping.items():
        env_value = os.getenv(env_name, default_value[0] if default_value else None)
        if env_value:
            converted_value = _convert_environ_value(env_value, field_type)
            if hasattr(config, field_name):
                setattr(config, field_name, converted_value)


def _convert_environ_value(value, type):
    if type == "int":
        return int(value)
    elif type == "float":
        return float(value)
    elif type == "bool":
        return value.lower() in ("true")
    else:
        return value
