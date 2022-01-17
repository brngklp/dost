# Discord Bot For automation of Currency Info.
# Author: Baran Gokalp
# Github: https://github.com/brngklp
# API used: Coinbase API
# API url: https://api.coinbase.com/v2/prices
# Date: 01/17/2022_10:24 PM

import hikari
import lightbulb
from libs.fetch import currencies

def main() -> None:
    
    """
    This is the part that you need to customize for your server. Just create a discord bot
    from the Discord Developer Portal, Give the bot required permissions and copy the bot's token
    and paste it here, changing the token variable's inside to your token. If you are a developer that
    wants to improve this project, you can uncomment the default_enabled_guilds variable and paste your
    server's Id to speed up things, like adding new commands to the bot.
    """

    bot = lightbulb.BotApp(
        token='your_token',
        # default_enabled_guilds=(serverId)
    )
    
    """
    Bot will print the text below when It's executed.
    """

    @bot.listen(hikari.StartedEvent)
    async def on_start(event) -> None:
        print("It's great to be alive again.")

    """
    This part is for the dollar command. It shows the usd to try currency.
    It may not be helpful for you but surely It's helpful for me and some others.
    """

    @bot.command
    @lightbulb.command('dollar', 'Shows the current usd to try currency')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def dolar(ctx: lightbulb.Context) -> None:
        await ctx.respond(currencies("usd", "try"))

    """
    This part of the bot is for the command 'dost'. What dost command does is It takes two arguments.
    First one is base and the second one is currency. It'll try to convert the base to the currency that's
    selected.
    """

    @bot.command
    @lightbulb.option('base', 'Base Currency', type=str)
    @lightbulb.option('currency', 'Target Currency', type=str)
    @lightbulb.command('dost', 'Choose from bases and currencies')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def currency(ctx: lightbulb.Context) -> None:
        await ctx.respond(currencies(str(ctx.options.base), str(ctx.options.currency)))

    """
    Error Handling Part. The coinbase api has a weird problem with returning the values of the currencies that tries to
    use 'usd' as currency and any other currency unit as the base currency. So I writed a error handling part for this
    special weird error. When this error occures hikari lightbulb returns the error named 'CommandInvocationError'.
    So We're catching that error and printing why that error occurred.
    """

    @bot.listen(lightbulb.CommandErrorEvent)
    async def on_error(event: lightbulb.CommandErrorEvent) -> None:
        if isinstance(event.exception, lightbulb.CommandInvocationError):
            await event.context.respond(
            f"""
            An error occurred during execution. It may be because the Coinbase API is not returning any results.
            The command that caused the error `{event.context.command.name}`. You can try to change the currency from usd
            and entering the base as usd
            """)
            raise event.exception

    """
    This part is the help part. To see the help message, you need to enter the command 'help'
    and It'll print the help message. If you're not quite familiar with python, all uppercase 
    variables means that the variable defined is constant.    
    """

    HELP_MESSAGE = """
    (still under development, commands may work differently in future versions)
    Commands available:
        `help`- Prints the help message.
        `dollar` - Prints out the usd to try currency.
        `dost` - Gives you the choice to select the currency and the base.
    Thank you for using dost!
    """

    @bot.command
    @lightbulb.command('help', 'prints out the help message')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def help(ctx: lightbulb.Context) -> None:
        await ctx.respond(HELP_MESSAGE)

    bot.run()

if __name__ == '__main__':
    main()