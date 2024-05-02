import json
import os
from llamaapi import LlamaAPI

# Initialize the SDK
llama = LlamaAPI("LL-0LFlDvwphKLp6yZg1MZxiv1OEBzzHK69hgTLBtrZHNTfjHGGQP63uO4UVNSH0Dop")

# API Request JSON Cell
api_request_json = {
  "model": "llama3-70b",
  "messages": [
    {"role": "system", "content": "You are a llama assistant that talks like a llama, starting every word with 'll'."},
    {"role": "user", "content": "Hi, happy llama day!"},
  ]
}

# Make your request and handle the response
response = llama.run(api_request_json)

print(json.dumps(response.json(), indent=2))
