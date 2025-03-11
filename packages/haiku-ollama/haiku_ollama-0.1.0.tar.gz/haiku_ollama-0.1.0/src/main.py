#!/usr/bin/env python

import ollama
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich.spinner import Spinner

import os
import argparse
import signal
import sys


def main():
    """Main entry point for the application"""
    parser = argparse.ArgumentParser(description="AI model")

    DEFAULT_MODEL = 'llama3.1:8b'  # 'deepseek-r1:32b'

    parser.add_argument("--model", type=str, help="model name", default=DEFAULT_MODEL)
    parser.add_argument("--keep-context", "-k", action="store_true", help="Keep conversation context")
    parser.add_argument("--system", "-s", type=str, help="System prompt to guide the model's behavior")
    parser.add_argument("--temperature", "-t", type=float, default=0.7, help="Temperature (0.0-1.0). Lower values are more deterministic.")
    parser.add_argument("--save", type=str, help="Save conversation to file")
    args = parser.parse_args()

    print(f"I am {args.model} ask me anything 🧠")
    model = args.model
    console = Console()

    exit_text = ("exit", "bye")
    messages = []

    def clear_console():
        os.system('clear' if os.name == 'posix' else 'cls')

    def save_conversation(filename, msgs):
        """Save conversation history to a file."""
        if filename and msgs:
            with open(filename, 'w') as f:
                for msg in msgs:
                    f.write(f"{msg['role'].upper()}: {msg['content']}\n\n")
            print(f"Conversation saved to {filename}")

    def handle_interrupt(sig, frame):
        print("\nExiting gracefully...")
        save_conversation(args.save, messages)
        sys.exit(0)
        
    signal.signal(signal.SIGINT, handle_interrupt)

    # Add system prompt if provided
    if args.system:
        messages.append({'role': 'system', 'content': args.system})

    BREAK = True
    while BREAK:
        question = input("🤔: ")
        if question in exit_text:
            BREAK = False
            save_conversation(args.save, messages)
            continue
        
        messages.append({'role': 'user', 'content': question})

        line_text = ""
        spinner = Spinner("dots", text="Thinking...")
        with Live(spinner, refresh_per_second=10, vertical_overflow="visible") as live:
            # Start the stream
            stream = ollama.chat(
                model=model,
                messages=messages if args.keep_context else [{'role': 'user', 'content': question}],
                stream=True,
                options={"temperature": args.temperature}
            )
            
            # Once we get the first chunk, replace the "Thinking..." with actual content
            first_chunk = True
            for chunk in stream:
                chunk_message = chunk['message']['content']
                if first_chunk:
                    line_text = chunk_message
                    first_chunk = False
                else:
                    line_text += chunk_message
                    
                # Update with rendered markdown
                live.update(Markdown(line_text))
        
        # Add response to messages
        messages.append({'role': 'assistant', 'content': line_text})


if __name__ == "__main__":
    main()