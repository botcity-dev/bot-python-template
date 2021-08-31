import os

project_type = "{{cookiecutter.project_type | lower}}"

proj_files = {
    "desktop": {"remove": ["webbot.py", "bothbot.py"], "use": None},
    "web": {"remove": ["bot.py", "bothbot.py"], "use": "webbot.py"},
    "both": {"remove": ["bot.py", "webbot.py"], "use": "bothbot.py"}
}

config = proj_files.get(project_type)

if not config:
    raise ValueError(f"Invalid project type: {project_type}")

for f in config["remove"]:
    os.remove(os.path.join("{{cookiecutter.bot_id}}", f))

if config["use"]:
    os.rename(os.path.join("{{cookiecutter.bot_id}}", config["use"]), os.path.join("{{cookiecutter.bot_id}}", "bot.py"))
