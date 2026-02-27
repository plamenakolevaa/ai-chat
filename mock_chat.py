import tkinter as tk

# ====== Fake AI logic ======
def fake_ai_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great 😄"
    elif "italy" in user_input:
        return "The capital of Italy is Rome."
    elif "bye" in user_input:
        return "Goodbye! 👋"
    else:
        return "Hmm... I’m not sure, but tell me more!"

# ====== Chat function ======
def send_message(event=None):  # allow Enter key
    user_input = entry.get()
    if not user_input.strip():
        return

    # Show user message
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_input + "\n")

    # Get fake AI response
    ai_response = fake_ai_response(user_input)

    # Show AI response
    chat_box.insert(tk.END, "AI: " + ai_response + "\n\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)  # scroll to bottom

    # Clear input
    entry.delete(0, tk.END)
    entry.focus()

# ====== UI Setup ======
window = tk.Tk()
window.title("Mock AI Chat")
window.configure(bg="#f0f0f0")  # light gray background

# Chat box
chat_box = tk.Text(window, height=20, width=60, state=tk.DISABLED,
                   bg="#ffffff", fg="#000000", font=("Arial", 12), bd=2, relief="sunken")
chat_box.pack(padx=10, pady=10)

# Frame around entry and send button
input_frame = tk.Frame(window, bg="#f0f0f0")
input_frame.pack(padx=10, pady=5, fill=tk.X)

# Entry field with color and padding
entry = tk.Entry(input_frame, width=40, font=("Arial", 14),
                 bd=2, relief="sunken", bg="#e0f7ff", fg="#000000")
entry.pack(side=tk.LEFT, padx=(0,5), pady=5, fill=tk.X, expand=True)
entry.focus()

# Send button
send_button = tk.Button(input_frame,
                        text="Send",
                        command=send_message,
                        font=("Arial", 14, "bold"),
                        bg="#4caf50",
                        fg="white",
                        bd=0,
                        relief="ridge",
                        padx=25,
                        pady=10,
                        highlightthickness=0)
send_button.pack(side=tk.RIGHT, pady=5)

# Bind Enter key
entry.bind("<Return>", send_message)

# Ensure entry keeps focus
window.after(100, lambda: entry.focus())

window.mainloop()