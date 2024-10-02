from endstone.plugin import Plugin
from endstone.event import *
class BetterServer(Plugin):
    api_version = "0.5"

    def on_enable(self) -> None:
        self.register_events(self)

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        event.join_message = f"§e§l{event.player.name}§r 來此共戲"
        self.logger.info(f"{event.player.name} {event.player.xuid} {event.player.device_os}"+ f" at {event.player.location}")
        event.player.send_toast(f"Welcome! §e§l{event.player.name}§r","欢迎回到 §s§lZH-Server§r!")
    
    @event_handler
    def on_player_quit(self, event: PlayerQuitEvent):
        event.quit_message = f"§e§l{event.player.name}§r 去矣"