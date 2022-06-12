class BasicCommands:

    def __init__(self):
        raise NotImplementedError("Cannot Instantiate BasicCommands!")

    @staticmethod
    async def say(ctx, message):
        await ctx.send(f"The bot says {message}")
