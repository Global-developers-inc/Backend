from SettingsManager.settings import *
from SettingsManager.scripts.__all_scripts import *


"""
Словарь с сылками на функции
"""
CATEGORYS = {
    "repo": Settings(
        get_func=get_repolist,
        post_func=change_repolist,
    ),
    "theme": Settings(
        get_func=get_themes,
        post_func=decoration_post,
    ), 
    "autostart": Settings(
        get_func=autostart_get_handler,
        post_func=autostart_post_handler,
    ),
    "user": Settings(
        get_func=user_get,
        post_func=user_post_handler,
    ), 
    "domain": Settings(
        get_func=domain_get, 
        post_func=join_to_domain,
    )
}
