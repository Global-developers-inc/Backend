from SettingsManager.settings import *
from SettingsManager.scripts.__all_scripts import *


"""
Словарь с сылками на функции
"""
CATEGORYS = {
    "repo": Settings(
        get_func=show_repolist,
        post_func=change_repolist,
    ),
}
