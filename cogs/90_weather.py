import aiohttp
from datetime import datetime, timedelta
import nextcord
from nextcord import Interaction, SlashOption # Used for UI slashcommands
from nextcord.ext import commands
from config import *
import json

# Specifying a dictionary of Cities
cities = ['Paris', 'London', 'New York']

# Creating a dictionary of dates for the next 5 days
today = datetime.today().date()
next_7_days = {
    'now': today.strftime('%Y-%m-%d'),
    'tomorrow': (today + timedelta(days=1)).strftime('%Y-%m-%d'),
    'in 2 days': (today + timedelta(days=2)).strftime('%Y-%m-%d'),
    'in 3 days': (today+ timedelta(days=3)).strftime('%Y-%m-%d'),
    'in 4 days': (today+ timedelta(days=4)).strftime('%Y-%m-%d'),
    'in 5 days': (today+ timedelta(days=5)).strftime('%Y-%m-%d')
}

# Importing keys
api_key = api_key_weather

class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @nextcord.slash_command(guild_ids=[1101909369911791637])
    async def my_weather(self,
                         interaction: Interaction,
                         my_date: str = SlashOption(name="date", choices=next_7_days.keys()),
                         city: str = SlashOption(name="cities", choices=cities)):
        
        async with aiohttp.ClientSession() as session:
        # A. First test case - User wants weather for today
            
            ##### 1. Passing end point URL
            url = 'https://api.weatherapi.com/v1/forecast.json'
            print(my_date)
            print(next_7_days[my_date])
            
            ##### 2. Specifying Parameters to API
            params = {'key': api_key, 'dt' : next_7_days[my_date],'q': city}
                
            ##### 3. Querry API and Returning data
            async with session.get(url, params=params) as response:
                data = await response.json()  # Parse the JSON response into a Python dictionary
                with open('weather_data.json', 'w') as f:
                    json.dump(data, f)
                    f.close()
                max_temp = data['forecast']['forecastday'][0]['day']['maxtemp_c']
                min_temp = data['forecast']['forecastday'][0]['day']['mintemp_c']
                avg_temp = data['forecast']['forecastday'][0]['day']['avgtemp_c']
                max_wind = data['forecast']['forecastday'][0]['day']['maxwind_kph']
                rain_chance = data['forecast']['forecastday'][0]['day']['daily_chance_of_rain']

        # C. Creating a Discord Embed to pass fields to.
        embed = nextcord.Embed(
            title=f"Weather for the {next_7_days[my_date]} in {city}",
            color=nextcord.Color.green()
            )

        # D. set the fields in the Embed object
        embed.add_field(name="Average Temperature", value=f"{avg_temp}°C", inline=True)
        embed.add_field(name="Max temperature", value=f"{max_temp}°C", inline=True)
        embed.add_field(name="Min temperature", value=f"{min_temp}°C", inline=True)
        embed.add_field(name="Max wind speed", value=f"{max_wind} km/h", inline=True)
        embed.add_field(name="Rain chance", value=f"{rain_chance}%", inline=True)

    # E. send the Embed object as a response
        await interaction.response.send_message(embed=embed)

def setup(client):
    client.add_cog(Weather(client))