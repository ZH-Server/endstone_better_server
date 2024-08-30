import endstone

from endstone import ColorFormat
from endstone.event import event_handler, EventPriority, PlayerJoinEvent, PlayerQuitEvent, ServerListPingEvent
from endstone.plugin import Plugin

class PLayerListener:
    def __init__(self, plugin: Plugin):
        self._plugin = plugin

    @event_handler(priority=EventPriority.HIGHEST)
    def on_server_list_ping(self, event: ServerListPingEvent):
        event.motd = ColorFormat.BOLD + ColorFormat.AQUA + "Welcome to ZH-Server!"

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        player = event.player
        self._plugin.logger.info(
            ColorFormat.YELLOW + f"{player.name}[/{player.address}] joined the game with UUID {player.unique_id}"
        )

    @event_handler
    def on_player_quit(self, event: PlayerQuitEvent):
        player = event.player
        self._plugin.logger.info(ColorFormat.YELLOW + f"{player.name}[/{player.address}] left the game.")
