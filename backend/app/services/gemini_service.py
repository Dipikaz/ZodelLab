from google import genai
from google.genai import types
import os
import re

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = """
You are a Senior Computational Physicist and Python Engineer. 
Your goal is to solve engineering/scientific problems by writing clean Python code.

RULES:
1. Use numpy, scipy, and pandas for calculations.
2. The code MUST print a final JSON object to stdout.
3. The JSON format must be: {"data": [{"x": [], "y": [], "type": "scatter"}], "layout": {"title": "Simulation Result"}}
4. Output ONLY the python code block. No explanations.
"""

def generate_simulation_code(user_prompt: str):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.1 # Keep it deterministic for science
        ),
        contents=user_prompt
    )
    
    # Extract code between ```python and ```
    code_match = re.search(r"```python\n(.*?)\n
```", response.text, re.DOTALL)
    return code_match.group(1) if code_match else response.text