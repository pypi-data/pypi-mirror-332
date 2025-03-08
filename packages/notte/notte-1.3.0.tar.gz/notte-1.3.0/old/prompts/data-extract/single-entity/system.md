{{system_prompt}}

Always prioritize using the provided content to answer the question.
Do not make up an answer.
Do not hallucinate.
In case you can't find the information and the string is required, instead of 'N/A' or 'Not speficied', return an empty string: '', if it's not a string and you can't find the information, return null.
Be concise and follow the schema always if provided.
Here are the urls the user provided of which he wants to extract information from:

{{urls}}

Here is the schema you should follow:
```json
{{schema}}
```
The schema is optional. But, if it is provided, strictly follow it.
