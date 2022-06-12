from discord.ext.commands import Cog, command

from processor.logger.log import Log
from processor.management.commands.basic.basic_commands import BasicCommands
from processor.management.object.objects_manager import ObjectsManager


class Listener(Cog):

    def __init__(self):

        self.__bot = ObjectsManager.get_object_by_name("Bot")
        self.__commands_prefix = self.__bot.commands_prefix

    @command()
    async def say(self, ctx, *args):
        message = " ".join(args)
        Log.debug(f"User typed '{self.__commands_prefix}say {message}'")
        await BasicCommands.say(ctx, message)
