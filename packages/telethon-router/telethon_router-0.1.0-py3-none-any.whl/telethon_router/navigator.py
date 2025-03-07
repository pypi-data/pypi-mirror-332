import re
from typing import Dict, Callable, List
from urllib.parse import parse_qs
from telethon_router.types.handler import Handler
from telethon import TelegramClient, events


class Navigator:
    """
    A navigation manager for handling Telegram bot events using a collection of handlers.

    This class allows for the registration of handlers and automatically sets up event
    listeners for each handler's methods. It supports query parameters in callback data,
    such as profile/friends/balance?friend_id=1&girlfriend_id=2.
    """

    __handlers: Dict[str, Handler] = {}
    __event_handlers: Dict[str, Callable] = {}

    def __init__(self, bot: TelegramClient):
        """
        Initializes the Navigator with a Telegram client.

        Args:
            bot (TelegramClient): The Telegram client instance.
        """
        self.bot = bot

    def add(self, handler: Handler) -> None:
        """
        Adds a handler to the Navigator.

        Args:
            handler (Handler): The handler to be added.
        """
        self.__handlers[handler.path] = handler

    def setup(self) -> None:
        """
        Sets up the Navigator by configuring event listeners for all registered handlers.
        """
        for path, handler in self.__handlers.items():
            self._register_handler_methods(path, handler)

    def _register_handler_methods(self, path: str, handler: Handler) -> None:
        """
        Registers all valid methods of a handler as event listeners.

        Args:
            path (str): The path associated with the handler.
            handler (Handler): The handler instance containing the methods to register.
        """
        for method_name in self._get_valid_methods(handler):
            self._register_event_listener(path, method_name, getattr(handler, method_name))

    def _get_valid_methods(self, handler: Handler) -> List[str]:
        """
        Retrieves a list of valid method names from a handler.

        Args:
            handler (Handler): The handler instance to inspect.

        Returns:
            List[str]: A list of valid method names.
        """
        return [
            method_name for method_name in dir(handler)
            if callable(getattr(handler, method_name)) and not method_name.startswith("__")
        ]

    def _register_event_listener(self, path: str, method_name: str, method: Callable) -> None:
        """
        Registers a single method as an event listener.

        Args:
            path (str): The path associated with the handler.
            method_name (str): The name of the method to register.
            method (Callable): The method to be registered as an event listener.
        """
        # Use a regex pattern to match the callback data with query parameters
        event_pattern = re.compile(f"^{path}/{method_name.replace("_", "/")}(?:\\?(.*))?$")
        self.__event_handlers[event_pattern.pattern] = method

        @self.bot.on(events.CallbackQuery(pattern=event_pattern))
        async def callback_handler(event: events.CallbackQuery.Event):
            # Extract query parameters from the callback data
            match = event_pattern.match(event.data.decode())
            if match:
                query_string = match.group(1) if match.group(1) else ""
                query_params = parse_qs(query_string)
                # Flatten the query parameters (e.g., {"friend_id": ["1"]} -> {"friend_id": "1"})
                flattened_params = {k: v[0] if isinstance(v, list) and len(v) == 1 else v for k, v in query_params.items()}
                await method(event, **flattened_params)

    def remove_handler(self, path: str) -> None:
        """
        Removes a handler from the Navigator.

        Args:
            path (str): The path of the handler to be removed.
        """
        if path in self.__handlers:
            del self.__handlers[path]
            # Remove all event handlers associated with this path
            for event_pattern in list(self.__event_handlers.keys()):
                if event_pattern.startswith(path):
                    self.bot.remove_event_handler(self.__event_handlers[event_pattern])
                    del self.__event_handlers[event_pattern]

    def clear_handlers(self) -> None:
        """
        Clears all handlers and their associated event listeners.
        """
        for event_pattern in self.__event_handlers:
            self.bot.remove_event_handler(self.__event_handlers[event_pattern])
        self.__handlers.clear()
        self.__event_handlers.clear()