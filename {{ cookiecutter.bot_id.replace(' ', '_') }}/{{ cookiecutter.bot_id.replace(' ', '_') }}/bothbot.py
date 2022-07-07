"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.web import WebBot, Browser
from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(WebBot):
    def action(self, execution=None):
        # Configure whether or not to run on headless mode
        self.headless = False

        # Instantiate a DesktopBot
        desktop_bot = DesktopBot()
        # Execute operations with the DesktopBot as desired
        # desktop_bot.control_a()
        # desktop_bot.control_c()
        # desktop_bot.get_clipboard()

        # Uncomment to change the default Browser to Firefox
        # self.browser = Browser.FIREFOX

        # Uncomment to set the WebDriver path
        # self.driver_path = "<path to your WebDriver binary>"

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.browse("https://www.botcity.dev")

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

        # Wait for 10 seconds before closing
        self.wait(10000)

        # Stop the browser and clean up
        self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
