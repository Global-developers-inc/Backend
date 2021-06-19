from SettingsManager.exec_cmd import exec_with_sudo
from SettingsManager.sudo import get_sudo_password


def disable_demon(demon_name: str):
    return exec_with_sudo(['systemctl', "disable", demon_name])


def enable_demon(demon_name: str):
    return exec_with_sudo(['systemctl', "enable", demon_name])


def disable_gdm(data):
    return disable_demon("gdm")