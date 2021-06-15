from botcity.core import DesktopBot


class Bot(DesktopBot):
    def action(self, execution):
        # Opens the BotCity website.
        self.browse("https://botcity.dev/en")

        # add an image for search
        # self.add_image("start", self.get_resource_abspath("start.png"))

        # Post an artifact into BotMaestro
        # self.maestro.post_artifact(
        #     execution.task_id, "artifact_name", "artifact_path.xlsx"
        # )


if __name__ == '__main__':
    Bot.main()
