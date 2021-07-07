import os

project_type = "{{cookiecutter.project_type | lower}}"

if project_type == "web":
    os.remove(os.path.join("{{cookiecutter.bot_id}}", "bot.py"))
    os.rename(os.path.join("{{cookiecutter.bot_id}}", "webbot.py"), os.path.join("{{cookiecutter.bot_id}}", "bot.py"))
else:
    os.remove(os.path.join("{{cookiecutter.bot_id}}", "webbot.py"))
