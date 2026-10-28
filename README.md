# discord-python

Kleine Python-Skripte für Discord: DM-Statistik („wer hat mehr geschrieben?“) und ein Zahlen-Ratespiel.

![Vorschau](discord-python.png)

> [!WARNING]
> Die Skripte laufen mit deinem **eigenen Benutzer-Token** („Self-Bot“). Das verstößt gegen die
> Nutzungsbedingungen von Discord und kann zur Sperre des Kontos führen. Nutzung auf eigene Gefahr.
> Der Token gibt vollen Zugriff auf dein Konto: **nie teilen, nie committen.**

## Skripte

| Datei | Was es macht |
|---|---|
| `dm_statistik.py` | Zählt die Nachrichten in DMs mit einer oder mehreren Personen: gesamt, von dir, von der anderen Person. Optional ab einem Datum |
| `guessnumber-in-dc.py` | Ratespiel: `$guess` in einen Chat schreiben, dann innerhalb von 5 Sekunden eine Zahl von 1–10 raten |
| `token_laden.py` | Hilfsfunktion: liest den Token aus `DISCORD_TOKEN` oder `.env` |

## Einrichten

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt        # discord.py-self (normales discord.py kann keine Self-Bots)
cp .env.example .env                   # Token eintragen
```

## Benutzen

```bash
# alle Nachrichten mit zwei Personen
python dm_statistik.py 123456789012345678 987654321098765432

# nur seit Jahresbeginn
python dm_statistik.py --seit 2025-01-01 123456789012345678

# Ratespiel starten (läuft, bis du Strg+C drückst)
python guessnumber-in-dc.py
```

Beispielausgabe:

```
Eingeloggt als slxt

Max (ID 123456789012345678) – seit 2025-01-01
  Du:     1204
  Er/Sie: 1391
  Gesamt: 2595
```

User-IDs bekommst du in Discord mit *Einstellungen → Erweitert → Entwicklermodus* und dann
Rechtsklick auf eine Person → *ID kopieren*.

## Änderungen (Oktober 2026)

- Der Token steht nicht mehr im Code, sondern kommt aus `DISCORD_TOKEN` oder `.env` (in `.gitignore`).
- `discord-main.py`, `discord-msg-count.py` und `discord-msg-count-each.py` sind in `dm_statistik.py`
  zusammengeführt. Statt IDs im Code anzupassen, gibst du sie beim Aufruf mit.
- Fehler behoben: `discord-msg-count-each.py` gab feste Zahlen aus statt der gezählten.
- Ratespiel: Antworten zählen nur noch aus demselben Chat.
