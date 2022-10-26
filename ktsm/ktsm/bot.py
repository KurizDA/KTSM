from twitchio.ext import commands
from . import load_model
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ktsm.settings")
import django
django.setup()
from .models import LiveChatData

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token='oauth:drkzkg8ximotjz1ec20xgaxbcab3ba', prefix='?', initial_channels=['#nokduro'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return

        msg, emt = load_model.live_chat(message.content)
        LiveChatData(
            user_id = 
        ).save()
        await self.handle_commands(message)
