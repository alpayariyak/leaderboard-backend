from providers.abstract_providers.openai_provider import OpenaiProvider
import os
from typing import Callable
from dotenv import load_dotenv

load_dotenv()


class RunPod(OpenaiProvider):
    NAME = "RunPod"
    API_KEY = os.environ["RUNPOD_API_KEY"]
    OPENAI_BASE_URL = os.environ["RUNPOD_OPENAI_BASE_URL"]
    SUPPORTED_MODELS = {
        "mistral-7b-instruct": os.environ["MODEL_NAME"],
    }

