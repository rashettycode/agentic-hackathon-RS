# Utility functions can be placed here
import re
import json
import os

PROFILE_PATH = "memory/user_profile.json"

def infer_and_store(user_input: str, profile: dict) -> str | None:
    """
    Infers new information (e.g., snack time) from user input and stores it in the user profile.
    If something is inferred, returns a response string. Otherwise, returns None.
    """
    user_input_lower = user_input.lower()

    # Infer snack time
    if "snack" in user_input_lower and "pm" in user_input_lower:
        time_match = re.search(r"\b\d{1,2}(?::\d{2})?\s*pm\b", user_input_lower)
        if time_match:
            snack_time = time_match.group()
            profile.setdefault("routines", {})["snack"] = snack_time
            save_profile(profile)
            return f"Okay, I’ll remember that your snack time is around {snack_time}."

    # Add more inference rules below (e.g., nap time, call reminders, etc.)
    # Example:
    # if "walk" in user_input_lower and "am" in user_input_lower:
    #     ...

    return None

def save_profile(profile: dict, path: str = PROFILE_PATH):
    """
    Saves the updated profile dictionary to disk as JSON.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(profile, f, indent=4)
