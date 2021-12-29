"""
Auxiliary functions to handle user configuration for `gutenberg2kindle`
"""

from typing import Final, Optional, Union

import usersettings  # type: ignore


SETTINGS_SMTP_SERVER: Final[str] = "smtp_server"
SETTINGS_SMTP_PORT: Final[str] = "smtp_port"
SETTINGS_SENDER_EMAIL: Final[str] = "sender_email"
SETTINGS_KINDLE_EMAIL: Final[str] = "kindle_email"
SETTINGS_FORMAT: Final[str] = "format"
AVAILABLE_SETTINGS: Final[list[str]] = [
    SETTINGS_SMTP_SERVER,
    SETTINGS_SMTP_PORT,
    SETTINGS_SENDER_EMAIL,
    SETTINGS_KINDLE_EMAIL,
    SETTINGS_FORMAT,
]

FORMAT_IMAGES: Final[str] = "images"
FORMAT_NO_IMAGES: Final[str] = "no_images"
FORMAT_AUTO: Final[str] = "auto"
VALID_FORMATS: Final[list[str]] = [
    FORMAT_IMAGES,
    FORMAT_NO_IMAGES,
    FORMAT_AUTO,
]

settings = usersettings.Settings("gutenberg2kindle")


def setup_settings() -> usersettings.Settings:
    """
    Sets up and returns an instance of the `usersettings.Settings` model
    with values for all the required settings used in the project
    """

    settings.add_setting(SETTINGS_SMTP_SERVER, str, "")
    settings.add_setting(SETTINGS_SMTP_PORT, int, 465)
    settings.add_setting(SETTINGS_SENDER_EMAIL, str, "")
    settings.add_setting(SETTINGS_KINDLE_EMAIL, str, "")
    settings.add_setting(SETTINGS_FORMAT, str, FORMAT_AUTO)
    settings.load_settings()


def get_config(name: Optional[str] = None) -> Optional[Union[dict, int, str]]:
    """
    Given a setting name, returns the value for said setting.

    If no name is given, returns a dictionary with all settings
    and their corresponding values.
    """

    if name is None:
        return settings

    if name not in AVAILABLE_SETTINGS:
        raise ValueError(f"`{name}` is not a valid setting name")

    return settings[name]


def set_config(name: str, value: Union[int, str]) -> None:
    """
    Given a setting name and a value, sets the value for said setting.
    """

    if name not in AVAILABLE_SETTINGS:
        raise ValueError(f"`{name}` is not a valid setting name")

    if name == SETTINGS_FORMAT and value not in VALID_FORMATS:
        raise ValueError(
            f"`{value}` is not a valid format "
            f"(expected one of: {VALID_FORMATS})"
        )

    settings[name] = value
    settings.save_settings()
