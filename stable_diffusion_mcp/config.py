from typing import Literal
from pydantic import BaseSettings

class Settings(BaseSettings):
    model_name: str = "runwayml/stable-diffusion-v1-5"
    device: Literal["cuda", "cpu", "auto"] = "auto"
    safety_checker: bool = True
    num_inference_steps: int = 50
    guidance_scale: float = 7.5
    max_batch_size: int = 4

    class Config:
        env_prefix = "SD_MCP_"
        case_sensitive = False

def get_settings():
    return Settings()
