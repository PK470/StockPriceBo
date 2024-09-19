# StockPriceBot
A Telegram bot to fetch real-time stock prices using `pyTelegramBotAPI` and `BeautifulSoup`.
![Python](https://img.shields.io/badge/Python-3.9-blue)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/StockPriceBot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd price
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   Create a `.env` file with your Telegram API key and stock API details.
   ```
   BOT_TOKEN = your_bot_token
   ```
## Usage
1. Start the bot:
   ```bash
   python bot.py
   ```

2. In Telegram, type `/price BAJAJHFL` to fetch the stock price of Bajaj Housing Finance.
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
