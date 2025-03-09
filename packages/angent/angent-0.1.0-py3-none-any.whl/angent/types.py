from typing import Any


class BaseAgent:
    @property
    def name(self) -> str:
        raise NotImplementedError("Agent class must have a name")

    @property
    def description(self) -> str:
        raise NotImplementedError("Agent class must have a description")

    async def handle(self, instruction: str, global_ctx: dict) -> Any:
        raise NotImplementedError("Agent class must have a handle method")
