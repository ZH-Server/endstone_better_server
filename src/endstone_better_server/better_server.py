from endstone.plugin import Plugin
from endstone import ColorFormat
from endstone.event import *
class BetterServer(Plugin):
    api_version = "0.5"

    def on_enable(self) -> None:
        self.register_events(self)

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        self.logger.info(ColorFormat.BOLD + ColorFormat.WHITE + f"{event.player.name} {event.player.xuid} using {event.player.device_os}"+ ColorFormat.YELLOW + f" {event.player.location}" + ColorFormat.WHITE + "has joined")
        event.player.send_toast(f"Welcome! §e§l{event.player.name}§r","欢迎回到 §s§lZH-Server§r!")
