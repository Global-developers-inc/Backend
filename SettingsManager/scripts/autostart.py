from SettingsManager.exec_cmd import exec_with_sudo


def change_state_of_damon(cmd: str, demon_name: str):
    return exec_with_sudo(['systemctl', cmd, demon_name])


def autostart_post_handler(data):
    # TODO
    if data["sub"] == "error_report":
        return change_state_of_damon(data["cmd"], "error_checker") ##  install.sh write error reporter to systemD service list
    return change_state_of_damon(data["cmd"], "HiRed") # this app


def autostart_get_handler():
    # TODO
    return {}, 201