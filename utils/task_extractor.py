import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_tasks(email_text):
    prompt = f"""
Extract all actionable tasks from the email below. For each task, return:
- task: what needs to be done
- due: deadline if mentioned
- priority: low, medium, or high (based on urgency or keywords)

Respond only with a JSON list.

Email:
\"\"\"
{email_text}
\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500
        )

        raw = response.choices[0].message.content.strip()

        # Clean potential formatting
        if raw.startswith("```json"):
            raw = raw.removeprefix("```json").removesuffix("```").strip()

        # Attempt to parse JSON
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            # Try extracting just the array portion
            start = raw.find("[")
            end = raw.rfind("]")
            if start != -1 and end != -1:
                return json.loads(raw[start:end+1])
            return []

    except Exception as e:
        print("OpenAI error:", e)
        return []
