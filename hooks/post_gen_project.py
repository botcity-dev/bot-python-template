import os

project_type = "{{cookiecutter.project_type | lower}}"
bot_id = "{{ cookiecutter.bot_id|replace(' ', '_') }}"

proj_files = {
    "desktop": {"remove": ["webbot.py", "bothbot.py", "custombot.py"], "use": None},
    "web": {"remove": ["bot.py", "bothbot.py", "custombot.py"], "use": "webbot.py"},
    "both": {"remove": ["bot.py", "webbot.py", "custombot.py"], "use": "bothbot.py"},
    "custom": {"remove": ["bot.py", "webbot.py", "bothbot.py"], "use": "custombot.py"}
}

config = proj_files.get(project_type)

if not config:
    raise ValueError(f"Invalid project type: {project_type}")

for f in config["remove"]:
    os.remove(f)

if config["use"]:
    os.rename(config["use"], "bot.py")
