"""Discord-Token aus der Umgebung oder einer Datei .env lesen – nie im Code speichern."""
import os
import sys
from pathlib import Path


def token_laden() -> str:
    token = os.environ.get("DISCORD_TOKEN", "").strip()
    env = Path(__file__).with_name(".env")
    if not token and env.exists():
        for zeile in env.read_text(encoding="utf-8").splitlines():
            key, _, wert = zeile.partition("=")
            if key.strip() == "DISCORD_TOKEN":
                token = wert.strip().strip("\"'")
    if not token:
        sys.exit("Kein Token: DISCORD_TOKEN als Umgebungsvariable setzen oder in .env eintragen (siehe README).")
    return token
