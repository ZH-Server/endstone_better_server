from endstone.plugin import Plugin

from better_server.listener import PLayerListener

class BetterServer(Plugin):
    api_version = "0.5"

    def on_load(self) -> None:
        self.logger.info("BetterServer has been loaded!")

    def on_enable(self) -> None:
        self.logger.info("BetterServer has been enabled!")

        self.register_events(self)  # register event listeners defined directly in Plugin class
        self.register_events(PLayerListener(self))  # you can also register event listeners in a separate class

        self.server.scheduler.run_task(self, self.log_time, delay=0, period=20 * 1)  # every second

    def on_disable(self) -> None:
        self.logger.info("BetterServer has been disabled!")
