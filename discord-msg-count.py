from discord.ext import commands
import discord

token = "YOUR DC TOKEN"
target_user_id =  User_id

bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.event
async def on_ready():
    print(f"Eingeloggt als {bot.user}")

    total = 0
    for channel in bot.private_channels:
        if isinstance(channel, discord.DMChannel) and channel.recipient.id == target_user_id:
            async for msg in channel.history(limit=None):
                total += 1

    print(f"Gesamte Nachrichten im Chat mit {target_user_id}: {total}")
    await bot.close()


bot.run(token)
