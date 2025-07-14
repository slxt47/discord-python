from discord.ext import commands
import discord
from datetime import datetime, timezone

token = "NDgzMzUzMTQ0OTMyMTcxNzc2.GEwjmZ.FYgmD_O6FJqq80wK4gG9p0EsgYUrpqOKFi3WiU"

target_user_ids = [
    268743080092499968,
    559606751335284748,
    299404314017923075,
    850668669453467659,
    705855310652375052
]

start_date = datetime(2025, 1, 1, tzinfo=timezone.utc)

bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.event
async def on_ready():
    print(f"Eingeloggt als {bot.user}\n")

    for target_user_id in target_user_ids:
        mine = 0
        theirs = 0
        total = 0
        user = None

        for channel in bot.private_channels:
            if isinstance(channel, discord.DMChannel) and channel.recipient.id == target_user_id:
                user = channel.recipient
                async for msg in channel.history(limit=None, oldest_first=True):
                    if msg.created_at < start_date:
                        continue

                    total += 1
                    if msg.author.id == bot.user.id:
                        mine += 1
                    else:
                        theirs += 1

        if user:
            display_name = user.global_name if user.global_name else f"{user.name}#{user.discriminator}"
            print(f"User-ID: {user.id}")
            print(f"Name   : {display_name}")
            print(f"--- Nachrichten seit {start_date.date()} ---")
            print(f"Du: {mine}")
            print(f"Er/Sie: {theirs}")
            print(f"Gesamt: {total}\n")
        else:
            print(f"⚠️ Kein DM-Channel gefunden für User-ID {target_user_id}\n")

    await bot.close()

bot.run(token)
