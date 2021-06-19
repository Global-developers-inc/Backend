from SettingsManager.exec_cmd import exec_cmd


def join_to_domain(data):
    return exec_cmd(["join-to-domain.sh"])


def domain_get():
    return "domain get."