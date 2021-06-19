from subprocess import Popen, PIPE

SUDO_PASSWORD = None


def check_password(password):
    proc = Popen(["sudo", "-v"], stdout=PIPE, stderr=PIPE, stdin=PIPE).communicate(input=password)
    print(proc[0].decode())
    print(proc[1].decode())
    return len(proc[1].decode()) == 0  # if password incorrect proc[1] - error text


def ask_sudo_password():
    proc = Popen(["zenity", "--password"], stdout=PIPE, stderr=PIPE, stdin=PIPE).communicate()
    out = proc[0].decode()
    print(out)
    return out

def get_sudo_password():
    global SUDO_PASSWORD
    if SUDO_PASSWORD is None:
        new_password = ask_sudo_password()# + "\n\n\n"
        print(f"{new_password=}")
        # 3 "\n" for get error if password incorrect
        if check_password(new_password.encode()):
            SUDO_PASSWORD = new_password.encode()
    return SUDO_PASSWORD