import glob 
import json
from pathlib import Path

DATA_CACHE_DIR = Path("data")
DATA_CACHE_DIR.mkdir(exist_ok=True)
data_dir = DATA_CACHE_DIR / "TinyStories_all_data"
shard_filenames = sorted(glob.glob(str(data_dir / "*.json")))

for shard in shard_filenames:
    print(shard)
    with open(shard, "r") as g:
        data = json.load(g)
    for example in data:
        print(example['translated'])
        break
    break