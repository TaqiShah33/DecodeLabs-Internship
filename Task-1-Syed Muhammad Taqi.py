def main():
    # 1. KNOWLEDGE BASE: Dictionary with 5+ intents (Optimized O(1) Lookup)
    knowledge_base = {
        "hello": "Hi there! Welcome to DecodeLabs. How can I help you today?",
        "hi": "Hello! Hope you are having a productive day.",
        "help": "I can assist you with basic queries. Try asking me about 'internship' or 'ai'.",
        "internship": "Project 1 is your foundation! Complete this rule-based chatbot to unlock next week's tasks.",
        "ai": "Artificial Intelligence starts with robust, deterministic rules before moving to probabilistic models.",
        "status": "System operational. All guardrails are fully active."
    }

    print("====================================================")
    print("DecodeLabs Rule-Based AI Chatbot Initialized.")
    print("Type 'exit' or 'bye' to terminate the session.")
    print("====================================================\n")

    # 2. INPUT LOOP: Continuous 'while' cycle
    while True:
        # 3. INPUT & SANITIZATION: Handle case sensitivity and stray whitespace
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

        # 4. EXIT STRATEGY: Clean break commands
        if clean_input in ['exit', 'bye']:
            print("Bot: Goodbye! Session terminated safely.")
            break

        # 5. PROCESS & FALLBACK: Atomic operation using .get()
        # If clean_input matches a key, it returns the value. Otherwise, it triggers the fallback text.
        reply = knowledge_base.get(clean_input, "I'm sorry, I don't understand that command. Try asking 'help' or 'internship'.")
        
        # 6. OUTPUT
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    main()