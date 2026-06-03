<!-- Language toggle -->
[English](README.md) | **中文**

# 🔍 百度 API：干净 JSON 格式的结构化百度搜索结果

> 使用百度 API 最高效、最可靠、对开发者最友好的方式。

**Actor 页面：** [apify.com/johnvc/Baidu-Search-Scraper](https://apify.com/johnvc/Baidu-Search-Scraper?fpr=9n7kx3)
**输入参数说明：** [apify.com/johnvc/Baidu-Search-Scraper/input-schema](https://apify.com/johnvc/Baidu-Search-Scraper/input-schema?fpr=9n7kx3)

百度 API (百度) 可对任意关键词运行百度搜索，并返回干净、结构化的 JSON 数据。每次运行为您提供自然结果（标题、链接、摘要、位置）、知识框、相关视频、"大家还在搜"建议、相关搜索词和热门搜索榜，以及按页元数据和分页详情。支持桌面端、移动端和平板端结果，简体中文和繁体中文本地化，时间范围过滤和多页分页。

## 视频演示

[![观看演示](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## 快速开始

### 前置要求
- Python 3.11 或更高版本
- 一个 Apify 账户和 API 密钥（[在此获取免费密钥](https://apify.com?fpr=9n7kx3)）

1. **克隆代码仓库**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Baidu-Search-Scraper.git
   cd Apify-Baidu-Search-Scraper
   ```

2. **使用 UV 安装依赖**
   ```bash
   # 如果尚未安装 UV，请先安装：
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # 安装项目依赖：
   uv sync
   ```

3. **配置您的 API 密钥**
   ```bash
   cp .env.example .env
   # 编辑 .env 文件并填入您的 Apify API 密钥
   # 在此获取免费 API 密钥：https://apify.com?fpr=9n7kx3
   ```

4. **运行示例**
   ```bash
   uv run python baidu-search-scraper.py
   ```

### 备选方案：直接设置 API 密钥
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python baidu-search-scraper.py
```

## 为什么使用本百度 API？

**完整的搜索结果页覆盖。** 一次调用即可将整个百度结果页作为结构化数据返回：自然结果、知识框、相关视频、"大家还在搜"、相关搜索词和热门搜索榜。您获得的是整页内容，而不仅仅是十条蓝色链接。

**专为中国市场研究打造。** 锁定简体或繁体中文结果，在桌面端、移动端和平板端之间切换，并按精确的日期范围过滤。这使其非常适用于中文市场的 SEO、市场研究和品牌监测。

**可预测的按需付费定价。** 按运行次数加处理页数计费，无月租费。您只需为实际进行的搜索付费，并可通过页数限制直接控制成本。

**干净、一致的 JSON。** 每次响应都采用相同的结构，因此您只需解析一次结果即可在不同查询间复用代码。按页元数据和分页详情让翻阅大型结果集变得轻松。

**易于自动化。** 用几行 Python 代码即可调用，或将其作为 MCP 工具加载，让 Claude、Cursor 等助手按需为您运行百度搜索。

## 功能特性

### 核心功能
- **关键词搜索**：在百度上搜索并提取完整结果页
- **设备定向**：支持桌面端、移动端和平板端结果
- **语言本地化**：支持所有语言、简体中文或繁体中文
- **时间范围过滤**：使用 Unix 时间戳窗口
- **多页分页**：可配置页数限制

### 数据质量
- **结构化自然结果**：含标题、链接、摘要、位置和丰富数据
- **丰富结果模块**：知识框、相关视频、大家还在搜、相关搜索词、热门搜索
- **按页元数据**：含结果数量和分页详情
- **一致的 JSON** 结构，适用于每次查询
- **按页计费**，让大型搜索保持成本透明

## 使用示例

### 基本示例
对单个关键词进行单页桌面端搜索。这是试用本 API 最经济的方式。
```json
{
  "query": "机器学习",
  "device": "desktop",
  "max_pagination": 1
}
```

### 高级示例
多字段搜索，启用简体中文本地化、增加每页结果数并使用日期范围过滤。
```json
{
  "query": "人工智能",
  "device": "desktop",
  "localization": 2,
  "page": 1,
  "num_results": 20,
  "time_period": "stf=1748994000,1749600000|stftype=1",
  "max_pagination": 3
}
```

## 输入参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `query` | `string` | 是 | - | 在百度上要查找的搜索词。 |
| `device` | `string` | 否 | `desktop` | 模拟的设备：`desktop`(桌面) / `mobile`(手机) / `tablet`(平板)。 |
| `localization` | `integer` | 否 | `1` | 语言过滤：`1` = 所有语言, `2` = 简体中文, `3` = 繁体中文。 |
| `page` | `integer` | 否 | `1` | 结果的起始页码。 |
| `num_results` | `integer` | 否 | `10` | 每页获取的结果数（最多50条）。 |
| `time_period` | `string` | 否 | (无) | 使用 Unix 时间戳的日期范围过滤，格式 `stf=起始时间戳,结束时间戳\|stftype=1`。留空则返回所有日期。 |
| `max_pagination` | `integer` | 否 | `3` | 最大获取页数（`0` = 不限制）。 |
| `output_file` | `string` | 否 | (无) | 可选的保存结果文件名；省略时自动生成。 |

## 输出格式

以下是查询 `机器学习` 的代表性响应。为便于阅读，此处精简了部分相关数组；它们以与 `organic_results` 相同的单项结构返回。

```json
{
  "query": "机器学习",
  "device": "desktop",
  "localization": 2,
  "page": 1,
  "num_results": 10,
  "filter_results": null,
  "time_period": null,
  "max_pagination": 3,
  "total_results_found": 29,
  "pages_processed": 3,
  "search_metadata": {
    "device": "desktop",
    "localization": 2,
    "filter_results": null,
    "time_period": null,
    "max_pagination": 3,
    "pagination_limit_reached": true
  },
  "pagination_info": {
    "total_pages": 3,
    "current_page": 1,
    "max_pagination_set": 3,
    "pagination_stopped_by_limit": true
  },
  "organic_results": [
    {
      "position": 2,
      "title": "机器学习 - 百度百科",
      "link": "https://baike.baidu.com/item/机器学习/217599",
      "displayed_brand": "百度百科",
      "snippet": "机器学习是一门多领域交叉学科，涉及概率论、统计学、逼近论、凸分析、算法复杂度理论等多门学科。"
    },
    {
      "position": 6,
      "title": "MACHINE LEARNING Definition & Meaning - Merriam-Webster",
      "link": "https://www.merriam-webster.com/dictionary/machine%20learning",
      "snippet": "machine learning noun: a computational method that is a subfield of artificial intelligence and that enables a computer to learn to perform tasks by analyzing a large dataset."
    }
  ],
  "answer_box": [],
  "related_videos": [],
  "people_also_search_for": [],
  "related_searches": [],
  "top_searches": []
}
```

字段说明：
- `query` - 搜索词
- `device` - 设备类型
- `localization` - 语言本地化代码
- `total_results_found` - 找到的结果总数
- `pages_processed` - 已处理的页数
- `search_metadata` - 搜索元数据
- `pagination_info` - 分页信息
- `organic_results` - 自然搜索结果（含位置 position、标题 title、链接 link、品牌 displayed_brand、摘要 snippet）
- `answer_box` - 知识框
- `related_videos` - 相关视频
- `people_also_search_for` - 大家还在搜
- `related_searches` - 相关搜索词
- `top_searches` - 热门搜索

---

## 作为 MCP 工具使用

您可以将百度 API 作为 MCP 工具加载，让助手为您调用它。以下 MCP 服务器 URL 仅预加载这一个 Actor：

```
https://mcp.apify.com/?tools=actors,docs,johnvc/Baidu-Search-Scraper
```

在出现提示时通过浏览器 OAuth 认证，或使用您的 Apify API 令牌（与 Python 示例中使用的 `APIFY_API_TOKEN` 相同）认证。在 https://console.apify.com/settings/integrations 获取令牌，在 https://apify.com?fpr=9n7kx3 注册免费 Apify 账户。

## 在 Claude Cowork 桌面版中安装

![在 Claude Cowork 桌面版中安装](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork 是桌面应用的自动化模式。要将百度 API 作为工具提供给它，请将 Apify MCP 服务器添加为连接器。

1. 打开 Claude 桌面应用，进入 **Settings → Connectors**（或 **Settings → Developer → Edit Config** 直接编辑 `claude_desktop_config.json`）。
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. 添加 Apify MCP 服务器，仅预加载此 Actor：

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/Baidu-Search-Scraper"
      ]
    }
  }
}
```

3. 重启应用。当 Cowork 首次调用工具时，在浏览器中完成 OAuth 提示，或在连接器设置中添加您的 Apify API 令牌以跳过 OAuth。
4. 在 Cowork 聊天中，确认工具可用并请它运行百度 API。

下载桌面应用并开始免费试用：https://claude.ai/referral/uIlpa7nPLg
更多帮助：https://docs.apify.com/platform/integrations/claude-desktop

## 在 Claude Code 中安装

![在 Claude Code 中安装](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code 是命令行工具。用一条命令即可添加该 Actor 的 MCP 服务器：

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/Baidu-Search-Scraper"
```

如需使用令牌而非浏览器 OAuth：

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/Baidu-Search-Scraper" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

然后用 `claude mcp list` 验证，或在会话中运行 `/mcp`。请 Claude Code 调用百度 API。

免费试用 Claude Code：https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP 文档：https://code.claude.com/docs/en/mcp

## 在 Claude 网页版中安装

![在 Claude 网页版中安装](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

在 claude.ai 上，您将 Apify 添加为连接器，然后仅启用此 Actor 的工具。

1. 进入 **Settings → Connectors → Browse connectors**，搜索 **Apify MCP server**。安装它（如有提示则启用或更新）。
2. 连接时，使用您的 Apify API 令牌认证，并启用工具 `johnvc/Baidu-Search-Scraper`。
3. 在任意聊天中，打开 **+ → Connectors** 并开启 **Apify**。
4. 或者，选择 **Add custom connector** 并粘贴完整 MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/Baidu-Search-Scraper`，在出现提示时使用 OAuth。
5. 请 Claude 运行百度 API。

在网页上打开 Claude：https://claude.ai

## 在 Cursor 中安装

![在 Cursor 中安装](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor 从项目文件 `.cursor/mcp.json` 读取 MCP 服务器。

1. 在您的项目中，创建 `.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/Baidu-Search-Scraper"
    }
  }
}
```

2. 如果您倾向于令牌认证而非浏览器 OAuth，请添加请求头：

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/Baidu-Search-Scraper",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. 打开 **Cursor → Settings → MCP** 并确认 **apify** 服务器已连接（绿点）。
4. 在 Composer 或 Chat 中，请 Cursor 调用百度 API。

初次使用 Cursor？在此获取：https://cursor.com/referral?code=XQP4VBLI3NNX

## 在 ChatGPT 中安装

![在 ChatGPT 中安装](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT 通过开发者模式连接到 Apify MCP 服务器（适用于 ChatGPT Pro、Plus、Business、Enterprise 和 Education 套餐）。

1. 点击您的头像图标，进入 **Settings > Apps**。如果看不到 **Create app** 按钮，请打开 **Advanced settings** 并启用 **Developer mode**。
2. 点击 **Create app** 并填写表单：
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/Baidu-Search-Scraper`
   - **Authentication:** OAuth
3. 点击 **Create** 并授权与 Apify 的连接。
4. 要在对话中使用该应用，请点击聊天中的 **+**，选择 **Developer mode**，然后选择 **Apify**。

更多帮助：https://docs.apify.com/platform/integrations/mcp

---

[**用心打造**](https://apify.com/johnvc?fpr=9n7kx3)

*使用百度 API，以可靠、结构化的结果驱动您的搜索和 SEO 工作流程。*

最后更新：2026.06.03
