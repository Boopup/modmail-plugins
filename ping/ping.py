import discord
from discord.ext import commands, tasks
import aiohttp

class WebsitePinger(commands.Cog):
    def __init__(self, bot, website_url):
        self.bot = bot
        self.website_url = website_url
        self.ping_website.start()

    def cog_unload(self):
        self.ping_website.cancel()

    @tasks.loop(minutes=1)
    async def ping_website(self):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.website_url) as response:
                    if response.status == 200:
            except Exception as e:
                print(f"Failed to ping {self.website_url}: {e}")

def setup(bot):
    website_url = "https://uptime.betterstack.com/api/v1/heartbeat/FWJKzRewAYpdFzFuK186A9pZ"  # Replace with your website URL
    bot.add_cog(WebsitePinger(bot, website_url))
