from memory.retriever import retrieve_memories, store_memory
from memory.profile_loader import load_user_profile
from agents.task_agent import plan_tasks
from agents.execution_agent import execute_tasks
from response_generator import generate_final_response
from utils.inference import infer_and_store

def handle_user_input(user_input: str) -> str:
    profile = load_user_profile()
    user_input_lower = user_input.lower()

    # 👋 Small talk
    if "hi" in user_input_lower or "hello" in user_input_lower:
        return f"Hi {profile.get('name', 'there')}! 👋 How can I help you today?"
    
    if "how are you" in user_input_lower:
        return "I'm doing great and always ready to help! 😊 How are you feeling today?"

    if "thank you" in user_input_lower or "thanks" in user_input_lower:
        return "You're always welcome! I'm here anytime you need me. 🙏"

    if "help" in user_input_lower:
        return "You can ask me about your routine, reminders, medications, or just have a friendly chat. 💬"

    if "exit" in user_input_lower:
        return "👋 Goodbye! Take care."

    # 🍽 Meal-time routines
    if "lunch" in user_input_lower:
        return f"Lunch is usually at {profile.get('routines', {}).get('lunch', 'an unspecified time')}."
    if "dinner" in user_input_lower:
        return f"Dinner is usually at {profile.get('routines', {}).get('dinner', 'an unspecified time')}."
    if "breakfast" in user_input_lower:
        return f"Breakfast is usually at {profile.get('routines', {}).get('breakfast', 'an unspecified time')}."
    if "white pill" in user_input_lower:
        return f"You take the white pill {profile.get('routines', {}).get('medications', {}).get('white pill', 'at an unspecified time')}."

    # 🍲 Dinner memory
    if "what do i eat for dinner" in user_input_lower:
        favorite_food = profile.get("favorite_food", "I don't know what's for dinner yet.")
        return f"You usually eat {favorite_food} for dinner."

    # 🍕 Favorite food
    if "favorite food" in user_input_lower or "favourite food" in user_input_lower:
        favorite_food = profile.get("favorite_food")
        if favorite_food:
            return f"Your favorite food is {favorite_food}."
        else:
            return "I don't know your favorite food yet. You can tell me if you'd like!"

    # 🎨 Favorite color
    if "favorite color" in user_input_lower or "favourite color" in user_input_lower:
        fav_color = profile.get("favorite_color")
        if fav_color:
            return f"Your favorite color is {fav_color}."
        else:
            return "I don’t know your favorite color yet. You can tell me if you'd like!"

    # 🧠 Dynamic memory inference and storage
    infer_and_store(user_input)

    # 💾 Store if reminder-style instruction
    if user_input_lower.startswith("remind me"):
        store_memory(user_input)
        return "Got it! I'll remember that for you."

    # 🧠 Retrieve past memories
    memories = retrieve_memories(user_input)

    # 📋 Plan and execute
    task_plan = plan_tasks(user_input, memories)
    tool_outputs = execute_tasks(task_plan)

    # 🧾 Generate final response
    final_response = generate_final_response(user_input, memories, task_plan, tool_outputs)

    if not final_response or final_response.strip().lower() in ["none", "null", ""]:
        return "I'm not sure how to help with that yet, but I'm learning!"

    return final_response


