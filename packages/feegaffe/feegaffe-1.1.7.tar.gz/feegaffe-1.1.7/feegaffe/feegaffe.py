import subprocess
import sys

def install_requirements():
    """Installe les requirements nécessaires si non installés."""
    required_packages = ["requests", "discord"]
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installation de '{package}' en cours...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_requirements()

import discord
from discord.ext import commands

class FeegaffeBot:
    def __init__(self, command_prefix: str = "!"):
        self.bot = commands.Bot(command_prefix=command_prefix, intents=discord.Intents.all())
        self.bot.event(self.on_ready)

    async def on_ready(self):
        print(f'Connecté en tant que {self.bot.user}')

    def command(self, *args, **kwargs):
        return self.bot.command(*args, **kwargs)

    def run(self, token: str):
        self.bot.run(token)

# Interface simple pour lancer un bot
def bot(token: str, command_prefix: str = "!"):
    feegaffe = FeegaffeBot(command_prefix)
    return feegaffe