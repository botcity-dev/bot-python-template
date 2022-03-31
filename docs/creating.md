# Creating a new Project using Cookiecutter

```bash
python -m cookiecutter https://github.com/botcity-dev/bot-python-template/archive/main.zip
```

When running this command you will be prompted for the following information:

!!! warning inline end
    **bot_id** value **must** match the Bot label configured on BotMaestro if using the integration.

- **project_type**: This will define which bot template is generated.
    The options are **Desktop**, **Web**, **Both** or **Custom**.
    - Select **Desktop** for general Desktop or non-headless Web automations.
    - Select **Web** if your automation involve only websites.
    - Select **Both** if your automation involves a mix.
    - Select **Custom** if you would like to add your own libraries or create an automation using only BotCity plugins.

- **bot_id**: This will be the name of your Python module. It can only contain letters (a-z or A-Z), underscore (_) and must end with a letter (a-z or A-Z).

- **project_name**: This is the name of the project. You can pick any name you would like.

- **project_short_description**: This is a short description of the bot.

Over the next chapter we will explore the package and guide you on the most common operations to be executed.