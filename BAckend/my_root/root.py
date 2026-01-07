import tkinter as tk
from collections import Counter
import re

def analyze_text():
    text = text_input.get("1.0", tk.END).lower()
    words = re.findall(r'\b\w+\b', text)
    freq = Counter(words)

    output.delete("1.0", tk.END)
    for word, count in freq.most_common():
        output.insert(tk.END, f"{word}: {count}\n")

# Main window
root = tk.Tk()
root.title("Word Frequency Analyzer")
root.geometry("500x400")
root.resizable(False, False)

# Title
tk.Label(root, text="Word Frequency Analyzer", font=("Arial", 14, "bold")).pack(pady=5)

# Text input
text_input = tk.Text(root, height=8, width=55)
text_input.pack(pady=5)

# Analyze button
tk.Button(root, text="Analyze", command=analyze_text).pack(pady=5)

# Output
output = tk.Text(root, height=10, width=55, font=("Consolas", 10))
output.pack(pady=5)

root.mainloop()
