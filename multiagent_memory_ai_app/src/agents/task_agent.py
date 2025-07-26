def plan_tasks(user_input: str, memories: str) -> list:
    # Naive task planner
    return [{"name": "search_gemini", "tool": "gemini", "input": user_input}]
