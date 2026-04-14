import urllib.request
import json
import os

url = "https://api.githubcopilot.com/mcp/"
headers = {
    "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN', '')}",
    "Content-Type": "application/json",
}

data = {"jsonrpc": "2.0", "id": 1, "method": "tools/list"}

req = urllib.request.Request(
    url, data=json.dumps(data).encode("utf-8"), headers=headers, method="POST"
)

try:
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode())
        tools = res_data.get("result", {}).get("tools", [])
        print("Available tools:")
        for t in tools:
            print(f"- {t.get('name')}: {t.get('description')}")
except Exception as e:
    print(f"Error: {e}")
