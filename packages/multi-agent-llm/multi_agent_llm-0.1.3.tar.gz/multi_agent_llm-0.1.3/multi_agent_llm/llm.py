import os
from typing import Any, Dict, List, Optional, Type

from openai import AsyncOpenAI, OpenAI
from pydantic import BaseModel, Field
from tenacity import retry, stop_after_attempt, wait_exponential


class DefaultResponseSchema(BaseModel):
    content: str = Field(..., description="The generated content")


class LLMBase:
    def __init__(self, model_name: str, **kwargs):
        self.model_name = model_name

    @retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def generate(self, prompt: Any, schema: Optional[Type[BaseModel]] = None) -> Any:
        raise NotImplementedError("Subclasses must implement this method")

    async def generate_async(
        self, prompt: Any, schema: Optional[Type[BaseModel]] = None
    ) -> Any:
        raise NotImplementedError("Subclasses must implement this method")


class OpenAILLM(LLMBase):
    def __init__(
        self,
        model_name: str,
        api_key: str | None = None,
        temperature: float | None = None,
        **kwargs
    ):
        super().__init__(model_name, **kwargs)
        _api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=_api_key, **kwargs)
        self.async_client = AsyncOpenAI(api_key=_api_key, **kwargs)
        self.temperature = temperature

    @retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(6))
    def generate(self, prompt: Any, schema: Optional[Type[BaseModel]] = None) -> Any:
        schema = schema or DefaultResponseSchema
        try:
            completion = self.client.beta.chat.completions.parse(
                model=self.model_name,
                messages=prompt,
                response_format=schema,
                temperature=self.temperature,
            )
            result = completion.choices[0].message.content
            return schema.model_validate_json(result)
        except Exception as e:
            print(f"Error in OpenAI generation: {e}")
            return None

    @retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(6))
    async def generate_async(
        self, prompt: Any, schema: Optional[Type[BaseModel]] = None
    ) -> Any:
        schema = schema or DefaultResponseSchema
        try:
            completion = await self.async_client.beta.chat.completions.parse(
                model=self.model_name,
                messages=prompt,
                response_format=schema,
            )
            result = completion.choices[0].message.content
            return schema.model_validate_json(result)
        except Exception as e:
            print(f"Error in OpenAI async generation: {e}")
            return None

    def format_prompt(
        self, system_prompt: str, user_prompt: str
    ) -> List[Dict[str, str]]:
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
