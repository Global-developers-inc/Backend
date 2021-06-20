from SettingsManager.scripts.repolist import change_repolist
from SettingsManager.exec_cmd import exec_cmd, exec_command, exec_with_sudo
from SettingsManager.utils import *


def change_avatar(filename):
    return exec_cmd(["yes", "|", "mv", "-r", "~/.face", filename])  # move file to ~/.face


def user_post_handler(data):
    if data["action"] == "avatar":
        return change_avatar(data["filename"])
    return toggle_autologin()


def check_autologin():
    username = exec_command(["whoami"])[0].decode().strip()
    enabled = False
    autologin = False
    data = read_file("/etc/gdm/custom.conf")
    for line in data:
        if line == "AutomaticLoginEnable=True":
            enabled = True
        if line == f"AutomaticLogin={username}":
            autologin = True
    return autologin, enabled, data


def toggle_autologin():
    username = exec_command(["whoami"])[0].decode().strip()
    autologin, enabled, content = check_autologin()
    indx = content.index("[daemon]")
    if enabled:
        for index, line in enumerate(content):
            if line == f"AutomaticLogin={username}":
                content[index] = "#" + line            
            elif line == f"#AutomaticLogin={username}":
                content[index] = line.replace("#", "")
    else:
        content.insert(indx + 1, "AutomaticLoginEnabled=True")
    if not autologin:  # enable autologin
        indx = content.index("[daemon]")
        content.insert(indx + 1, f"AutomaticLogin={username}")
    with open("tmp_gdm_config", "w+", encoding='utf-8') as f:
        f.write("\n".join(content))
    return exec_with_sudo(["mv",  "tmp_gdm_config", "/etc/gdm/custom.conf"])


def user_get():
    autologin = check_autologin()
    return {
        "autologin": autologin[0] and autologin[1],
    }, 200
    pass