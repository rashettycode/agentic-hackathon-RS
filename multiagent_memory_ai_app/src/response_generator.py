def generate_final_response(user_input, memories, task_plan, tool_outputs) -> str:
    # Handle Gemini or tool responses cleanly
    if tool_outputs and isinstance(tool_outputs, dict):
        for source, output in tool_outputs.items():
            if isinstance(output, str) and output.strip():
                return output.strip()

    # Fallback message
    return "I'm not sure how to help with that yet, but I'm learning!"

