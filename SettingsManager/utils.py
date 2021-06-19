import os


def read_file(file_name: str):
    if not os.path.isfile(file_name):
        return ""
    file_data = ""
    with open(file_name, 'r', encoding="utf-8") as file:
        file_data = file.read().splitlines()
    return file_data


def get_themes_list(dir_name: str) -> list:
    theme_list = []
    for theme in os.listdir(dir_name):
        for line in read_file(f"{dir_name}/{theme}/index.theme"):
            if "Name=" in line:
                theme_list.append(line.replace("Name=", ""))
    return theme_list
