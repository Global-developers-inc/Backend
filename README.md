# Backend

# Usage
## GET
/\<category\>
return information about category
### repo
keys - repo id, values - [repo discription, is enabled]. 
### theme
Возращает список тем в ключе data и примененную
```
{
    "apply": "'Layan-dark'\n",
    "data": [
        "Adwaita-dark",
        "Adwaita",
        "High Contrast"
    ],
    "error_text": ""
}
```
### autostart
in process
### user
```
{
     "autologin": false
}
```
### domain
Ничего не возращает
## POST
/\<category\>
по сути действия. полученый json определяет повдение
### repo 
if data["action"] == "add"
добавляет в repolist репо по адресу data["url"]
data["action"] == "enable":
Включить репо с id data["id"]
data['action'] == "disable":
отключить репо с id data["id"]
### theme
if data["action"] == "bg"
поставить на обои data["name"]
if data["action"] == "theme":
поставить data["name"] тему
### autostart
если data["cmd"] == enable включает ErrorChecker если data["sub"] == "error_report"
disable - отключить

если data["sub"] == "autostart" то соответветственно включить и выключить
### user
if data["actions"] == "avatar":
    сменить аватар на data["filename"]
in process
### domain
Просто пост запрос запускает join-to-domain.sh
