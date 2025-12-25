[https://apify.com/johnvc/baidu-search-scraper](https://apify.com/johnvc/baidu-search-scraper?fpr=9n7kx3)

# 🚀 Baidu Search Scraper 🇨🇳

> **The most efficient, reliable, and developer-friendly Baidu search scraper**

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- An Apify account and API key

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Apify-Baidu-Search-Scraper
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Using venv (Python 3.3+)
   python -m venv venv
   
   # Activate the virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Install from requirements.txt
   pip install -r requirements.txt

   ```

4. **Configure your API key**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Apify API key
   # Get your API key from: https://apify.com?fpr=9n7kx3
   ```

5. **Run the example**
   ```bash
   python baidu-search-scraper.py
   ```

### Alternative: Direct API Key Usage
If you prefer not to use a `.env` file, you can set the environment variable directly:
```bash
export APIFY_API_TOKEN="your_api_key_here"
python baidu-search-scraper.py
```

> **The most efficient, reliable, and developer-friendly Baidu search scraper for Apify platform**

## 🌟 Why Choose This Scraper?

The Baidu Search data scraper delivers enterprise-grade performance with these advanced capabilities:

**Performance & Reliability**: Built optimized for high-throughput scraping with intelligent rate limiting and pagination handling.

**Cost-Effective**: Provides consistent, reliable results with intelligent pagination management to optimize API usage.

**Lightning-Fast Search & Retrieval**: Search any keyword across Baidu with blazing-fast performance. Retrieve comprehensive results in seconds, not minutes, with intelligent caching and optimization.

**Precision Targeting & Advanced Filtering**: Pinpoint exact search parameters with device targeting, localization support, and time period filtering. Get precisely the search data you need, when you need it.

**Rich, Structured Data Extraction**: Extract complete search information, including organic results, answer boxes, related videos, people also search for, related searches, and top searches. Our advanced parsing ensures you get clean, structured data ready for immediate use.

**Enterprise-Grade Configuration & Flexibility**: Built for developers and businesses who demand reliability. Highly configurable with intuitive controls, comprehensive error handling, and robust logging. Focus on your business logic while we handle the complexity of search scraping.

**No Hidden Costs or Rental Fees**: We do not charge monthly rentals, our scraper operates on a pay-per-use model. Scale up or down based on your actual needs without being locked into expensive subscriptions.

## 🚀 Features

### Core Capabilities
- **Advanced Search**: Support for complex queries with device targeting, localization, and time period filtering
- **Intelligent Pagination**: Automatic handling of Baidu search pagination with configurable limits
- **Device Targeting**: Support for desktop and mobile search results
- **Multi-Language**: Support for international search markets with localization options
- **Time Period Filtering**: Advanced time-based result filtering using Unix timestamps

### Data Quality
- **Clean Output**: Automatic structured data metadata for clean, production-ready data
- **Structured Results**: Consistent JSON structure across all search results
- **Comprehensive Fields**: Organic results, answer boxes, related videos, people also search for, and more
- **Metadata Tracking**: Page-level analytics and search performance metrics
- **Per-Page Billing**: Results are pushed as separate dataset items for accurate billing

## 📖 Usage Examples

### Basic Search Example

Search for "python tutorial" on desktop with default settings.

```json
{
  "query": "python tutorial",
  "device": "desktop"
}
```

### Advanced Search Example

Search for "machine learning" on desktop with Chinese localization, time period filtering, and pagination limits.

```json
{
  "query": "machine learning",
  "device": "desktop",
  "localization": 2,
  "page": 1,
  "num_results": 20,
  "time_period": "stf=1755138395,1755743195|stftype=1",
  "max_pagination": 3
}
```

## 🔍 Input References

#### Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `str` | ✅ | `"python tutorial"` | Search query |
| `device` | `str` | ❌ | `"desktop"` | Device type (`"desktop"` or `"mobile"`) |
| `localization` | `Optional[int]` | ❌ | `None` | Localization code (e.g., `2` for Simplified Chinese) |
| `page` | `int` | ❌ | `1` | Starting page number |
| `num_results` | `int` | ❌ | `10` | Number of results per page |
| `time_period` | `Optional[str]` | ❌ | `None` | Time period filter format (stf=start_timestamp,end_timestamp|stftype=1) Parameter defines the time period for results. (e.g., stf=1755138395,1755743195|stftype=1 only returns results from the past 7 days. First integer within the parameter,1755138395 is Unix Timestamp for 7 days ago. Second integer,1755743195 is Unix Timestamp for now.).|
| `max_pagination` | `Optional[int]` | ❌ | `3` | Maximum pages to fetch (0 = no limit) |
| `output_file` | `Optional[str]` | ❌ | `None` | Custom output filename |

## 📊 Output Format

### Search Result Structure

```json
{
  "query": "machine learning",
  "device": "desktop",
  "localization": 2,
  "page": 1,
  "num_results": 20,
  "filter_results": null,
  "time_period": "stf=1755138395,1755743195|stftype=1",
  "max_pagination": 3,
  "total_results_found": 150,
  "pages_processed": 3,
  "search_metadata": {
    "query": "machine learning",
    "device": "desktop",
    "localization": 2,
    "page": 1,
    "num_results": 20,
    "filter_results": null,
    "time_period": "stf=1755138395,1755743195|stftype=1",
    "max_pagination": 3,
    "pagination_limit_reached": false
  },
  "pagination_info": {
    "total_pages": 3,
    "current_page": 1,
    "max_pagination_set": 3,
    "pagination_stopped_by_limit": false
  },
  "organic_results": [
    {
      "title": "Machine Learning Tutorial",
      "link": "https://example.com/ml-tutorial",
      "snippet": "Learn machine learning fundamentals...",
      "position": 1,
      "displayed_link": "example.com",
      "thumbnail": "https://thumbnail.url",
      "rich_snippet": "Rich snippet content...",
      "sitelinks": [...],
      "related_videos": [...]
    }
  ],
  "answer_box": [...],
  "related_videos": [...],
  "people_also_search_for": [...],
  "related_searches": [...],
  "top_searches": [...],
  "results_by_page": {
    "1": {
      "organic_results": [...],
      "answer_box": [...],
      "related_videos": [...],
      "people_also_search_for": [...],
      "related_searches": [...],
      "top_searches": [...]
    }
  }
}
```

[**Made with ❤️**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your search automation with the most reliable and efficient Baidu search scraper on the market.*
Last Updated: 2025.12.25
