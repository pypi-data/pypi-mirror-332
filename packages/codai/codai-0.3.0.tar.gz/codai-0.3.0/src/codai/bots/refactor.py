from pydantic import BaseModel, Field
from pydantic_ai.agent import AgentRunResult

from codai.bot import Bot

model = "openai:o3-mini"

system = """
You are an expert refactoring bot.
""".strip()


class RefactorResult(BaseModel):
    """Refactor result."""

    new_content: str = Field(
        ..., title="New content", description="Refactored content."
    )
    explanation: str = Field(
        ..., title="Explanation", description="Explanation of the refactoring."
    )


class RefactorBot(Bot):
    def __call__(self, text: str, message_history: list = None) -> AgentRunResult:
        message_history = message_history or self.get_messages(bot_id=self.id)

        res = self.agent.run_sync(text, message_history=message_history)

        self.append_message(
            bot_id=self.id,
            data=res.new_messages_json(),
        )

        return res


bot = Bot(model=model, system_prompt=system, result_type=RefactorResult)
