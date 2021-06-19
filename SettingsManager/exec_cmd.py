from SettingsManager.sudo import get_sudo_password
from os import error
from subprocess import PIPE, Popen


def exec_with_sudo(args: list) -> dict:
    args.insert(0, "sudo")
    args.insert(1, "-S")
    proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate(input=get_sudo_password()) 
    return {
        "data": proc[0].decode(), 
        "error_text": proc[1].decode(),
    }


def exec_cmd(args: list) -> dict:
    proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate(input=get_sudo_password()) 
    return {
        "data": proc[0].decode(), 
        "error_text": proc[1].decode(),
    }
