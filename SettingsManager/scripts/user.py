from SettingsManager.scripts.repolist import change_repolist
from SettingsManager.exec_cmd import exec_cmd, exec_command, exec_with_sudo
from SettingsManager.utils import *


def change_avatar(filename):
    return exec_cmd(["yes", "|", "mv", "-r", "~/.face", filename])  # move file to ~/.face


def user_post_handler(data):
    if data["actions"] == "avatar":
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
    indx = 0
    if enabled:
        for index, line in enumerate(content):
            if line == f"AutomaticLogin={username}":
                indx = index
                content[index] = "#" + line            
            elif line == f"#AutomaticLogin={username}":
                indx = index
                content[index] = line.replace("#", "")
    if not autologin:
        content.insert(indx, "AutomaticLoginEnabled=True")
    text = "\n".join(content)
    return exec_with_sudo(["echo", f'\"{text}\"', ">", "/etc/gdm/custom.conf"])


def user_get():
    autologin = check_autologin()
    return {
        "autologin": autologin[0] and autologin[1],
    }, 200
    pass