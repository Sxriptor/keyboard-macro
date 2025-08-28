import keyboard
import tkinter as tk
from tkinter import ttk

active = False
hotkeys = []  # keep track of our own hotkeys

def toggle_macros():
    global active
    active = not active
    status.set("ON" if active else "OFF")
    rebind_keys()

def send_text(text):
    if active:
        keyboard.write(text)

def rebind_keys():
    global hotkeys
    # Remove only our own hotkeys
    for h in hotkeys:
        try:
            keyboard.remove_hotkey(h)
        except KeyError:
            pass
    hotkeys = []

    if active:
        # Macros mode: suppress numbers, type commands
        keymap = {
            "num 1": lambda: send_text("npm install"),
            "num 2": lambda: send_text("npm run build"),
            "num 3": lambda: send_text("npm start"),
            "num 4": lambda: send_text("npm run dev"),
            "num 7": lambda: send_text("git add ."),
            "num 8": lambda: send_text('git commit -m "message"'),
            "num 9": lambda: send_text("git push origin main"),
        }
        for key, action in keymap.items():
            h = keyboard.add_hotkey(key, action, suppress=True)
            hotkeys.append(h)

    # Always re-bind the toggle key (mapped to G1 in iCUE)
    h = keyboard.add_hotkey("ctrl+alt+g", toggle_macros, suppress=False)
    hotkeys.append(h)

# ---- GUI ----
root = tk.Tk()
root.title("Macro Toggle")
root.geometry("300x150")

status = tk.StringVar(value="OFF")

ttk.Label(root, text="Macro Status:").pack(pady=10)
ttk.Label(root, textvariable=status, font=("Arial", 16)).pack()
ttk.Button(root, text="Toggle Now (G1)", command=toggle_macros).pack(pady=10)

# Initial binding
rebind_keys()

root.mainloop()
