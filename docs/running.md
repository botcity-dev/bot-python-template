# Running Your Code

This chapter will cover a couple different ways in which you can run your code for testing
and production.

## Direct execution via IDE or Command Line

The `bot.py` file inside of the package has special code which invokes the `main` method
on the bot class. This allow for direct execution of the bot via your favorite IDE or the 
command line.
```python
if __name__ == '__main__':
    Bot.main()
```

Here is how to start the code via the command line.
```shell
python bot.py
```

## Using the Module Entry Point

The package has a module entry point `__main__.py` which imports the `bot.py` module and
dynamically identify the Bot class for execution.

To start your bot via the entry point do:

```shell
# Assuming your bot_id used during creation of the package
# is botPython. Adjust as needed for your case.
python -m botPython
```

!!! note
    This is the method used by the BotCity BotRunner when using the Bot Maestro orchestration.
