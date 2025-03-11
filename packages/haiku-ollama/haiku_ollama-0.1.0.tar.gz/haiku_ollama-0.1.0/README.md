
# Haiku 
A clean, elegant command-line interface for chatting with local AI models via Ollama, featuring real-time Markdown rendering. 
 
## Features 
 
- 💬 Interactive chat interface with Ollama models 
- 📝 Real-time Markdown rendering (code blocks, tables, lists, etc.) 
- 🔄 Full conversation context preservation 
- 🎯 Customizable system prompts 
- 🌡️ Adjustable temperature settings 
- 💾 Conversation saving to files 
 
## Installation 
 
```bash 
pip install haiku-ollama 
```
 
Make sure you have Ollama installed and running before using Haiku. 
 
## Usage 
 
Start a conversation with the default model (llama3.1:8b): 
 
```bash 
haiku 
```
 
### Command Line Options 
 
| Option | Description | 
|--------|-------------| 
| --model | Specify which Ollama model to use (default: llama3.1:8b) | 
| --keep-context, -k | Maintain full conversation history between prompts | 
| --system, -s | Set a custom system prompt to guide the model's behavior | 
| --temperature, -t | Set temperature (0.0-1.0) - lower values are more deterministic | 
| --save | Save the conversation to a specified file | 
 
### Examples 
 
Using a specific model: 
 
```bash 
haiku --model mistral:7b 
```
 
Preserving conversation context: 
 
```bash 
haiku --keep-context 
````
 
Setting a system prompt: 
 
```bash 
haiku --system "You are an expert programmer who explains code concisely" 
```
 
Adjusting temperature: 
 
```bash 
haiku --temperature 0.2 
```
 
Saving your conversation: 
 
```bash 
haiku --save conversation.md 
```
 
Combining multiple options: 
 
```bash 
haiku --model codellama --keep-context --system "You write Python code" --temperature 0.3 --save coding_session.md 
 ```
 
## Exiting 
 
To exit the program, simply type exit or bye, or press Ctrl+C. 
 
## Requirements 
 
- Python 3.8+ 
- Ollama installed and running 
- Python packages: ollama, rich 
 
## Contributing 
 
Contributions are welcome! Feel free to submit issues or pull requests. 
 
## License 
 
MIT License