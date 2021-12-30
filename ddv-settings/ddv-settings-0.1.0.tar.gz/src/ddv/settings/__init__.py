import os

import configparser

settings = {}


def read(settings_file_path):

    global settings

    if settings_file_path.endswith(".ini"):
        settings = _read_ini_settings(settings_file_path)


def export(target_module=None, export_env=True, prefix=""):

    global settings

    for section in settings:
        for key in settings[section]:
            value = settings[section][key]

            full_name = f"{prefix}_{section}_{key}".upper()

            if target_module:
                setattr(target_module, full_name, value)

            if export_env:
                os.environ[full_name] = value


def _read_ini_settings(ini_file_path):
    config = configparser.ConfigParser()
    config.read(ini_file_path)

    settings = {}

    for section in config.sections():
        settings[section] = {}
        for key in config[section]:
            settings[section][key] = config[section][key]

    return settings