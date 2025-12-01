from pathlib import Path
import json
from langfuse import Langfuse

langfuse = Langfuse()
dataset = langfuse.create_dataset(
    name="strands-ai-mcp-agent-evaluation",
    description="Evaluation dataset for MCP agent testing"
)

items = json.loads(Path("dataset.json").read_text())

for item in items:
    langfuse.create_dataset_item(
        dataset_name="strands-ai-mcp-agent-evaluation",
        input=item["input"],
        expected_output=item["expected_output"]
    )

print(f"✅ Successfully created dataset 'strands-ai-mcp-agent-evaluation' with {len(items)} items")
