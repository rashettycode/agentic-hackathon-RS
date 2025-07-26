import json
import os
import re
from memory.profile_loader import load_user_profile, save_profile

PROFILE_PATH = os.path.join("data", "user_profile.json")

def infer_and_store(user_input: str):
    profile = load_user_profile()
    user_input_lower = user_input.lower()

    updated = False

    # Favorite color
    color_match = re.search(r"(?:my favorite color is|favourite colour is|favourite color is|it is)\s+([a-zA-Z\s]+)", user_input_lower)
    if color_match:
        color = color_match.group(1).strip()
        profile["favorite_color"] = color
        updated = True
        print(f"[Memory] Learned favorite color: {color}")

    # Favorite food
    food_match = re.search(r"(?:my favorite food is|favourite food is|i love eating|i usually eat)\s+([a-zA-Z\s]+)", user_input_lower)
    if food_match:
        food = food_match.group(1).strip()
        profile["favorite_food"] = food
        updated = True
        print(f"[Memory] Learned favorite food: {food}")

    # User name
    name_match = re.search(r"(?:my name is|i am)\s+([a-zA-Z]+)", user_input_lower)
    if name_match:
        name = name_match.group(1).strip().capitalize()
        profile["name"] = name
        updated = True
        print(f"[Memory] Learned user name: {name}")

    # Save profile if updated
    if updated:
        save_profile(profile)
