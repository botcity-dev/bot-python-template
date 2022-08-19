"""
This is a template for a custom script bot.

Make sure to add your dependencies to the requirements.txt file.
"""

"""
Example Desktop Bot
"""
# from botcity.core import DesktopBot
# bot = DesktopBot()

# if not bot.find( "visual_element", matching=0.97, waiting_time=60000):
#     print("visual_element was not found")
# bot.click_relative(20, -35)


"""
Example Web Bot
"""
# from botcity.web import WebBot, Browser, By
# webbot = WebBot()
# # Configure whether or not to run on headless mode
# webbot.headless = False

# # Uncomment to change the default Browser to Firefox
# # webbot.browser = Browser.FIREFOX

# # Uncomment to set the WebDriver path
# # webbot.driver_path = "<path to your WebDriver binary>"

# # Opens the BotCity website.
# webbot.browse("https://www.botcity.dev")

# # Stop the browser and clean up
# webbot.stop_browser()


"""
BotCity Maestro Integration
"""
# from botcity.maestro import *

# # Instantiate BotCity Maestro SDK
# maestro = BotMaestroSDK()
# # Login with BotCity Maestro using workspace credentials
# maestro.login(server="<your maestro url>", login="<your login>", key="<your password>")

