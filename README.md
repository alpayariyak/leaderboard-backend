## Usage

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Edit the `.env` file
```bash
RUNPOD_API_KEY = "" # Your Runpod API key
RUNPOD_OPENAI_BASE_URL = "" # Your Runpod OpenAI base URL
MODEL_NAME="" # The model name
```
This will actually also work for any OpenAI compatible API, e.g. if you deploy openai-compatible vllm server on a pod.
