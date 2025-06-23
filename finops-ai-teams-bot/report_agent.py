# placeholder for report generator function

import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-03-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def summarize_with_gpt(resources):
    if not resources:
        return "No underutilized resources found in the current subscription."

    prompt = f"""
    You are a FinOps assistant. Given the following Azure resources identified as underutilized, generate a summary and provide cost-saving recommendations.

    Resources:
    {resources}

    Format the response in markdown. Use bullets and headers where appropriate.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
