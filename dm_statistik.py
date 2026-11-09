"""Zählt die Nachrichten in deinen Discord-Direktnachrichten – gesamt und wer wie viel geschrieben hat.

Aufruf:
    export DISCORD_TOKEN=...            # oder in eine Datei .env schreiben (siehe README)
    python dm_statistik.py 123456789012345678 987654321098765432
    python dm_statistik.py --seit 2025-01-01 123456789012345678

Ersetzt discord-main.py, discord-msg-count.py und discord-msg-count-each.py.
"""
import argparse
import sys
from datetime import datetime, timezone

import discord
from discord.ext import commands

from token_laden import token_laden


def argumente():
    p = argparse.ArgumentParser(description="Nachrichten in Discord-DMs zählen")
    p.add_argument("user_ids", nargs="+", type=int, help="Discord-User-IDs der Chat-Partner")
    p.add_argument("--seit", type=lambda s: datetime.fromisoformat(s).replace(tzinfo=timezone.utc),
                   default=datetime(2000, 1, 1, tzinfo=timezone.utc),
                   help="nur Nachrichten ab diesem Datum zählen (JJJJ-MM-TT)")
    return p.parse_args()


def main():
    args = argumente()
    bot = commands.Bot(command_prefix="!", self_bot=True)

    @bot.event
    async def on_ready():
        print(f"Eingeloggt als {bot.user}\n")
        dms = {c.recipient.id: c for c in bot.private_channels if isinstance(c, discord.DMChannel)}

        for uid in args.user_ids:
            channel = dms.get(uid)
            if channel is None:
                print(f"⚠️  Kein DM-Chat mit User-ID {uid} gefunden\n")
                continue

            meine = deine = 0
            async for msg in channel.history(limit=None, after=args.seit, oldest_first=True):
                if msg.author.id == bot.user.id:
                    meine += 1
                else:
                    deine += 1

            user = channel.recipient
            name = user.global_name or user.name
            print(f"{name} (ID {user.id}) – seit {args.seit.date()}")
            print(f"  Du:     {meine}")
            print(f"  Er/Sie: {deine}")
            print(f"  Gesamt: {meine + deine}\n")

        await bot.close()

    bot.run(token_laden())


if __name__ == "__main__":
    sys.exit(main())
