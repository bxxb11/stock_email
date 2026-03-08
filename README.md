# 📈 Stock Email — Daily PLTR & NVDA Briefing

A daily stock briefing emailer for **Palantir (PLTR)** and **NVIDIA (NVDA)**, featuring:

- 📰 Latest news & analyst upgrades/downgrades
- 💬 Reddit community sentiment (r/PLTR, r/wallstreetbets)
- 🎯 Analyst price targets & consensus ratings
- 📊 30-day price charts with MA5/MA20, volume & money flow
- 🌙 Apple-style dark-themed HTML email

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy the example config and fill in your credentials:
   ```bash
   cp config.example.json config.json
   ```
   Edit `config.json` with your Gmail address and [App Password](https://support.google.com/accounts/answer/185833).

3. Generate charts:
   ```bash
   python gen_charts.py
   ```

4. Build the email HTML:
   ```bash
   python build_email.py
   ```

## Scheduling

The email is designed to run daily at 21:00. You can schedule it via cron:
```
0 21 * * * cd /path/to/stock_email && python gen_charts.py && python build_email.py
```

## Email Preview

The generated email includes:
- Dark-themed header with date badge
- PLTR & NVDA news sections with source links
- Reddit community discussion highlights
- Market sentiment grid with analyst consensus targets
- Embedded 30-day price charts (base64 inline images)

## Requirements

- Python 3.8+
- Gmail account with App Password enabled
- Internet access for fetching stock data
