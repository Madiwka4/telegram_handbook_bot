# Telegram Handbook Bot

This is a small test project that uses the Telegram Bot API and Google's Gemini API to create a bot that can answer questions about a PDF handbook.

## Installation

1. Clone this repository.
2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

Determining workspace structure

Deciding which workspace information to collect

Gathering workspace info

Sure, here's a basic README for your project:

```markdown
# Telegram Handbook Bot

This is a small test project that uses the Telegram Bot API and Google's Gemini API to create a bot that can answer questions about a PDF handbook.

## Installation

1. Clone this repository.
2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

## Usage

1. Set your Telegram API token and Gemini API key in a `.env` file:

```env
TELEGRAM_API_TOKEN=your_telegram_api_token
GEMINI_API_KEY=your_gemini_api_key
```

2. Run the bot:

```sh
python main.py
```

3. Send a message to the bot on Telegram. The bot will respond with information from the PDF handbook.

## Files

- `main.py`: The main script that runs the bot.
- `pdf_parser.py`: Contains functions for parsing the PDF handbook.
- `utils.py`: Contains utility functions.