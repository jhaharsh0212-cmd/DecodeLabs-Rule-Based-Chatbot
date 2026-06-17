🤖 Project 1: Deterministic Logic Engine (Rule-Based AI Chatbot)
This repository contains the foundational Phase 1 project for the DecodeLabs Industrial Training Kit (Batch 2026).
Before building probabilistic generative models (System 1), it is essential to master the precision of a deterministic logic engine (System 2). This project serves as a "white box" guardrail, providing high-speed, hard-coded responses with zero hallucination risk.  

🏗️ Architectural Overview
The system is built on the IPO (Input, Process, Output) model, functioning as a continuous digital loop that simulates basic human interaction through programmatic decision-making.  
Key Engineering Decisions:
Algorithmic Efficiency over Anti-Patterns: Instead of relying on structural weaknesses like an If-Elif ladder which operates at a linear time complexity $O(n)$, this engine utilizes Python Dictionaries (Hash Maps). This pivot ensures direct access and $O(1)$ instant lookup regardless of the knowledge base size.  
Atomic Operations: The intent matching and fallback mechanisms are handled simultaneously using the dictionary .get() method, combining the lookup and default error response into a single atomic operation.  
Sanitization Layer: All raw user inputs undergo sanitization (handling case modifications and whitespace stripping) before passing through the logic skeleton.  

⚙️ Features
Continuous Input Loop: The application runs an infinite while cycle, keeping the digital organism alive until explicitly terminated.  
Instant Keyword Mapping: Exact match mapping to predefined intents (e.g., greetings, status checks).  
Dynamic Fallbacks: Graceful handling of unknown edge cases to prepare for future hybrid architectures (where unmatched rules are passed to an LLM).  
Clean Exit Strategy: A dedicated kill command to safely break the process.  

🚀 How to Run
Clone this repository to your local machine.
Ensure you have Python 3.x installed.
Run the script via your terminal:
          Bashpython chatbot.py
Interact with the bot using known intents (like `hello`, `status`, or `help`), or type `exit` to terminate the program.

## 👨‍💻 Author
**Harsh** 
*AI Engineering Intern | DecodeLabs*[cite: 1]
