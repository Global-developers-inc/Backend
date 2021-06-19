SUDO_PASSWORD = "***"


def get_sudo_password():
    if SUDO_PASSWORD is None:
        # show ask password dialog
        pass
    return SUDO_PASSWORD.encode()