# Macro Toggle Script

This script lets you turn your **numpad** into a quick command launcher for development tasks like `npm install`, `git add .`, etc.  
It uses Python’s [`keyboard`](https://pypi.org/project/keyboard/) library for hotkeys and `tkinter` for a small toggle GUI.

---

## Features

### Toggle Macros
Press **Ctrl + Alt + G** (or click the button in the window) to enable/disable macros.

### Mapped Commands
When enabled, numpad keys send dev commands instead of numbers:

- **Num 1** → `npm install`  
- **Num 2** → `npm run build`  
- **Num 3** → `npm start`  
- **Num 4** → `npm run dev`  
- **Num 7** → `git add .`  
- **Num 8** → `git commit -m "message"`  
- **Num 9** → `git push origin main`  

### Safe Toggle
Disabling returns your numpad to normal behavior.

---

## Requirements

- Python 3.8+  
- Install dependencies:  
  ```bash
  pip install keyboard
