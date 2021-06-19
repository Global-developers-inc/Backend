from SettingsManager.exec_cmd import exec_cmd, exec_command
from subprocess import Popen, PIPE


def change_avatar(filename):
    return exec_cmd(["yes", "|", "mv", "-r", "~/.face", filename])  # move file to ~/.face


def user_post_handler(data):
    if data["actions"] == "avatar":
        return change_avatar(data["filename"])


def user_get():
    # TODO is autostart?
    return {}, 200
    pass