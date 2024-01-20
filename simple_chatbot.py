import openai
import tkinter as tk
from tkinter import scrolledtext
from nltk.tokenize import sent_tokenize

# Set your OpenAI API key here
openai.api_key = 'YOUR_API_KEY'

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.chat_history.pack(padx=10, pady=10)

        self.user_input = tk.Entry(master, width=40)
        self.user_input.pack(pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        user_message = self.user_input.get()
        self.display_message(f"User: {user_message}")

        # Call OpenAI API to get the chatbot's response
        chatbot_response = self.get_chatbot_response(user_message)
        self.display_message(f"Chatbot: {chatbot_response}")

        # Clear the user input
        self.user_input.delete(0, tk.END)

    def get_chatbot_response(self, user_message):
        # Tokenize the user message into sentences using NLTK
        sentences = sent_tokenize(user_message)

        # Use the last sentence as the prompt for OpenAI API
        prompt = f"User: {sentences[-1]}\nChatbot:"

        # Call OpenAI API to get the chatbot's response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=100,
            n=1,
        )

        return response.choices[0].text.strip()

    def display_message(self, message):
        current_text = self.chat_history.get("1.0", tk.END).strip()
        new_text = f"{current_text}\n{message}"
        self.chat_history.delete("1.0", tk.END)
        self.chat_history.insert(tk.END, new_text)
        self.chat_history.yview(tk.END)

def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
