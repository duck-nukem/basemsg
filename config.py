import os
from configparser import ConfigParser
from pathlib import Path


def read_config() -> ConfigParser:
    script_directory = Path(os.path.dirname(os.path.abspath(__file__)))
    config_parser = ConfigParser()
    config_parser.read_file(open(script_directory / 'config.cfg'))

    return config_parser
