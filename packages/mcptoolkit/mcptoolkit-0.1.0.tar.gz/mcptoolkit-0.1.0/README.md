# MCP Unified Server

A modular server implementation for Claude AI assistants with a variety of integrated tools, enabling Claude to perform actions and access external resources.

## Overview

The MCP Unified Server provides a unified interface for Claude to interact with various external systems and tools including:

- **File system operations**: Read, write, and manipulate files
- **Time tools**: Get current time in different timezones, convert between timezones
- **Sequential thinking**: A tool for dynamic and reflective problem-solving
- **Brave Search**: Web and local search capabilities
- **Browserbase**: Browser automation for web interactions
- **World Bank API**: Access to economic and development data
- **News API**: Access to global news sources and articles
- **PowerPoint**: Create and manipulate PowerPoint presentations
- **Excel**: Create and manipulate Excel spreadsheets

## Architecture

The server is built with a modular architecture:

```
mcp_unified_server/
├── mcp_unified_server.py     # Main server implementation
├── .env                      # Environment variables 
└── tools/                    # Tool modules
    ├── __init__.py           # Package initialization
    ├── brave_search.py       # Brave Search API integration
    ├── browserbase.py        # Browserbase browser automation
    ├── filesystem.py         # File system operations
    ├── news_api.py           # News API integration
    ├── ppt.py                # PowerPoint tools
    ├── sequential_thinking.py # Sequential thinking tools
    ├── time_tools.py         # Time-related tools
    ├── worldbank.py          # World Bank API integration
    └── xlsxwriter.py         # Excel spreadsheet creation
```

Each tool module follows a consistent pattern:
- External MCP reference
- Service class implementation
- Tool function definitions
- Registration functions

## Installation

### Prerequisites

- Python 3.9+
- Required Python packages (automatically installed with pip)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/mcp_unified_server.git
   cd mcp_unified_server
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables by creating a `.env` file (see Configuration section)

5. Run the server:
   ```bash
   python mcp_unified_server.py
   ```

## Configuration

The server can be configured using environment variables. Create a `.env` file in the project root with the following variables:

```env
# MCP Server Configuration
MCP_HOST=0.0.0.0
MCP_PORT=8000
MCP_LOG_LEVEL=info  # debug, info, warning, error

# Tool API Keys
BRAVE_API_KEY=your_brave_api_key
BROWSERBASE_API_KEY=your_browserbase_api_key
BROWSERBASE_PROJECT_ID=your_browserbase_project_id
NEWS_API_KEY=your_news_api_key

# File System Configuration
MCP_FILESYSTEM_DIRS=~/documents,~/downloads  # Comma-separated list of allowed directories
```

### API Keys

To use all features of the MCP Unified Server, you'll need to obtain API keys for the following services:

- **Brave Search API**: Get an API key from [Brave Search API](https://brave.com/search/api/)
- **Browserbase**: Sign up at [Browserbase](https://browserbase.com) to get API key and project ID
- **News API**: Get an API key from [News API](https://newsapi.org)

## Available Tools

### File System Tools

- `read_file`: Read contents of a file
- `read_multiple_files`: Read multiple files simultaneously
- `write_file`: Create or overwrite a file
- `edit_file`: Make line-based edits to a file
- `create_directory`: Create a new directory
- `list_directory`: Get directory contents
- `directory_tree`: Get a recursive tree view
- `move_file`: Move or rename files/directories
- `search_files`: Search for files matching a pattern
- `get_file_info`: Get file metadata
- `list_allowed_directories`: List allowed directories

### Time Tools

- `get_current_time`: Get current time in a specified timezone
- `convert_time`: Convert time between timezones

### Sequential Thinking

- `sequentialthinking`: A tool for breaking down complex problems using a step-by-step thinking process

### Brave Search

- `brave_web_search`: Perform web searches
- `brave_local_search`: Search for local businesses and places

### Browserbase

- `browserbase_create_session`: Create a new browser session
- `browserbase_close_session`: Close a browser session
- `browserbase_navigate`: Navigate to a URL
- `browserbase_screenshot`: Take a screenshot
- `browserbase_click`: Click an element
- `browserbase_fill`: Fill a form field
- `browserbase_evaluate`: Execute JavaScript
- `browserbase_get_content`: Extract page content

### World Bank API

- `worldbank_get_indicator`: Get indicator data for a country

### News API

- `news_top_headlines`: Get top news headlines
- `news_search`: Search for news articles
- `news_sources`: List available news sources

### PowerPoint Tools

- `ppt_create_presentation`: Create a new PowerPoint presentation
- `ppt_open_presentation`: Open an existing presentation
- `ppt_save_presentation`: Save a presentation
- `ppt_add_slide`: Add a new slide
- `ppt_add_text`: Add text to a slide
- `ppt_add_image`: Add an image to a slide
- `ppt_add_chart`: Add a chart to a slide
- `ppt_add_table`: Add a table to a slide
- `ppt_analyze_presentation`: Analyze presentation structure
- `ppt_enhance_presentation`: Suggest enhancements
- `ppt_generate_presentation`: Generate a presentation from text
- `ppt_command`: Process natural language commands

### XlsxWriter Tools

- `xlsx_create_workbook`: Create a new Excel workbook
- `xlsx_add_worksheet`: Add a worksheet to a workbook
- `xlsx_write_data`: Write data to a cell
- `xlsx_write_matrix`: Write a matrix of data
- `xlsx_add_format`: Create a cell format
- `xlsx_add_chart`: Add a chart to a worksheet
- `xlsx_add_image`: Add an image to a worksheet
- `xlsx_add_formula`: Add a formula to a cell
- `xlsx_add_table`: Add a table to a worksheet
- `xlsx_close_workbook`: Close and save the workbook

## Usage Examples

### Example 1: Using File Operations with Time Tools

```python
from mcp.client import MCPClient

# Connect to the MCP server
client = MCPClient("http://localhost:8000")

# Use file operations
client.call_tool("write_file", {"path": "~/data/timestamp.txt", "content": "File created at:"})

# Get current time
time_result = client.call_tool("get_current_time", {"timezone": "America/New_York"})

# Append time to file
client.call_tool("edit_file", {
    "path": "~/data/timestamp.txt", 
    "edits": [{"oldText": "File created at:", "newText": f"File created at: {time_result}"}]
})
```

### Example 2: News Search and Analysis

```python
from mcp.client import MCPClient

# Connect to the MCP server
client = MCPClient("http://localhost:8000")

# Search for news about a topic
news_results = client.call_tool("news_search", {"q": "artificial intelligence", "page_size": 10})

# Create a directory for results
client.call_tool("create_directory", {"path": "~/news_analysis"})

# Save results to a file
client.call_tool("write_file", {"path": "~/news_analysis/ai_news.txt", "content": news_results})
```

### Example 3: Creating an Excel Report

```python
from mcp.client import MCPClient

# Connect to the MCP server
client = MCPClient("http://localhost:8000")

# Create a new Excel workbook
client.call_tool("xlsx_create_workbook", {"filename": "sales_report.xlsx"})

# Add a worksheet
client.call_tool("xlsx_add_worksheet", {"filename": "sales_report.xlsx", "name": "Sales"})

# Add a bold format for headers
client.call_tool("xlsx_add_format", {
    "filename": "sales_report.xlsx",
    "format_name": "header_format",
    "properties": {"bold": True, "bg_color": "#DDDDDD"}
})

# Write headers
headers = ["Quarter", "Revenue", "Expenses", "Profit"]
for i, header in enumerate(headers):
    client.call_tool("xlsx_write_data", {
        "filename": "sales_report.xlsx",
        "worksheet": "Sales",
        "row": 0,
        "col": i,
        "data": header,
        "format": "header_format"
    })

# Write data
data = [
    ["Q1", 100000, 80000, 20000],
    ["Q2", 110000, 85000, 25000],
    ["Q3", 115000, 90000, 25000],
    ["Q4", 130000, 95000, 35000]
]

client.call_tool("xlsx_write_matrix", {
    "filename": "sales_report.xlsx",
    "worksheet": "Sales",
    "start_row": 1,
    "start_col": 0,
    "data": data
})

# Close and save the workbook
client.call_tool("xlsx_close_workbook", {"filename": "sales_report.xlsx"})
```

## Development

### Adding a New Tool Module

1. Create a new file in the `tools` directory (e.g., `my_tool.py`)
2. Follow the existing module pattern:
   - Create service class
   - Define tool functions
   - Implement registration functions
3. Update `mcp_unified_server.py` to import and register your new module

### Extending an Existing Tool Module

1. Add new methods to the service class
2. Add new tool functions
3. Update the registration function to include your new tools

## Troubleshooting

- **Module not loading**: Check the import path and dependencies
- **API key errors**: Verify your API keys in the `.env` file
- **Permission errors**: Check the allowed directories in `MCP_FILESYSTEM_DIRS`
- **Connection errors**: Ensure the server is running and the port is accessible

## License

The MCP Unified Server is licensed under the MIT License.

### MIT License

Copyright (c) 2025 MCP Unified Server Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Third-Party Libraries

This project incorporates several third-party libraries, each with their own licenses:

- **XlsxWriter**: BSD License
- **python-pptx**: MIT License
- **NLTK**: Apache License 2.0
- **pandas**: BSD 3-Clause License
- **httpx**: BSD License
- **Pillow**: HPND License
- **requests**: Apache License 2.0
- **newsapi-python**: MIT License
- **python-dotenv**: BSD 3-Clause License

Please refer to the licenses of each library for more details.

## Acknowledgements

This project uses several open-source libraries and APIs:
- MCP SDK for Claude AI assistants
- NewsAPI for news access
- Brave Search API for web search
- World Bank API for economic data
- python-pptx for PowerPoint manipulation
- XlsxWriter for Excel spreadsheets
# MCP Tools Configuration System

This system provides an easy way to enable and disable tools in the MCP Unified Server through a web-based user interface. The configuration system consists of three main components:

1. **Configuration UI**: A Streamlit web application for easy tool management
2. **Configuration Loader**: A Python module to load configuration settings
3. **MCP Unified Server Integration**: Modified server that respects configuration settings

## Quick Start

1. Install requirements:
   ```bash
   pip install streamlit pyyaml python-dotenv
   ```

2. Start both the server and configuration UI:
   ```bash
   python launcher.py
   ```

3. Or start them separately:
   ```bash
   # Start just the server
   python launcher.py --server-only
   
   # Start just the configuration UI
   python launcher.py --ui-only
   ```

4. Access the Configuration UI in your web browser at http://localhost:8501

## Configuration System Overview

### Configuration File Structure

The system uses a YAML-based configuration file (`config.yaml`) with the following structure:

```yaml
enabled_tools:
  filesystem: true
  time_tools: true
  sequential_thinking: true
  brave_search: true
  # ... other tools here

tool_config:
  brave_search:
    rate_limit: 100
    max_results: 10
  filesystem:
    allowed_directories:
      - "~/documents"
      - "~/downloads"
    allow_file_deletion: false
  # ... other tool-specific configurations
```

### Configuration UI Features

The Streamlit-based configuration UI provides the following features:

- **Enable/Disable Tools**: Easily toggle tools on or off
- **Tool Configuration**: Configure specific settings for each tool
- **Environment Variables**: View and edit environment variables
- **Server Control**: Start, stop, and restart the MCP server
- **Advanced Settings**: Edit raw configuration YAML

### Files in this System

- `mcp_unified_server.py`: Main MCP server with configuration integration
- `config_loader.py`: Module for loading and parsing configuration
- `config_ui.py`: Streamlit web application for configuration management
- `launcher.py`: Helper script to start both server and UI
- `config.yaml`: Configuration file (created automatically if not present)

## Extending the Configuration System

### Adding a New Tool

1. Create your tool module in the `tools` directory
2. Make sure it follows the standard MCP tool module pattern:
   - Has a `set_external_mcp()` function
   - Has a `get_<toolname>_tools()` function that returns a dictionary of tools
   - Optionally has an `initialize()` function
3. Add the tool name to the `AVAILABLE_TOOLS` list in `mcp_unified_server.py`
4. Restart the server and it will be available in the configuration UI

### Adding Tool-Specific Configuration Options

For each tool, you can add custom configuration options:

1. Update the UI in `config_ui.py` to include form fields for the tool's settings
2. Access the configuration in your tool using the `get_tool_config()` function

## Troubleshooting

- **UI can't connect to server**: Make sure the server is running and check the ports
- **Tool not appearing in UI**: Ensure it's in the `AVAILABLE_TOOLS` list and follows the module pattern
- **Configuration changes not taking effect**: Make sure to save changes and restart the server

## Security Considerations

- The configuration UI doesn't include authentication by default
- Consider adding authentication or only running it on localhost
- Be careful with environment variables containing sensitive credentials
