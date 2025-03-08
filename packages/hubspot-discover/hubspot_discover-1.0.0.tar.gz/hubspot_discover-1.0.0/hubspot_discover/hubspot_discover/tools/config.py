import os
from dotenv import dotenv_values


def read_value(key, env_file=".env"):
    """
    Reads the value associated with 'key' from the .env file.
    If the key is not present in the file, returns the value from the environment variable.

    :param key: The key to search for.
    :param env_file: Path to the .env file (default: '.env').
    :return: The value associated with 'key', or None if it is not defined.
    """
    # Load the contents of the .env file into a dictionary.
    config = dotenv_values(env_file)

    # If the key is found in the .env file and its value is not empty, return its value.
    if key in config and config[key]:
        return config[key]

    # Otherwise, return the value from the environment variables.
    return os.environ.get(key)
