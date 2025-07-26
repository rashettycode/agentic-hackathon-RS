from agents.user_agent import handle_user_input

def run_agent():
    print("👋 Hi, I’m your Sarah you personal memory assistant. Ask me anything (type 'exit' to quit).")
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Take care.")
            break
        response = handle_user_input(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    run_agent()
