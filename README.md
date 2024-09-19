# StockPriceBot
A Telegram bot to fetch real-time stock prices using `pyTelegramBotAPI` and `BeautifulSoup`.
![Python](https://img.shields.io/badge/Python-3.9-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![StockPriceBot in action](path/to/your/demo.gif)
![Bot Screenshot](path/to/your/screenshot.png)
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/StockPriceBot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd StockPriceBot
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   Create a `.env` file with your Telegram API key and stock API details.
   ```
   TELEGRAM_API_KEY=your_api_key
   STOCK_API_KEY=your_stock_api_key
   ```
## Usage
1. Start the bot:
   ```bash
   python bot.py
   ```

2. In Telegram, type `/price BAJAJHFL` to fetch the stock price of Bajaj Housing Finance.
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
