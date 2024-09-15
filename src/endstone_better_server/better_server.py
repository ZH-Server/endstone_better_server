from endstone.plugin import Plugin
from endstone import ColorFormat
from endstone.event import *
import time

class BetterServer(Plugin):
    api_version = "0.5"

    def on_enable(self) -> None:
        self.register_events(self)

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        self.server.broadcast_message(ColorFormat.BOLD + ColorFormat.WHITE + f"{event.player.name}" + ColorFormat.YELLOW + "来啦~")
        self.logger.info(ColorFormat.BOLD + ColorFormat.WHITE + f"{event.player.name} {event.player.xuid} using {event.player.device_os}"+ ColorFormat.YELLOW + f"{event.player.dimension} {event.player.location}" + ColorFormat.WHITE + "has joined")
        event.player.send_toast("Welcome!","欢迎回到 ZH-Server!")
