"""
Baidu API: A Quick Start Example | 百度 API：快速入门示例
See more at: https://apify.com/johnvc/Baidu-Search-Scraper?fpr=9n7kx3
Input schema: https://apify.com/johnvc/Baidu-Search-Scraper/input-schema?fpr=9n7kx3

This script shows how to call the Baidu API on Apify from Python and read its
structured JSON output. It exercises several input parameters so you can see what
is configurable, while keeping the run small so your first call stays cheap.

本脚本演示如何从 Python 调用 Apify 上的百度 API 并读取其结构化 JSON 输出。
它使用了多个输入参数，让您了解可配置的内容，同时保持运行规模较小，
使您的首次调用保持低成本。

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
在此获取免费 Apify API 密钥：https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
# 使用您的 API 令牌初始化 Apify 客户端（从 .env 文件读取）
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one query, max_pagination=1) to keep this first run
# inexpensive. Raise these once you have your own API key and know your budget.
#
# 构建 Actor 输入。
# 输入保持较小规模（单个查询，max_pagination=1）以使首次运行成本低廉。
# 在您拥有自己的 API 密钥并了解预算后，可适当增大这些值。

# --- English example: an English-language query ---
# --- 英文示例：英文查询词 ---
run_input = {
    "query": "machine learning",   # the only required field | 唯一必填字段
    "device": "desktop",            # desktop, mobile, or tablet | 桌面、手机或平板
    "localization": 1,              # 1 = all languages, 2 = Simplified Chinese, 3 = Traditional Chinese | 1=所有语言, 2=简体中文, 3=繁体中文
    "num_results": 10,              # results per page (max 50) | 每页结果数（最多50条）
    "max_pagination": 1,            # pages to fetch; kept at 1 to keep the run cheap | 获取页数；保持为1以降低成本
    # "time_period": "stf=1748994000,1749600000|stftype=1",  # optional date-range filter | 可选的日期范围过滤
}

# --- Chinese example: a Chinese-language query with Simplified Chinese localization ---
# --- 中文示例：中文查询词，启用简体中文本地化 ---
# To run the Chinese example instead, replace `run_input` above with `run_input_zh` below.
# 要改用中文示例，请将上面的 `run_input` 替换为下面的 `run_input_zh`。
run_input_zh = {
    "query": "机器学习",            # Chinese query: "machine learning" | 中文查询词："机器学习"
    "device": "desktop",            # desktop, mobile, or tablet | 桌面、手机或平板
    "localization": 2,              # 2 = Simplified Chinese results | 2=简体中文结果
    "num_results": 10,              # results per page (max 50) | 每页结果数（最多50条）
    "max_pagination": 1,            # pages to fetch | 获取页数
}

# Run the Actor and wait for it to finish
# 运行 Actor 并等待其完成
run = client.actor("johnvc/Baidu-Search-Scraper").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")  # Actor 运行未返回结果。

# Read structured results from the run's default dataset
# 从运行的默认数据集读取结构化结果
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} item(s).\n")  # 返回了若干条结果

# Show a few key fields from each page of results.
# 显示每页结果中的几个关键字段。
for item in items:
    print(
        f"Query: {item.get('query')}  |  "
        f"Pages: {item.get('pages_processed')}  |  "
        f"Results found: {item.get('total_results_found')}"
    )
    for result in (item.get("organic_results") or [])[:5]:
        print(f"  {result.get('position')}. {result.get('title')}")
        print(f"     {result.get('link')}")
    print()
