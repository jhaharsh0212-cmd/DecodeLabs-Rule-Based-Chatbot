import time
import random

def run_logic_engine():
    """
    Project 1 Submission: Rule-Based Chatbot
    Author: Harsh
    Notes: Ditched the highly inefficient O(n) if-elif ladder for an O(1) dictionary lookup. 
    """
    
    # The core knowledge base (Hash Map). 
    responses = {
        "hello": "Hey there! Welcome to the DecodeLabs platform.",
        "hi": "Hello! I'm awake and ready to process commands.",
        "status": "All systems operational. The logic engine is humming along nicely.",
        "what is your objective": "I'm a deterministic guardrail. I handle the knowns before passing the unknowns to an LLM.",
        "help": "Keep it simple. You can say 'hello', check my 'status', ask about 'krishimitra', or type 'exit' to bail.",
        "bye": "Catch you later! Shutting down."
    }

    # Dynamic fallbacks so the bot doesn't sound like a broken record
    fallbacks = [
        "I'm drawing a blank here. Try a known command.",
        "Does not compute! Try typing 'help'.",
        "I'm just a rule-based skeleton, I don't know that one yet."
    ]

    print("--> Booting up DecodeLabs Logic Engine...")
    time.sleep(1) # Fake loading time for aesthetic
    print("--> System ready. Type 'exit' to terminate.\n")

    # The infinite loop heartbeat
    while True:
        # Grab user input
        raw_text = input("You: ")
        
        # Sanitize: clean up weird spaces and make it lowercase
        clean_text = raw_text.lower().strip()
        
        # Exit strategy
        if clean_text == 'exit':
            print("Bot: Terminating process. See ya!")
            break
            
        # Simulate a slight "thinking" delay to feel more natural
        time.sleep(0.4)
        
        # The atomic dictionary lookup. If the key isn't there, pick a random fallback.
        default_reply = random.choice(fallbacks)
        reply = responses.get(clean_text, default_reply)
        
        print(f"Bot: {reply}")

if __name__ == "__main__":
    run_logic_engine()