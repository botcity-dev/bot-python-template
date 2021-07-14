from botcity.core import DesktopBot


class Bot(DesktopBot):
    def action(self, execution):
        # add an image for search
        # self.add_image("start", self.get_resource_abspath("start.png"))

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.browse("http://botcity.dev")

        # Post an artifact into BotMaestro
        # self.maestro.post_artifact(
        #     execution.task_id, "artifact_name", "artifact_path.xlsx"
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
