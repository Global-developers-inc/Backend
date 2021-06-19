from SettingsManager.sudo import get_sudo_password
from os import error
from subprocess import PIPE, Popen


def exec_with_sudo(args: list) -> dict:
    args.insert(0, "sudo")
    args.insert(1, "-S")
    password = get_sudo_password()
    if password is None:
        return {
            "data": "forbidden",
            "error_text": "Incorrect sudo password",
        }
    proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate(input=password) 
    created = 201 if len(proc[1]) == 0 else 400
    return {
        "data": proc[0].decode(), 
        "error_text": proc[1].decode(),
    }, created


def exec_cmd(args: list) -> dict:
    proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()
    created = 201 if len(proc[1]) == 0 else 400
    return {
        "data": proc[0].decode(), 
        "error_text": proc[1].decode(),
    }, created

