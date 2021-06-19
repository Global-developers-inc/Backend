from SettingsManager.exec_cmd import exec_cmd, exec_command
from SettingsManager.utils import get_themes_list


def set_colortheme(theme):
    return exec_cmd(["gsettings", 'set', 'org.gnome.desktop.interface', 'gtk-theme', theme])


def set_bg(filename):
    return exec_cmd(['gsettings', 'get', 'org.gnome.desktop.background', 'picture-uri', filename])


def get_themes():
    # get all themes
    themes = get_themes_list("/usr/share/themes")
    installed_theme = exec_command(
        ["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"]
    ).communicate()
    if len(installed_theme[1]) > 0:
        return {
            "data": "error",
            "error_text": "error",
        }
    return {"data": themes, "apply": installed_theme[0].decode(), "error_text": ""}, 201


def decoration_post(data):
    if data["action"] == "bg":
        return set_colortheme(data['name'])
    return set_colortheme(data["name"])