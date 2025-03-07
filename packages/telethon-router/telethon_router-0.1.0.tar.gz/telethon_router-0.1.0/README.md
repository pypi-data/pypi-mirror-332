# Telethon Router

A library for building Telegram bots using routing similar to web pages. It allows you to organize your bot's logic into handlers and routes, making it easy to manage complex interactions.

### Features

    Routing: Define routes for callback queries, similar to web frameworks.

    Query Parameters: Pass parameters to handlers via callback data.

    Modular Handlers: Organize your bot's logic into reusable handlers.

    Easy Setup: Simple and intuitive API for setting up your bot.

### Example Usage

Below is a simple example of how to use TelegramRouter to create a Telegram bot with routing and query parameters.
Code Example
python
Copy

```python
from telethon import TelegramClient, events, Button
from telethon_router.navigator import Navigator
from telethon_router.types.handler import Handler


###  Initialize the Telegram client
bot = TelegramClient("bot", "YOUR_API_ID", "YOUR_API_HASH")
navigator = Navigator(bot)


# Define a message handler to display buttons
@bot.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event: events.NewMessage.Event):
    buttons = [
        [Button.inline("Say Hi!", b"profile/index")],
        [Button.inline("Friend 1", b"profile/friends?friend_id=1")],
        [Button.inline("Friend 1 Balance", b"profile/friends/balance?friend_id=1")],
    ]

    await event.respond("Choose an option:", buttons=buttons)


# Define a handler for profile-related commands
class Profile(Handler):
    path = "profile"

    async def index(self, event: events.CallbackQuery.Event) -> None:
        await event.answer("Index clicked!", alert=True)

    async def friends(self, event: events.CallbackQuery.Event, **kwargs) -> None:
        friend_id = kwargs.get("friend_id", "Unknown")
        await event.answer(f"Friend clicked! Friend ID: {friend_id}", alert=True)

    async def friends_balance(self, event: events.CallbackQuery.Event, **kwargs) -> None:
        friend_id = kwargs.get("friend_id", "Unknown")
        await event.answer(f"Friend balance clicked! Friend ID: {friend_id}", alert=True)


# Add the Profile handler to the Navigator
navigator.add(Profile())
navigator.setup()


# Start the bot
bot.start(bot_token="YOUR_BOT_TOKEN")
bot.run_until_disconnected()
```

### How It Works
1. Routing

The Navigator class handles routing based on the callback_data of inline buttons. Each route corresponds to a method in a handler.

    Example Routes:

        profile/index: Routes to the index method.

        profile/friends?friend_id=1: Routes to the friends method with friend_id=1.

        profile/friends/balance?friend_id=1: Routes to the friends_balance method with friend_id=1.

2. Query Parameters

Query parameters are passed to the handler methods as keyword arguments (**kwargs). This allows you to dynamically pass data to your handlers.

    Example:

        profile/friends?friend_id=1 passes friend_id=1 to the friends method.

        profile/friends/balance?friend_id=1 passes friend_id=1 to the friends_balance method.

3. Buttons

Buttons are created using Button.inline. The callback_data of each button follows the routing pattern.

    Example Buttons:

        Button.inline("Say Hi!", b"profile/index"): Creates a button that routes to the index method.

        Button.inline("Friend 1", b"profile/friends?friend_id=1"): Creates a button that routes to the friends method with friend_id=1.

4. Handlers

Handlers are classes that define methods to handle specific routes. Each method corresponds to a route and processes the incoming callback.

    Example Methods:

        index: Handles the profile/index route.

        friends: Handles the profile/friends route and accepts friend_id as a parameter.

        friends_balance: Handles the profile/friends/balance route and accepts friend_id as a parameter.

### Example Interaction

    Send /start or hi to the bot:

        The bot responds with a list of buttons:

            Say Hi!: Calls the index method.

            Friend 1: Calls the friends method with friend_id=1.

            Friend 1 Balance: Calls the friends_balance method with friend_id=1.

    Click a button:

        The bot processes the callback and displays the result.

### Requirements

    Python 3.13+

    Telethon

Install the required dependencies using pip:
```bash
pip install telethon
```

### Contribution

Contributions are welcome! Feel free to open issues and PRs.
License

This project is licensed under the MIT License.

### Detailed Explanation
Navigator

The Navigator class is the core of the library. It manages routing for callback queries and sets up event listeners for each handler.

    add(handler): Registers a handler with the navigator.

    setup(): Configures event listeners for all registered handlers.

Handler

Handlers are classes that define methods to handle specific routes. Each handler has a path attribute that defines its base route.

    Example:

        A handler with path = "profile" will handle routes starting with profile/.

Buttons

Buttons are created using Button.inline. The callback_data of each button follows the routing pattern.

    Example:

        Button.inline("Say Hi!", b"profile/index"): Creates a button that routes to the index method.

Query Parameters

Query parameters are passed to the handler methods as keyword arguments (**kwargs). This allows you to dynamically pass data to your handlers.

    Example:

        profile/friends?friend_id=1 passes friend_id=1 to the friends method.
