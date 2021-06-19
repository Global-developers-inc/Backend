from SettingsManager.exec_cmd import exec_cmd, exec_with_sudo
from SettingsManager.sudo import get_sudo_password


def get_repolist() -> dict:
    """
    return repo list in dict where key - repo url, value - repo description
    """
    cmd = exec_cmd(["dnf", "repolist"])
    if cmd["terminated"]:
        return cmd
    repos =  list(filter(lambda s: s, cmd["data"]))[1:]  # get output and delete title
    repos = list(map(lambda x: x.split(), repos))
    res = {}
    for s in repos:
        res[s[0]] = ' '.join(s[1:])
    return res


def in_repolist(repo_id: str) -> bool:
    return repo_id in get_repolist()
    

def add_repo(repo_url: str) -> list:
    return exec_with_sudo([f"dnf", "config-manager", "--add-repo", repo_url]), 201


def disable_repo(repo_id: str) -> list:
    if not in_repolist(repo_id):
        return {}, 404
    res = exec_with_sudo(
        ["dnf", "config-manager", "--set-disabled", repo_id])
    return res, 201


def enable_repo(repo_id: str) -> list:
    if not in_repolist(repo_id):
        return {}, 404
    return exec_with_sudo(
        ["dnf", "config-manager", "--set-disabled", repo_id])


def show_repolist() -> list:
    return get_repolist(), 201


def change_repolist(data):
    if data["action"] == "add":
        return add_repo(data["url"])
    elif data["action"] == "enable":
        return enable_repo(data["id"])
    return disable_repo(data["id"])