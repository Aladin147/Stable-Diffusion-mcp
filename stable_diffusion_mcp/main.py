#!/usr/bin/env python3
import logging
from fastapi import FastAPI, HTTPException
from modelcontextprotocol.sdk.server import Server
from modelcontextprotocol.sdk.server.stdio import StdioServerTransport
from modelcontextprotocol.sdk.types import ErrorCode, McpError
import torch
from diffusers import StableDiffusionPipeline
from .config import get_settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Stable Diffusion MCP Server")
settings = get_settings()

# Initialize Stable Diffusion pipeline
pipe = None

@app.on_event("startup")
async def load_model():
    global pipe
    try:
        device = settings.device
        if device == "auto":
            device = "cuda" if torch.cuda.is_available() else "cpu"
        
        logger.info(f"Loading model {settings.model_name} on {device}")
        pipe = StableDiffusionPipeline.from_pretrained(
            settings.model_name,
            safety_checker=None if not settings.safety_checker else None
        )
        pipe = pipe.to(device)
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        raise

@app.get("/health")
async def health_check():
    return {
        "status": "healthy" if pipe else "unhealthy",
        "model_loaded": pipe is not None,
        "device": str(pipe.device) if pipe else None
    }

class StableDiffusionServer:
    def __init__(self):
        self.server = Server(
            {"name": "stable-diffusion-mcp", "version": "0.1.0"},
            {"capabilities": {"resources": {}, "tools": {}}}
        )
        self.setup_tools()

    def setup_tools(self):
        @self.server.tool(
            name="text_to_image",
            description="Generate image from text prompt",
            input_schema={
                "type": "object",
                "properties": {
                    "prompt": {"type": "string"},
                    "steps": {"type": "number", "default": settings.num_inference_steps},
                    "guidance_scale": {"type": "number", "default": settings.guidance_scale}
                },
                "required": ["prompt"]
            }
        )
        async def text_to_image(prompt: str, steps: int = None, guidance_scale: float = None):
            try:
                if not pipe:
                    raise McpError(ErrorCode.InternalError, "Model not loaded")
                
                steps = steps or settings.num_inference_steps
                guidance_scale = guidance_scale or settings.guidance_scale
                
                logger.info(f"Generating image for prompt: {prompt}")
                image = pipe(prompt, num_inference_steps=steps, guidance_scale=guidance_scale).images[0]
                return {"image": image.tobytes(), "format": "PNG"}
            except Exception as e:
                logger.error(f"Generation failed: {str(e)}")
                raise McpError(ErrorCode.InternalError, str(e))

    async def run(self):
        transport = StdioServerTransport()
        await self.server.connect(transport)

if __name__ == "__main__":
    import uvicorn
    server = StableDiffusionServer()
    uvicorn.run(app, host="0.0.0.0", port=8000)
