from SettingsManager.exec_cmd import exec_with_sudo


def change_state_of_damon(cmd: str, demon_name: str):
    return exec_with_sudo(['systemctl', cmd, demon_name])


def autostart_post_handler(data):
    # TODO
    if data["sub"] == "error_report":
        pass
    return change_state_of_damon(data["cmd"], "")