from bot.bot import Bot
from processor.bot.listener import Listener
from processor.logger.log import Log
from processor.management.object.objects_manager import ObjectsManager


class MainClass:

    def __init__(self):
        self.__bot = ObjectsManager.create_object(Bot)
        self.__listener = ObjectsManager.create_object(Listener)
        self.__bot.add_cog(self.__listener)

    def run(self):
        Log.debug("running the application!")

        try:
            self.__bot.run("OTI3NTMxNjkzMDkzNTYwMzMw.YdLlNA.4chF-w9-WaoVj_DRIy6Bqq5MUKA")

        except RuntimeError:
            Log.info("Exiting the application...!")

        ObjectsManager.delete_object("Listener")
        ObjectsManager.delete_object("Bot")

        Log.debug("application closed!")
