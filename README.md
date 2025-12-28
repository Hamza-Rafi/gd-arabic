# gd-arabic

Arabic Lemma lookup script for [GoldenDict-NG](https://github.com/xiaoyifang/goldendict-ng). Tokenises Arabic text and provides ckickable links to look up the lemma (dictionary form) of each word.

## Prerequisites

Install build deps (required by CAMeL Tools)

```bash
paru -S cmake boost
```

## Installation

```bash
git clone https://git.hamzarafi.com/Hamza-Rafi/gd-arabic.git
cd gd-arabic
```

Make the client script executable:

```bash
chmod +x ./gd_arabic_client.py
```

## GoldenDict-NG Setup

1. Open **Edit -> Dictionaries** (F3)
2. Go to **Programs** tab
3. Click **Add** and configure:
   - **Enabled**: ✓
   - **Type**: html
   - **Name**: gd-arabic
   - **Command Line**: `/home/path/to/gd_arabic_client.py %GDWORD% %GDSEARCH%`

## Usage

Ensure the server is running beforehand:

```
ln -s /home/path/to/gd-arabic/gd-arabic-server.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable gd-arabic-server.service
systemctl --user start gd-arabic-server.service
```

The script accepts two args:

```bash
./gd_arabic_client.py <word> [sentence]
```

- `word` - the word to highlight
- `sentence` - the sentence to display

GoldenDict-NG passes these automatically via `%GDWORD%` and `%GDSEARCH%`.
