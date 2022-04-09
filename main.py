import click
import discord
import discord.client
from configparser import ConfigParser

genchannel = None

class GenBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        for guild in self.guilds:
            print(guild)
        await self.broadcast("hello")

    async def on_message(self, message):
        print('Message from {0} {0.author}: {0.content}'.format(message))

    async def on_guild_join(self, guild):
        print(f'join guild {guild}')


    async def on_guild_remove(self, guild):
        print(f'leave guild {guild}')

    async def broadcast(self, message):
        for guild in self.guilds:
            for channel in guild.text_channels:
                if channel.name == genchannel:
                    await channel.send(message)

@click.command()
@click.argument("config", type=click.File("r"))
def genbot(config):
    """
    general discord bot
    """
    global genchannel

    parser = ConfigParser()
    parser.read_file(config)
    genchannel = parser["MAIN"]["broadcastchannel"]
    bot = GenBot()
    bot.run(parser["MAIN"]["token"])


if __name__ == '__main__':
    genbot()
