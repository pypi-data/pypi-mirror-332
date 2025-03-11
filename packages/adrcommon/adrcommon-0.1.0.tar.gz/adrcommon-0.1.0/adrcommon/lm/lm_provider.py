import dspy
from openai import Client, AsyncClient

from .inference import get_endpoint
from adrcommon.secrets.provider import SecretProvider

OPENAI = 'openai'


class LmProvider:
    def __init__(self, secrets: SecretProvider):
        self._secrets = secrets

    def get_lm(self, model_name: str, provider: str = None, temperature = 0.1, max_tokens = 4000):
        provider = provider or OPENAI
        
        params = {
            'model': f'{OPENAI}/{model_name}',
            'temperature': temperature,
            'max_tokens': max_tokens,
        }
        
        if provider == OPENAI:
            return dspy.LM(
                api_key=self._secrets.get_api_key(OPENAI),
                **params
            )
        else:
            api_endpoint, api_key = get_endpoint(self._secrets, provider)
            return dspy.LM(
                api_key=api_key,
                api_base=api_endpoint,
                **params
            )
    
    def get_client(self):
        return Client(api_key=self._secrets.get_api_key(OPENAI), max_retries=10)
    
    def get_async_client(self):
        return AsyncClient(api_key=self._secrets.get_api_key(OPENAI), max_retries=10)
