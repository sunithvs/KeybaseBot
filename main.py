
import asyncio
import logging
import os
import sys

import pykeybasebot.types.chat1 as chat1
from dotenv import load_dotenv
from pykeybasebot import Bot, KbEvent

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

if "win32" in sys.platform:
    # Windows specific event-loop policy
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()  # type: ignore
    )


class Handler:
    async def __call__(self, bot: Bot, event: KbEvent):
        if event.msg.sender.username == bot.username:
            exit(0)
        if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
            return
        if not event.msg.content.text.body.split(" ")[0].startswith("!"):
            print(f'{event.msg.content.text.body.split(" ")[0] = }')
            return

        channel = event.msg.channel
        msg_id = event.msg.id
        await bot.chat.react(channel, msg_id, "hi welcome to ooty nice to meet you")


listen_options = {
    "local": True,
    "wallet": True,
    "dev": True,
    "hide-exploding": False,
    "convs": True,
    "filter_channel": None,
    "filter_channels": {"name": "spaceupbot,sunithvs"}
}

bot_client = Bot(username=os.environ.get('BOT_NAME'), paperkey=os.environ.get('BOT_TOKEN'), handler=Handler())

asyncio.run(bot_client.start(listen_options))
