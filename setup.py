from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="stable-diffusion-mcp",
    version="0.1.0",
    author="Aladin147",
    description="MCP server for local Stable Diffusion generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aladin147/stable-diffusion-mcp",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn>=0.21.0",
        "torch>=2.0.0",
        "diffusers>=0.15.0",
        "transformers>=4.28.0",
        "@modelcontextprotocol/sdk>=0.5.0",
        "python-multipart>=0.0.6",
        "pydantic>=1.10.0"
    ],
    entry_points={
        "console_scripts": [
            "stable-diffusion-mcp=stable_diffusion_mcp.main:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
