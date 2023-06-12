import nextcord
from nextcord import Interaction, SlashOption # Used for UI slashcommands
from nextcord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, client):
        self.count = 0
        self.client = client

    @nextcord.slash_command(guild_ids=[1101909369911791637])
    async def slash_command_cog(self, interaction: nextcord.Interaction):
        """This is a slash command in a cog"""
        await interaction.response.send_message("Hello I am a slash command in a cog!")

def setup(client):
    client.add_cog(ExampleCog(client))