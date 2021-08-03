# Creating a new Project using Cookiecutter

```bash
python -m cookiecutter https://github.com/botcity-dev/bot-python-template
```

When running this command you will be prompted for the following information:

!!! warning inline end
    **bot_id** value **must** match the Bot label configured on BotMaestro if using the integration.

- **project_type**: This will define which bot template is generated.
    The options are Desktop or Web. Select Web if your automation involve only websites otherwise pick
    Desktop.

- **bot_id**: This will be the name of your Python module.

- **project_name**: This is the name of the project. You can pick any name you would like.

- **project_short_description**: This is a short description of the bot.

Over the next chapter we will explore the package and guide you on the most common operations to be executed.