MyMemory AI: Building AI That Remembers What Matters
Introduction
AI assistants are becoming part of everyday work and learning, but one major problem remains: they often lose continuity between conversations. Users may have to repeat their goals, preferences, projects, deadlines, and previous decisions again and again.
MyMemory AI is our solution to this problem — a personal AI assistant designed to remember useful context and use it to make future conversations more relevant.
The Problem
A normal AI conversation can be helpful in the moment, but important context may not carry forward.
For example, a student might tell an AI:
“I want to get a robotics internship by December. I am currently learning Python and machine learning.”
Later, the student may ask:
“What should I focus on this week?”
Without memory, the assistant may give generic advice. With long-term memory, it can understand that the user's current priority is the robotics internship and tailor the response accordingly.
Our Solution
MyMemory AI uses Hindsight as its long-term memory layer.
The basic memory loop is:
The user talks to the assistant.
Useful information is identified.
Important context is stored using Hindsight.
Relevant memories are retrieved when needed.
The AI uses those memories to generate a personalized response.
The conversation continues with context.
This turns an AI assistant from a system that simply answers individual questions into one that can maintain continuity across conversations.
Key Features
Long-term memory across conversations
Goal and project continuity
Retrieval of relevant past context
Personalized responses
Support for important dates and commitments
User-controlled memory
Privacy-focused memory controls
Privacy by Design
Memory should belong to the user.
MyMemory AI is designed around simple controls such as:
Remember — save useful information for future conversations.
Temporarily remember — use information for the current interaction.
Don't remember — prevent information from being stored.
Forget — remove information the user no longer wants remembered.
The goal is to make memory useful without taking control away from the user.
Technology Stack
Our prototype uses:
Python
FastAPI
Hindsight
LLM API
Web technologies
Vercel for deployment of the frontend prototype
Example Use Case
Imagine a student working toward a long-term career goal.
On Day 1:
“I want to get a robotics internship by December. I am learning Python and machine learning.”
On Day 20:
“What should I focus on this week?”
MyMemory AI can retrieve the relevant goal and learning context before answering. Instead of starting from zero, the assistant can continue from where the user left off.
Why MyMemory AI?
The future of personal AI should not be based only on better answers. It should also be based on better continuity.
People have ongoing goals, projects, decisions, deadlines, and preferences. MyMemory AI aims to give those conversations continuity while keeping memory under the user's control.
Conclusion
MyMemory AI — a personal AI assistant that remembers what matters.
Built by Team Nakama for the hackathon, our project explores how long-term memory can make AI interactions more useful, personal, and continuous.
GitHub: https://github.com/bhanumudhiraj798-hub/mymemory-ai
