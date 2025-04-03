<div align="center">

# 🌈✨ Stable Diffusion MCP Server

**The Open-Source Bridge to Your Local AI Image Generator**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Open Source](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://opensource.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red.svg)](https://github.com/Aladin147)

<img src="https://raw.githubusercontent.com/CompVis/stable-diffusion/main/assets/stable-diffusion-v1/samples/txt2img/merged-0006.png" alt="Stable Diffusion Example" width="400"/>

</div>

A friendly, open-source MCP server that connects to your local Stable Diffusion installation.  
Free to use, modify, and share under the MIT license.

## 📋 Table of Contents

- [Features](#-features)
- [How It Works](#-how-it-works)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Examples](#-examples)
- [Requirements](#-requirements)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Features

- 🖼️ **Text-to-image generation** - Create stunning images from text prompts
- 🔄 **Image-to-image transformation** - Transform existing images with text guidance
- 🤖 **Model management** - Use different Stable Diffusion models
- ⚡ **Performance optimization** - Automatic GPU/CPU detection
- 🔧 **Customizable parameters** - Control steps, guidance scale, and more
- 🔌 **Seamless integration** - Works directly with Cline through MCP

## 🔍 How It Works

The Stable Diffusion MCP server acts as a bridge between Cline and your local Stable Diffusion installation:

```
┌─────────┐    ┌─────────────────┐    ┌───────────────────┐
│  Cline  │◄───┤ SD MCP Server   │◄───┤ Stable Diffusion  │
│         │    │ (This Project)  │    │ (Local Install)   │
└─────────┘    └─────────────────┘    └───────────────────┘
    ▲                  ▲                       ▲
    │                  │                       │
    └──────────────────┴───────────────────────┘
           Seamless Integration Flow
```

When you send a prompt from Cline, the MCP server:
1. Processes your request
2. Calls your local Stable Diffusion installation
3. Returns the generated image back to Cline

## 🏃‍♂️ Quick Start

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
    "PYTHONPATH": ".",
    "SD_MCP_MODEL_NAME": "runwayml/stable-diffusion-v1-5"
  },
  "disabled": false,
  "autoApprove": []
}
```
2. Restart Cline to connect

## ⚙️ Configuration

The server can be configured using environment variables:

| Environment Variable | Description | Default |
|----------------------|-------------|---------|
| `SD_MCP_MODEL_NAME` | Stable Diffusion model to use | `runwayml/stable-diffusion-v1-5` |
| `SD_MCP_DEVICE` | Device to run on (`cuda`, `cpu`, or `auto`) | `auto` |
| `SD_MCP_SAFETY_CHECKER` | Enable safety checker | `true` |
| `SD_MCP_NUM_INFERENCE_STEPS` | Number of denoising steps | `50` |
| `SD_MCP_GUIDANCE_SCALE` | How closely to follow the prompt | `7.5` |
| `SD_MCP_MAX_BATCH_SIZE` | Maximum batch size | `4` |

## 📝 Examples

### Basic Text-to-Image

```python
# In Cline
result = await use_mcp_tool(
  server_name="stable_diffusion",
  tool_name="text_to_image",
  arguments={
    "prompt": "A beautiful sunset over mountains, photorealistic"
  }
)
```

### Advanced Options

```python
# In Cline
result = await use_mcp_tool(
  server_name="stable_diffusion",
  tool_name="text_to_image",
  arguments={
    "prompt": "A futuristic city with flying cars, cyberpunk style",
    "steps": 75,
    "guidance_scale": 9.0
  }
)
```

## 📋 Requirements

- Python 3.8+
- Stable Diffusion installed locally
- MCP client (Cline)
- PyTorch
- 8GB+ RAM (16GB+ recommended)
- GPU with 4GB+ VRAM for optimal performance (CPU mode available)

## 🔧 Troubleshooting

### Common Issues

**Issue**: Server fails to start  
**Solution**: Ensure Python 3.8+ is installed and all dependencies are correctly installed

**Issue**: CUDA out of memory error  
**Solution**: Reduce batch size or use a smaller model

**Issue**: Model not found  
**Solution**: Check your internet connection or specify a different model

**Issue**: Slow generation on CPU  
**Solution**: This is expected. For faster generation, use a CUDA-compatible GPU

## 👥 Contributing

We welcome contributions! Please see our [Contribution Guidelines](CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  
Made with ❤️ by [Aladin147](https://github.com/Aladin147)

If you find this project useful, please consider giving it a ⭐

</div>
