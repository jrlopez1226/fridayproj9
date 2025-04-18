import tkinter as tk
from tkinter import scrolledtext, messagebox
import openai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found in .env file.")

openai.api_key = api_key

def get_completion():
    prompt = prompt_input.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("Input Error", "Please enter a prompt.")
        return

    try:
        # Use openai.ChatCompletion only for chat models
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        output_text = response.choices[0].message.content
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output_text.strip())
        output_box.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("API Error", str(e))


# GUI setup
root = tk.Tk()
root.title("OpenAI Prompt GUI")
root.geometry("600x500")

tk.Label(root, text="Enter your prompt below:", font=("Arial", 12)).pack(pady=5)

prompt_input = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD, font=("Arial", 10))
prompt_input.pack(padx=10, pady=5, fill=tk.BOTH)

submit_btn = tk.Button(root, text="Submit Prompt", command=get_completion, font=("Arial", 12), bg="lightblue")
submit_btn.pack(pady=10)

tk.Label(root, text="Response:", font=("Arial", 12)).pack()

output_box = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD, font=("Arial", 10), state=tk.DISABLED)
output_box.pack(padx=10, pady=5, fill=tk.BOTH)

root.mainloop()
