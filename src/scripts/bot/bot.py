from discord.ext.commands import Bot as SuperBot, Cog, CommandNotFound

from processor.logger.log import Log


class Bot(SuperBot):

    def __init__(self):

        self.__commands_prefix = "K$"
        super().__init__(self.__commands_prefix)

    @property
    def commands_prefix(self):
        return self.__commands_prefix

    @Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, CommandNotFound):
            await ctx.send("This is not a known command!")
            Log.error("Command Not Found!")
            return

        Log.critical(f"Error happened!{error}")
