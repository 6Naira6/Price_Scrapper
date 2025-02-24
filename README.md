# Price Scraper

## Overview

**Price Scraper** is a Python-based web scraping tool designed to automatically extract and monitor product prices from popular e-commerce websites, allowing easy price comparison and market analysis.

## Features

- **Multi-platform Scraping:** Supports scraping prices from Amazon, Digikala, and Torob.
- **Automated Web Scraping:** Efficiently extracts and aggregates pricing data.
- **Data Merging and Analysis:** Combines data from different sources to facilitate comprehensive price comparisons.

## Repository Contents

- `Amazon Scraper/`: Contains scripts specific to Amazon price extraction.
- `Digikala Scraper/`: Tools to scrape product pricing from Digikala.
- `Torob Scraper/`: Dedicated scripts for scraping pricing from Torob.
- `Digi-Torob Merger/`: Scripts for merging data from Digikala and Torob for comparison.
- `Show_Case/`: Demonstrations and usage examples of the scrapers.
- `chromedriver/`: Includes ChromeDriver required for browser automation with Selenium.

## Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/6Naira6/Price_Scrapper.git
cd Price_Scrapper
```

2. **Set Up the Python Environment:**

- Install dependencies:

```bash
pip install -r requirements.txt
```

*(Make sure `requirements.txt` lists packages such as `requests`, `beautifulsoup4`, and `selenium`.)*

3. **ChromeDriver Setup:**

- Download ChromeDriver compatible with your Google Chrome version from [ChromeDriver Official](https://sites.google.com/a/chromium.org/chromedriver/).
- Place the downloaded `chromedriver` executable in the `chromedriver/` directory or add it to your system's PATH.

## Usage

### Amazon Scraper

- Navigate and run:

```bash
cd "Amazon Scraper"
python amazon_scraper.py
```

### Digikala Scraper

- Navigate and run:

```bash
cd "Digikala Scraper"
python digikala_scraper.py
```

### Torob Scraper

- Navigate and run:

```bash
cd "Torob Scraper"
python torob_scraper.py
```

### Digi-Torob Merger

- Merge and analyze data:

```bash
cd "Digi-Torob Merger"
python merger.py
```

*(Replace script names with actual filenames if they differ.)*

## Example Workflow

1. Scrape data individually from Amazon, Digikala, and Torob.
2. Use `Digi-Torob Merger` to combine and analyze scraped data.
3. Utilize the merged data for informed price comparison and decision-making.


