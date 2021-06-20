from SettingsManager.exec_cmd import exec_cmd, exec_command
from subprocess import Popen, PIPE


def change_avatar(filename):
    return exec_cmd(["yes", "|", "mv", "-r", "~/.face", filename])  # move file to ~/.face


def user_post_handler(data):
    if data["actions"] == "avatar":
        return change_avatar(data["filename"])


def check_autologin():
    username = exec_command(["whoami"])[0].decode().strip()
    print(username)
    enabled = False
    autologin = False
    with open("/etc/gdm/custom.conf", "r", encoding='utf-8') as f:
        data = f.read().splitlines()
    for line in data:
        if line == "AutomaticLoginEnable=True":
            enabled = True
        if line == f"AutomaticLogin={username}":
            autologin = True
    return autologin and enabled


def user_get():
    return {
        "autologin": check_autologin(),
    }, 200
    pass