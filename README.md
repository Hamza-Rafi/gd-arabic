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
uv tool install . --python 3.10
```

## GoldenDict-NG Setup

1. Open **Edit -> Dictionaries** (F3)
2. Go to **Programs** tab
3. Click **Add** and configure:
   - **Enabled**: ✓
   - **Type**: html
   - **Name**: gd-arabic
   - **Command Line**: `gd-arabic %GDWORD% %GDSEARCH%`

> **Troubleshooting:** If you get a `Query error: exit code 255`, GoldenDict-NG can't find the command. Use the full path instead:
>
> ```
> /home/$USER/.local/bin/gd-arabic %GDWORD% %GDSEARCH%
> ```

## Usage

The script accepts two args:

```bash
gd-arabic <word> [sentence]
```

- `word` - the word to highlight
- `sentence` - the sentence to display

GoldenDict-NG passes these automatically via `%GDWORD%` and `%GDSEARCH%`.
