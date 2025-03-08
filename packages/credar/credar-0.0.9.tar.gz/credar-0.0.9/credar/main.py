import os
import sys
import argparse
import json
import git
from pathlib import Path
from typing import List, Dict, Optional, Union

from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter, Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.filters import has_focus

from litellm import completion

# Config directory setup
CONFIG_DIR = os.path.join("credar_config_dir")
HISTORY_FILE = os.path.join(CONFIG_DIR, "history.txt")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

# Ensure config directory exists
os.makedirs(CONFIG_DIR, exist_ok=True)

# Default configurations
DEFAULT_CONFIG = {
    "openai": {
        "model": "gpt-4o",
        "api_key": "",
        "base_url": "https://api.openai.com/v1/"
    },
    "ollama": {
        "model": "openai/qwen2.5:0.5b-instruct",
        "api_key": "ollama",
        "base_url": "http://localhost:11434/v1/"
    },
    "dsollama": {
        "model": "openai/qwen2.5:7b-instruct",
        "api_key": "ollama",
        "base_url": "http://192.168.170.76:11434/v1/"
    },
    "deepseek": {
        "model": "openai/hf.co/bartowski/DeepSeek-R1-Distill-Qwen-14B-GGUF:Q5_K_M",
        "api_key": "ollama",
        "base_url": "http://192.168.170.76:11434/v1/"
    },
    # "deepseek": {
    #     "model": "openai/hf.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF:Q5_K_M",
    #     "api_key": "ollama",
    #     "base_url": "http://localhost:11434/v1/"
    # },

    "current_mode": "Ask"
}


# Combined completer for both commands and files
class CredarCompleter(Completer):
    def __init__(self, commands):
        self.commands = commands
        self._update_file_list()

    def _update_file_list(self):
        """Update the list of files in the git repository"""
        self.files = []
        try:
            # Try to initialize a git repo from the current directory
            repo = git.Repo(os.getcwd(), search_parent_directories=True)
            repo_root = repo.git.rev_parse("--show-toplevel")

            # Get tracked files in the repository
            for file_path in repo.git.ls_files().split('\n'):
                if file_path:  # Skip empty entries
                    abs_path = os.path.join(repo_root, file_path)
                    self.files.append((file_path, abs_path))

            # Add untracked files that aren't ignored
            for file_path in repo.git.ls_files("--others", "--exclude-standard").split('\n'):
                if file_path:  # Skip empty entries
                    abs_path = os.path.join(repo_root, file_path)
                    self.files.append((file_path, abs_path))

        except git.exc.InvalidGitRepositoryError:
            # If not in a git repo, just use files in current directory (recursively)
            for root, _, files in os.walk(os.getcwd()):
                for file in files:
                    abs_path = os.path.join(root, file)
                    rel_path = os.path.relpath(abs_path, os.getcwd())
                    self.files.append((rel_path, abs_path))

    def get_completions(self, document, complete_event):
        text = document.text
        word_before_cursor = document.get_word_before_cursor()

        # Command completion for slash commands
        if text.startswith('/'):
            word = text[1:]
            for command in self.commands:
                if command.lower().startswith(word.lower()):
                    yield Completion(command, start_position=-len(word))

        # File completion for @ symbol
        elif '@' in text:
            # Get the text after the last @ symbol
            parts = text.split('@')
            prefix = '@'.join(parts[:-1])
            file_prefix = parts[-1].strip()

            # Position where the file prefix begins
            prefix_pos = len(prefix) + 1  # +1 for the @ symbol

            # Find the cursor position relative to the file prefix
            cursor_pos_in_doc = document.cursor_position
            relative_pos = cursor_pos_in_doc - prefix_pos

            # Only complete if cursor is in the file prefix area
            if relative_pos >= 0 and (not file_prefix or file_prefix in text[prefix_pos:cursor_pos_in_doc]):
                for rel_path, abs_path in self.files:
                    if file_prefix.lower() in rel_path.lower():
                        # The completion text is the filename with the file path in parentheses
                        file_name = rel_path.split("/")[-1]
                        completion_text = f"{file_name}({rel_path})"
                        display_text = f"{file_name} ({rel_path})"

                        # Calculate start position for replacement
                        start_pos = -len(file_prefix) if file_prefix else 0

                        yield Completion(
                            completion_text,
                            start_position=start_pos,
                            display=display_text,
                            # display_meta="File"
                        )


# Styles for the prompt
style = Style.from_dict({
    'prompt': 'ansicyan bold',
    'agent': 'ansigreen bold',
    'chat': 'ansiblue bold',
})


class CredarCLI:
    def __init__(self):
        self.load_config()
        self.setup_parser()
        self.history = FileHistory(HISTORY_FILE)

        # Available slash commands
        self.commands = ["Agent", "Ask", "Clear", "Config", "Exit", "Help", "Refresh"]

        # Initialize the completer with commands
        self.completer = CredarCompleter(self.commands)

        # Initialize prompt session
        self.session = PromptSession(
            history=self.history,
            auto_suggest=AutoSuggestFromHistory(),
            completer=self.completer
        )

        self.mode = self.config.get("current_mode", "Ask")
        self.conversation_history = []

    def load_config(self):
        """Load or create config file"""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = DEFAULT_CONFIG
            self.save_config()

    def save_config(self):
        """Save config to file"""
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=2)

    def setup_parser(self):
        """Setup command line argument parser"""
        self.parser = argparse.ArgumentParser(description="Credar CLI - AI Assistant")
        self.parser.add_argument("--ollama", action="store_true", help="Use Ollama models")
        self.parser.add_argument("--deepseek", action="store_true", help="Use Ollama models")
        self.parser.add_argument("--dsollama", action="store_true", help="Use Ollama models")
        self.parser.add_argument("--openai", action="store_true", help="Use OpenAI models (default)")
        self.parser.add_argument("--model", type=str, help="Specify model name")
        self.parser.add_argument("--api-key", type=str, help="API key for the service")
        self.parser.add_argument("--base-url", type=str, help="Base URL for the API")
        self.parser.add_argument("--thinking", action="store_true", help="Show model thinking when available")

    def parse_args(self):
        """Parse command line arguments and update config"""
        args = self.parser.parse_args()

        # Determine provider (default to openai if none specified)
        if args.ollama:
            self.provider = "ollama"
        elif args.dsollama:
            self.provider = "dsollama"
        elif args.deepseek:
            self.provider = "deepseek"
        else:
            self.provider = "openai"

        # Update config with command line args if provided
        if args.model:
            self.config[self.provider]["model"] = args.model
        if args.api_key:
            self.config[self.provider]["api_key"] = args.api_key
        if args.base_url:
            self.config[self.provider]["base_url"] = args.base_url

        self.show_thinking = args.thinking

        self.save_config()

    def get_prompt_prefix(self):
        """Get the prompt prefix based on current mode"""
        if self.mode == "Agent":
            return HTML('<style fg="green">[Agent]</style> ')
        else:
            return HTML('<style fg="blue">[Ask]</style> ')

    def process_command(self, command):
        """Process slash commands"""
        cmd_parts = command[1:].strip().split()  # Remove the leading / and split by space
        cmd = cmd_parts[0].lower()
        args = cmd_parts[1:] if len(cmd_parts) > 1 else []

        if cmd == "agent":
            self.mode = "Agent"
            self.config["current_mode"] = "Agent"
            self.save_config()
            print("Switched to Agent mode")
            return True

        elif cmd == "ask":
            self.mode = "Ask"
            self.config["current_mode"] = "Ask"
            self.save_config()
            print("Switched to Ask mode")
            return True

        elif cmd == "clear":
            self.conversation_history = []
            print("Conversation history cleared")
            return True

        elif cmd == "config":
            print(f"Current configuration ({self.provider}):")
            print(json.dumps(self.config[self.provider], indent=2))
            return True

        elif cmd == "refresh":
            self.completer._update_file_list()
            print("File list refreshed")
            return True

        elif cmd == "exit":
            print("Goodbye!")
            sys.exit(0)

        elif cmd == "help":
            print("Available commands:")
            print("  /Agent    - Switch to Agent mode")
            print("  /Ask      - Switch to Ask mode")
            print("  /Clear    - Clear conversation history")
            print("  /Config   - Show current configuration")
            print("  /Refresh  - Refresh the file list")
            print("  /Exit     - Exit the application")
            print("  /Help     - Show this help")
            print("\nFile completion:")
            print("  Type '@' to search for files in the git repository or current directory")
            return True

        else:
            print(f"Unknown command: /{cmd}")
            return True

    def process_file_tags(self, text):
        """Process text to extract file tags and potentially read file contents"""
        import re

        # Find all occurrences of @filename in the text
        file_tags = re.findall(r'@(\S+)', text)

        result = text

        if file_tags:
            for file_tag in file_tags:
                file_rel_path = file_tag[file_tag.find("(") + 1:-1]
                try:
                    with open(os.path.join(os.getcwd(), file_rel_path), 'r') as f:
                        file_content = f.read()
                    result = result.replace(f'@{file_tag}', f'[{file_tag}]:\n```\n{file_content}\n```')
                except Exception as e:
                    result = result.replace(f'@{file_tag}', f'[Failed to read {file_tag}: {str(e)}]')
        return result

    def get_llm_response(self, prompt):
        """Get response from LLM"""
        provider_config = self.config[self.provider]

        # Process any file references in the prompt
        processed_prompt = self.process_file_tags(prompt)

        try:
            # Prepare messages for the API
            messages = []

            # Add conversation history
            for entry in self.conversation_history:
                messages.append(entry)

            # Add the new user message
            messages.append({"role": "user", "content": processed_prompt})

            # Get response from the API
            response = completion(
                model=provider_config["model"],
                api_key=provider_config["api_key"],
                base_url=provider_config["base_url"],
                messages=messages,
                stream=True
            )

            # Process streaming response
            full_response = ""
            in_thinking_block = False
            thinking_content = ""

            for chunk in response:
                if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                    # Extract text from the chunk based on its structure
                    if hasattr(chunk.choices[0], 'delta') and hasattr(chunk.choices[0].delta, 'content'):
                        content = chunk.choices[0].delta.content
                        if content:
                            # Check for thinking tags
                            if "<think>" in content:
                                if not self.show_thinking:
                                    print("Thinking ...", end="", flush=True)
                                in_thinking_block = True
                                # Split at the tag and handle the part before it
                                parts = content.split("<think>", 1)
                                if parts[0]:  # If there's content before the tag
                                    print(parts[0], end='', flush=True)
                                    full_response += parts[0]
                                # Start collecting thinking content if enabled
                                if self.show_thinking:
                                    print("<think>", end='', flush=True)
                                thinking_content = ""
                                if len(parts) > 1:  # If there's content after the tag
                                    thinking_content += parts[1]
                                    if self.show_thinking:
                                        print(parts[1], end='', flush=True)
                            elif "</think>" in content and in_thinking_block:
                                in_thinking_block = False
                                # Split at the tag and handle the parts
                                parts = content.split("</think>", 1)
                                if parts[0]:  # If there's content before the closing tag
                                    thinking_content += parts[0]
                                    if self.show_thinking:
                                        print(parts[0], end='', flush=True)
                                if self.show_thinking:
                                    print("</think>", end='', flush=True)
                                if len(parts) > 1:  # If there's content after the closing tag
                                    print(parts[1], end='', flush=True)
                                    full_response += parts[1]
                            elif in_thinking_block:
                                thinking_content += content
                                if self.show_thinking:
                                    print(content, end='', flush=True)
                            else:
                                print(content, end='', flush=True)
                                full_response += content
            print("\n")  # End with a new line

            # Add the assistant's response to conversation history
            self.conversation_history.append({"role": "user", "content": processed_prompt})
            self.conversation_history.append({"role": "assistant", "content": full_response})

            return full_response

        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def run(self):
        """Main loop for the CLI"""
        self.parse_args()

        print(f"Credar CLI v0.1.0 - Using {self.provider} with model {self.config[self.provider]['model']}")
        print("Type /help for available commands")
        print("Type '@' to search for files in the repository")

        while True:
            try:
                # Get user input with appropriate prefix and command completion
                user_input = self.session.prompt(
                    self.get_prompt_prefix(),
                    style=style
                )

                # Process slash commands
                if user_input.startswith('/'):
                    self.process_command(user_input)
                    continue

                # Skip empty inputs
                if not user_input.strip():
                    continue

                # Get response from LLM
                if self.mode == "Agent":
                    # Agent mode - special processing could be added here
                    self.get_llm_response(user_input)
                else:
                    # Regular chat mode
                    self.get_llm_response(user_input)

            except KeyboardInterrupt:
                print("\nUse /exit to quit")
            except EOFError:
                print("\nGoodbye!")
                break


def main():
    """Entry point for the CLI"""
    cli = CredarCLI()
    cli.run()


if __name__ == '__main__':
    main()
