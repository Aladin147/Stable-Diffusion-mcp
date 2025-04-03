remove # Stable Diffusion MCP Server 🌈✨  
**Open-Source** bridge to your local AI image generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Open Source](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://opensource.org/)

A friendly, open-source MCP server that connects to your local Stable Diffusion installation.  
Free to use, modify, and share under the MIT license.

## Features
- 🖼️ Text-to-image generation
- 🔄 Image-to-image transformation
- 🤖 Model management
- ⚡ Performance monitoring

## Quick Start

### PowerShell (Windows)
```powershell
pip install -r requirements.txt
pip install -e .
Start-Process -NoNewWindow python -ArgumentList "-m stable_diffusion_mcp"
```

### Bash (Linux/Mac)
```bash
pip install -r requirements.txt
pip install -e .
python -m stable_diffusion_mcp
```

### MCP Integration
1. Add to cline_mcp_settings.json:
```json
"stable_diffusion": {
  "command": "python",
  "args": ["-m", "stable_diffusion_mcp"],
  "env": {
    "PYTHONPATH": "."
  }
}
```
2. Restart Cline to connect

## Requirements
- Python 3.8+
- Stable Diffusion installed locally
- MCP client

## Contributing
We welcome contributions! Please see our [Contribution Guidelines](CONTRIBUTING.md).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
