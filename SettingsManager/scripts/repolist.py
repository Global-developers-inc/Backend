from SettingsManager.exec_cmd import exec_cmd, exec_with_sudo, exec_command


def get_repolist() -> dict:
    """
    return repo list in dict where key - repo url, value - repo description
    """
    cmd = str(exec_command(["dnf", "repolist"])[0].decode())
    repos =  list(filter(lambda s: s, cmd.split('\n')))[1:]  # get output and delete title
    repos = list(map(lambda x: x.split(), repos))
    
    enabled = str(exec_command(["dnf", "repolist", "enabled"])[0].decode())
    res = {}
    for s in repos:
        print(s)
        res[s[0]] = [' '.join(s[1:]), True if s[0] in enabled else False]
    return res


def in_repolist(repo_id: str) -> bool:
    return repo_id in get_repolist()
    

def add_repo(repo_url: str) -> list:
    return exec_with_sudo([f"dnf", "config-manager", "--add-repo", repo_url])


def disable_repo(repo_id: str) -> list:
    if not in_repolist(repo_id):
        return {}, 404
    res = exec_with_sudo(
        ["dnf", "config-manager", "--set-disabled", repo_id])
    return res


def enable_repo(repo_id: str) -> list:
    if not in_repolist(repo_id):
        return {}, 404
    return exec_with_sudo(
        ["dnf", "config-manager", "--set-disabled", repo_id])


def add_repo_with_SSL(repo_url: str, ssl_location: str):
    name = repo_url.replace('https://', "")
    return exec_with_sudo(
        [
            "echo", f"\"[{name}]\nbaseurl={repo_url}\nproxy_sslcacert={ssl_location}\nenabled=1\nname=User repo with SSL\"", "" ">", 
            f"/etc/yum.repos.d/{name}.repo"
        ]
    )


def change_repolist(data):
    if data["action"] == "add_ssl":
        return add_repo_with_SSL(data["url"], data["ssl"])
    elif data["action"] == "add":
        return add_repo(data["url"])
    elif data["action"] == "enable":
        return enable_repo(data["id"])
    return disable_repo(data["id"])