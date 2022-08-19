import os
import shutil

project_type = "{{cookiecutter.project_type | lower}}"
bot_id = "{{ cookiecutter.bot_id|replace(' ', '_') }}"

proj_files = {
    "desktop": {"remove": ["webbot.py", "bothbot.py", "custombot.py", "scriptbot.py", "requirements.txt"], "use": None},
    "web": {"remove": ["bot.py", "bothbot.py", "custombot.py", "scriptbot.py", "requirements.txt"], "use": "webbot.py"},
    "both": {"remove": ["bot.py", "webbot.py", "custombot.py", "scriptbot.py", "requirements.txt"], "use": "bothbot.py"},
    "custom": {"remove": ["bot.py", "webbot.py", "bothbot.py", "scriptbot.py", "requirements.txt"], "use": "custombot.py"},
    "script": {"remove": ["__init__.py", "__main__.py", "bot.py", "bothbot.py", "webbot.py", "custombot.py"], "use": "scriptbot.py"}
}

config = proj_files.get(project_type)

if not config:
    raise ValueError(f"Invalid project type: {project_type}")

for f in config["remove"]:
    os.remove(os.path.join(bot_id, f))

if config["use"]:
    os.rename(os.path.join(bot_id, config["use"]), os.path.join(bot_id, "bot.py"))

if project_type == "script":
    root_files = [
        "MANIFEST.in",
        "setup.py",
        "VERSION",
        "requirements.txt"
    ]

    for f in root_files:
        os.remove(f)
    os.rename("script_build.sh", "build.sh")
    os.rename("script_build.bat", "build.bat")
else:
    os.remove("script_build.sh")
    os.remove("script_build.bat")
