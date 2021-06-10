# Exploring the project

If you execute the cookiecutter command above and select the default values, you will end up
with the following structure:
```
 botPython
 ├── MANIFEST.in       <- This file defines the content of the package such as images.
 ├── README.md         <- Simple README file for your bot project.
 ├── VERSION           <- This file defines the Bot package version.
 ├── botPython         <- Main module for your Bot package.
 │   ├── __init__.py
 │   ├── __main__.py   <- Entrypoint for the module. You don't need to bother with this file.
 │   ├── bot.py        <- Module for your bot code. Here is where you will develop your bot.
 │   └── resources     <- Folder containing resources useful for the Bot.
 ├── build.bat         <- Batch script to generate the package
 ├── build.sh          <- Shell script to generate the package
 ├── requirements.txt  <- File describing the python dependencies for your Bot.
 └── setup.py          <- Setup file for the package.
```

The main files to be modified are:

- **bot.py**: Change this file and add here the code for your bot.

- **resources**: Add into this folder files to be used with your bot such as images, spreadsheets and etc.

- **VERSION**: Change the content of this file when updating the version of your bot.
It is recommended to use versions in the format X.Y. E.g. 1.0, 1.1, 2.5, 3.10.

## Resources

By default this project is configured to add into the package all files and subfolders that 
are added under the `resources` folder.

The bot base class offers an utility method to handle files taking into consideration the package path.
Please refer to the BotCity Framework documentation under the Bot API for the `get_resource_abspath` method.

Here is an example:

```python
class Bot(DesktopBot):
    def action(self, execution):
        # Add the resource start.png. 
        # Note the self.get_resource_abspath call to handle
        # the package path
        self.add_image("start", self.get_resource_abspath("start.png"))
```

!!! warning
    If adding **new** resource folders parallel to the existing `resources` folder,
    make sure to change the `MANIFEST.in` file and also add the folder name
    under `package_data` at `setup.py`. 

## Bot Code

This template project contains a skeleton class under `bot.py` with an initial example
which opens up the browser with the BotCity website.

The base class, `DesktopBot`, contains all the functions of the BotCity Python Core Framework
as methods so please keep in mind to use `self.` when invoking the methods.


```python
class Bot(DesktopBot):
    def action(self, execution):
        # using browse from browser module
        self.browse(...)
        # using find from display module
        self.find(...)
        # using mouse_move from mouse module
        self.mouse_move(x=100, y=200)
        # using enter from keyboard module
        self.enter()
```

!!! warning
    In case you use a different module for your main bot (instead of the default `bot.py`),
    make sure to change the `__main__.py` file to load the proper module. 
