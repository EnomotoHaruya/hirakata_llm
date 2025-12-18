import json
import os
import hirakata_bot.config as config

all_data = []

for file in [config.JSON_TO_JSONL_FILE, config.JSON_XLSX_DATASET_FILE]:
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                all_data.append(json.loads(line))

with open(config.JSON_MERGED_DATASET_FILE, "w", encoding="utf-8") as f:
    for item in all_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Merged {len(all_data)} items into {config.JSON_MERGED_DATASET_FILE}")