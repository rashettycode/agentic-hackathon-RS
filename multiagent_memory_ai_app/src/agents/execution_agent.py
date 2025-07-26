from tools.gemini_api import query_gemini

def execute_tasks(task_plan: list) -> dict:
    results = {}
    for task in task_plan:
        if task["tool"] == "gemini":
            results[task["name"]] = query_gemini(task["input"])
    return results
