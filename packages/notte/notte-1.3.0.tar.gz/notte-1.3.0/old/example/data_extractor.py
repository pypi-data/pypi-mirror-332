from typing import Any, Literal, final

import chevron
import datetime as dt
from notte.common.conversation import Conversation
from notte.llms.engine import LLMEngine
from pydantic import BaseModel

class DataExtractorOutput(BaseModel):
    success: bool
    error: str | None = None
    data: dict[str, Any] | list[dict[str, Any]] | None = None

system_rules = """
You are extracting content on behalf of a user.
If a user asks you to extract a 'list' of information, or 'all' information,
YOU MUST EXTRACT ALL OF THE INFORMATION THAT THE USER REQUESTS.

Always prioritize using the provided content to answer the question.
Do not miss any important information.
Do not make up an answer.
Do not hallucinate.
In case you can't find the information and the string is required, instead of 'N/A' or 'Not speficied', return an empty string: '', if it's not a string and you can't find the information, return null.
Be concise and follow the schema always if provided.
If the document provided is not relevant to the prompt nor to the final user schema, return null.

Generate a JSON output that extracts ONLY the relevant information from the following user request:
{{prompt}}

Additional rules:
- The JSON schema has to be simple. No crazy properties.
- Don't create too many properties, just the ones that are needed.
- Don't invent properties.
- Return a valid JSON response object with properties that would capture the information requested in the prompt.

Example of a valid JSON response for a user request related to hotels search:
```json
{{success_example}}
```

Example of an valid output if you cannot answer the user request:
```json
{{failure_example}}
```
In case of a failure, be very explicit in the error message about what is missing or what is wrong.

Today is: {{timestamp}}

Transform the following document into structured JSON output based on the provided user request:

```markdown
{{document}}
```

Your turn:
"""

@final
class DataExtractor:
    def __init__(self, llm: LLMEngine):
        self.llm: LLMEngine = llm
        self.conv: Conversation = Conversation()
        
    def success_example(self) -> DataExtractorOutput:
        return DataExtractorOutput(
            success=True,
            data={
                "hotels": [
                    {
                        "city": "Edinburg",
                        "price": 100,
                        "currency": "USD",
                        "availability": "2024-12-28",
                        "return_date": "2024-12-30",
                        "link": "https://www.example.com/edinburg-hotel-1"
                    },
                    {
                        "city": "Edinburg",
                        "price": 120,
                        "currency": "USD",
                        "availability": "2024-12-28",
                        "return_date": "2024-12-30",
                        "link": "https://www.example.com/edinburg-hotel-2"
                    }
                ]
            }
        )
        
    def failure_example(self) -> DataExtractorOutput:
        return DataExtractorOutput(
            success=False,
            error="The user requested information about a cat but the document is about a dog",
            data=None
        )

    def extract(
        self,
        prompt: str,
        document: str
    ) -> DataExtractorOutput:
        """Validate the output of the last action is what the user wanted"""
        self.conv.reset()
        system_prompt = chevron.render(system_rules, data={
            "prompt": prompt,
            "document": document,
            "success_example": self.success_example().model_dump_json(),
            "failure_example": self.failure_example().model_dump_json(),
            "timestamp": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }, warn=True)
        self.conv.add_system_message(content=system_prompt)

        return self.llm.structured_completion(self.conv.messages(), response_format=DataExtractorOutput)
