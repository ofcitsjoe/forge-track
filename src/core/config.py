import json
from pathlib import Path

CONFIG_PATH = Path("config.json")

DEFAULT_CONFIG = {
    "games": [
        "DetroitBecomeHuman.exe",
        "Hades.exe",
        "Stardew Valley.exe",
        "zen.exe"
    ]
}

def load_config():
    """loads the configuration from the config.json file, or creates it with default values if it doesn't exist"""

    if not CONFIG_PATH.exists():
        print("Config file not found. Creating default config.json...")

        with open(CONFIG_PATH, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)

        return DEFAULT_CONFIG
    
    with open(CONFIG_PATH, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("WARNING: Config file is corrupted. Recreating default config.json...")
            
            return DEFAULT_CONFIG
        
if __name__ == "__main__":
    config = load_config()
    print("Loaded configuration:", config)