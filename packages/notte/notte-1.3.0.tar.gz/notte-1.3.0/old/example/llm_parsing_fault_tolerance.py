



from notte.llms.engine import LLMEngine
from notte_agents.falco.prompt import SimplePrompt

prompt_example = """

Step 1: Analyze the current page and identify the model's last update date
...

## Step 2: Scroll down the page to find the model's last update date
...

## Step 3: Check if the model's last update date is within March 2023
...

The final answer is: $\boxed{
{
  "state": {
    "page_summary": "On the page is a model card for phobert-base-vi-sentiment-analysis",
    "previous_goal_eval": "Success - The model card is loaded",
    "memory": "Model card for phobert-base-vi-sentiment-analysis loaded, need to find last update date",
    "next_goal": "Find the model's last update date"
  },
  "actions": [
    {
      "scroll_down": {"amount": null}
    }
  ]
}
}$

"""


fault_tolerance_prompt = """
You are an expert in parsing and formatting LLM responses.

You are given a response from an LLM, which failed to be parsed correctly in JSON format.

Your task is to understand whether you can still extract the information needed in the response.
Or if a completely new generation attempt is needed.

You will be given a prompt example of how to parse the response, and a response from an LLM.

You need to parse the response and format it in a way that is easy to understand.

This is the format that we expect to be able to correctly parse the response (notte the '```json' and '```' tags which are CRUTIAL):
```json
{{example_format}}
```

This is the response from the LLM:
```json
{{response}}
```

Now, either return a new generation attempt, or the parsed response.


"""

class LLMParsingFaultTolerance:
    def __init__(self, llm: LLMEngine, prompt: SimplePrompt):
        self.llm: LLMEngine = llm
        self.prompt: SimplePrompt = prompt

    def parse(self, response: str) -> str:
        return response

