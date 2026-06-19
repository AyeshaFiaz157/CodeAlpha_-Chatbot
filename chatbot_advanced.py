"""
╔══════════════════════════════════════════════════════╗
║   ADVANCED CHATBOT — CodeAlpha Internship             ║
║   Task 4 | Python Programming                         ║
╚══════════════════════════════════════════════════════╝

An upgraded rule-based chatbot. Still no AI/ML — just smarter
pattern matching using keyword search instead of exact phrases,
so it can respond to a much wider range of input.

Key concepts used: if-elif, functions, loops, input/output,
                    string methods, lists, dictionaries, datetime
"""

import random
from datetime import datetime


BOT_NAME = "CodeBot"
CREATOR = "a CodeAlpha intern"


def contains_any(text, keywords):
    """Return True if any keyword appears inside text."""
    return any(word in text for word in keywords)


def get_response(user_input):
    """
    Analyze the user's message using keyword-based rules and
    return an appropriate reply. Order matters: more specific
    checks come before general ones.
    """
    text = user_input.lower().strip()

    # ─── Empty input ────────────────────────────────
    if not text:
        return "Say something — I'm listening!"

    # ─── Farewell (checked early so it doesn't get
    #      caught by other broader rules) ────────────
    if contains_any(text, ["bye", "goodbye", "see you", "exit", "quit", "good night"]):
        return random.choice(["Goodbye! Take care.", "See you later!", "Bye! It was nice chatting."])

    # ─── Greetings ──────────────────────────────────
    elif contains_any(text, ["hello", "hi", "hey", "salaam", "assalam", "yo "]) or text in ("hi", "hey", "yo"):
        return random.choice(["Hi there!", "Hello!", "Hey! Good to see you.", "Hi! How's it going?"])

    # ─── How are you ────────────────────────────────
    elif contains_any(text, ["how are you", "how r u", "how do you do", "kaise ho", "kya hal"]):
        return "I'm fine, thanks! How about you?"

    elif contains_any(text, ["i am good", "i'm good", "i'm fine", "doing good", "doing great", "i am fine"]):
        return random.choice(["Glad to hear that! 😊", "That's great!"])

    elif contains_any(text, ["i am sad", "i'm sad", "feeling down", "not good", "not feeling well", "i am tired", "i'm tired"]):
        return "I'm sorry to hear that. I hope things get better for you soon."

    # ─── Bot identity ───────────────────────────────
    elif contains_any(text, ["your name", "who are you", "what are you"]):
        return f"I'm {BOT_NAME}, a rule-based chatbot built for a CodeAlpha internship task."

    elif contains_any(text, ["who made you", "who created you", "your creator"]):
        return f"I was built by {CREATOR} as part of the CodeAlpha Python internship."

    elif contains_any(text, ["how old are you", "your age"]):
        return "I don't have an age — I'm just lines of Python code!"

    # ─── User introducing themselves ────────────────
    elif "my name is" in text:
        name = text.split("my name is")[-1].strip().split()[0].title()
        return f"Nice to meet you, {name}!"

    elif text.startswith("i am ") or text.startswith("i'm "):
        name = text.replace("i'm", "i am").replace("i am", "").strip().split()[0].title()
        return f"Nice to meet you, {name}!"

    # ─── Time / date ────────────────────────────────
    elif contains_any(text, ["what time", "current time", "time now"]):
        return f"Right now it's {datetime.now().strftime('%I:%M %p')}."

    elif contains_any(text, ["what date", "today's date", "what day"]):
        return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

    # ─── Weather chit-chat (no real API, just a friendly dodge) ──
    elif "weather" in text:
        return "I can't check live weather, but I hope it's nice where you are!"

    # ─── Small talk: jokes ──────────────────────────
    elif contains_any(text, ["joke", "make me laugh", "funny"]):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the function break up with the loop? It needed space.",
            "I told my computer I needed a break, and it said: 'No problem, I'll go to sleep.'",
        ]
        return random.choice(jokes)

    # ─── Compliments / gratitude ─────────────────────
    elif contains_any(text, ["thanks", "thank you", "thx", "appreciate it"]):
        return random.choice(["You're welcome!", "Anytime!", "Happy to help!"])

    elif contains_any(text, ["you are smart", "you are cool", "you are great", "good bot", "nice bot", "you're great", "love this"]):
        return "Aw, thank you! That made my day. 😊"

    # ─── Help / capabilities ────────────────────────
    elif contains_any(text, ["help", "what can you do", "options", "commands"]):
        return (
            "I can chat about a few things — try greetings, asking how I am, my name, "
            "the time/date, asking for a joke, or saying bye."
        )

    # ─── Yes / No casual replies ─────────────────────
    elif text in ("yes", "yeah", "yup", "sure"):
        return "Got it!"

    elif text in ("no", "nope", "nah"):
        return "Okay, no worries."

    # ─── Fallback ───────────────────────────────────
    else:
        fallbacks = [
            "Sorry, I didn't understand that. Try saying 'hello', 'how are you', or ask for a joke.",
            "I'm not sure how to respond to that yet — I'm a simple rule-based bot!",
            "Hmm, that's beyond what I know. Try 'help' to see what I can do.",
        ]
        return random.choice(fallbacks)


def is_exit_command(text):
    """Check if the user wants to end the chat."""
    return contains_any(text.lower().strip(), ["bye", "goodbye", "see you", "exit", "quit"])


def chat():
    """Main chat loop."""
    print("=" * 55)
    print(f"      {BOT_NAME} (Advanced) — CodeAlpha Chatbot")
    print("=" * 55)
    print(f"  {BOT_NAME}: Hi! I'm {BOT_NAME}. Type 'help' to see what I can do, or 'bye' to exit.\n")

    while True:
        user_input = input("  You: ").strip()

        if not user_input:
            print(f"  {BOT_NAME}: Say something!\n")
            continue

        response = get_response(user_input)
        print(f"  {BOT_NAME}: {response}\n")

        if is_exit_command(user_input):
            break

    print("=" * 55)
    print("      Chat ended — CodeAlpha Internship")
    print("=" * 55)


if __name__ == "__main__":
    chat()
