from discord.ext.commands import Cog

from processor.logger.log import Log
from processor.management.object.objects_manager import ObjectsManager


class Listener(Cog):

    def __init__(self):

        self.__bot = ObjectsManager.get_object_by_name("Bot")
        self.__commands_prefix = self.__bot.commands_prefix
