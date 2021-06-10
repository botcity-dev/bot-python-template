from botcity.core import DesktopBot


class Bot(DesktopBot):
    def action(self, execution):
        # Opens the BotCity website.
        self.browse("https://botcity.dev/en")


if __name__ == '__main__':
    Bot.main()