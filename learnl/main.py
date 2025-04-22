
import os
import sys

# Try to import readline for command history on Linux/macOS
try:
    import readline
except ImportError:
    readline = None  # On Windows, this disables native readline history

from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML

from .shell import run_shell_command
from .llm import ask_llm

# To store the last LLM suggestion
last_suggestion = ""

# Prompt-toolkit setup
session = PromptSession()
kb = KeyBindings()

# Load last 5 bash history commands from ~/.bash_history
def get_last_5_bash_history():
    history_path = os.path.expanduser("~/.bash_history")
    if os.path.exists(history_path):
        with open(history_path, "r") as f:
            lines = f.read().splitlines()
            return lines[-5:] if len(lines) >= 5 else lines
    return []

# Ctrl+S: Insert the last LLM suggestion
@kb.add('c-s')
def _(event):
    buffer = event.app.current_buffer
    buffer.document = buffer.document.insert_after(last_suggestion)
    buffer.validate_and_handle()


def get_prompt():
    # Get the current working directory
    current_dir = os.getcwd()

    # Colorize the current directory in blue
    prompt = f'<ansiblue>{current_dir}</ansiblue>-$ '  # ansiblue makes the text blue
    return prompt


def main():
    global last_suggestion
    print("🤖 learnl assistant (interactive) started.")
    print("💡 Type your shell command or a prompt like 'learnl make a folder called test'")
    print("🎯 Press Ctrl+S to run the suggested command\n")

    # Load bash history
    history = get_last_5_bash_history()

    while True:
        try:
            prompt = get_prompt()  # Get the colored prompt
            user_input = session.prompt(HTML(prompt), key_bindings=kb).strip()
            if not user_input:
                continue

            # If input starts with 'learnl', treat it as a prompt to LLM
            if user_input.lower().startswith("learnl"):
                parts = user_input.split(maxsplit=1)
                question = parts[1] if len(parts) > 1 else ""
                suggestion = ask_llm(history, question)
                last_suggestion = suggestion
                print(f"\n📥 Suggested command:\n{suggestion}")
                print("▶ Press Ctrl+S to inject into prompt buffer\n")
            else:
                # Otherwise, treat it as a real shell command
                run_shell_command(user_input)
                history.append(user_input)

        except (KeyboardInterrupt, EOFError):
            print("\n👋 Exiting learnl.")
            break
