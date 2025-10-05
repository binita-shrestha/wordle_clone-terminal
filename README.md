# 🟩 Clone of Wordle in Python (Terminal Edition)

A fun, command-line implementation of the popular NYT **Wordle** game — built entirely in Python!  
Guess the hidden five-letter English word within six tries.  
After each guess, color-coded feedback helps you narrow down your options:

- 🟩 **Green** — correct letter in the correct position  
- 🟨 **Yellow** — correct letter but wrong position  
- ⬛ **Grey** — letter not in the word  

---

## Features

✅ 100% terminal-based — runs in any console  
✅ Uses **real English words** from the NLTK corpus  
✅ Handles **duplicate letters** correctly (just like real Wordle!)  
✅ Validates that guesses are **real English words**  
✅ Displays colorful feedback using `colorama`  

---

## How It Works

1. Loads a list of all valid **five-letter English words** from the NLTK corpus  
2. Randomly picks one as the **CHOSEN WORD**  
3. Prompts the user for guesses (must be valid 5-letter words)  
4. Gives visual hints for each letter:
   - 🟩 Green — right letter, right spot  
   - 🟨 Yellow — right letter, wrong spot  
   - ⬛ Grey — not in the word  
5. Ends when the user guesses correctly or uses all 6 attempts  

---

## Installation

Make sure you have **Python 3.8+** installed.  
Then install the required packages:

```bash
pip install nltk colorama
Download the word corpus once (only the first time):

```python
import nltk
nltk.download('words')

## Future Improvements

Here are a few ideas for expanding this project further:

- 🔁 **Replay option:** Let players start a new game without restarting the script  
- ⚙️ **Difficulty modes:** Allow 4-, 5-, and 6-letter words  
- 🧮 **Statistics:** Track number of wins, average guesses, and streaks  
- 🎨 **Enhanced UI:** Add a graphical interface (e.g., Tkinter or a web app)  
- 🌍 **Multilingual mode:** Support for different languages  
- 🔊 **Sound effects or animations:** Make the terminal experience more engaging  

## Inspiration

This project was inspired by the following tutorial:  

👉 [YouTube: Wordle in Python (Coding Tutorial)](https://www.youtube.com/watch?v=NCgN4qtbh2Q)

The video helped shape the core logic and game flow.  
In addition, this project was **developed and refined with ChatGPT**,  
where I asked for detailed explanations of each concept and line of code.  
This approach helped deepen my understanding of Python programming  
and the logic behind building interactive terminal applications.
