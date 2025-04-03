import pytest
from fastapi.testclient import TestClient
from stable_diffusion_mcp.main import app, pipe
from modelcontextprotocol.sdk.types import ErrorCode

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()
    assert "model_loaded" in response.json()

@pytest.mark.asyncio
async def test_text_to_image_tool():
    from stable_diffusion_mcp.main import StableDiffusionServer
    server = StableDiffusionServer()
    
    # Test with valid prompt
    result = await server.server.tools["text_to_image"].handler(
        {"prompt": "a cat", "steps": 5}
    )
    assert "image" in result
    assert "format" in result
    
    # Test with invalid input
    with pytest.raises(Exception) as exc_info:
        await server.server.tools["text_to_image"].handler({})
    assert exc_info.value.code == ErrorCode.InvalidParams

def test_model_loading():
    assert pipe is not None
    assert hasattr(pipe, "device")

def test_config():
    from stable_diffusion_mcp.config import get_settings
    settings = get_settings()
    assert settings.model_name == "runwayml/stable-diffusion-v1-5"
    assert settings.device in ["cuda", "cpu", "auto"]
