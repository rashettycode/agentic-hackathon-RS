import json
import os

PROFILE_PATH = "memory/user_profile.json"

# Default structure
DEFAULT_PROFILE = {
    "name": "User",
    "preferences": {
        "wants_reminders": True
    },
    "contacts": [],
    "routines": {
        "breakfast": "8:00 AM",
        "lunch": "1:00 PM",
        "dinner": "7:00 PM",
        "medications": {}
    },
    "traits": {}
}

def load_user_profile():
    """Load the user profile and ensure all required keys are present."""
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, "r") as f:
            profile = json.load(f)
    else:
        profile = {}

    # Ensure all keys exist
    for key, default_value in DEFAULT_PROFILE.items():
        if key not in profile:
            profile[key] = default_value
        elif isinstance(default_value, dict):
            # Recursively ensure sub-keys exist
            for sub_key, sub_default in default_value.items():
                if sub_key not in profile[key]:
                    profile[key][sub_key] = sub_default

    return profile

def save_profile(profile):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=2)

