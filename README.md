# 🧠 Quiz Game (Anime & Manga Edition)
Welcome to the **Quiz Game**! This is a modular, object-oriented Command-Line Interface (CLI) trivia game built with Python. Test your knowledge of Japanese Anime & Manga with a series of True/False questions and track your score as you play.
---
## 🚀 Features
- **Object-Oriented Architecture:** Designed using clean OOP principles (separate models for questions and game logic).
- **Dynamic Scoring:** Real-time feedback on answers and automatic score updates after each question.
- **Extensible Question Bank:** Easily add or modify questions in the data store.
- **Interactive CLI:** Simple and clean user input validation.
---
## 📂 Project Structure
The project is structured logically into separate modules:
*   **[`main.py`](file:///C:/Users/Barkh/.gemini/antigravity/scratch/Quiz-Game/main.py):** The entry point of the application. It initializes the question bank, instantiates the game loop, and presents the final results.
*   **[`question_model.py`](file:///C:/Users/Barkh/.gemini/antigravity/scratch/Quiz-Game/question_model.py):** Contains the `Questions` class, which models individual quiz questions with text and answer attributes.
*   **[`quiz_brain.py`](file:///C:/Users/Barkh/.gemini/antigravity/scratch/Quiz-Game/quiz_brain.py):** Contains the `QuizBrain` class, which manages the quiz execution flow, checks user answers, updates scores, and tracks the current question index.
*   **[`data.py`](file:///C:/Users/Barkh/.gemini/antigravity/scratch/Quiz-Game/data.py):** The local database storing the anime and manga-themed True/False questions formatted as a list of dictionaries.
---
## 🛠️ Requirements
- **Python 3.x** installed on your system.
---
## 💻 Installation & Running
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Paras-cod/Quiz-Game.git
   cd Quiz-Game
   ```
2. **Run the game:**
   ```bash
   python main.py
   ```
---
## 🎮 Gameplay Preview
Here is an example of what the game looks like in your terminal:
```text
Q.1: In the "Toaru Kagaku no Railgun" anime, espers can only reach a maximum of level 6 in their abilities.(True/False): False
You got it right!
The correct answer is: False
The score is 1/1
Q.2: Clefairy was intended to be Ash's starting Pokémon in the pilot episode of the cartoon.(True/False): True
You got it right!
The correct answer is: True
The score is 2/2
...
You completed the quiz
The final score is: 8/10
```
---
## 📝 Extending the Quiz
Want to add your own questions? Just update the list in [`data.py`](file:///C:/Users/Barkh/.gemini/antigravity/scratch/Quiz-Game/data.py) using the following format:
```python
question_data = [
    {
        "question": "Your custom question text here.",
        "correct_answer": "True" # or "False"
    },
    # Add more dictionary objects as needed
]
```
---
## 👤 Author
*   **Paras Bansal**
    *   GitHub: [@Paras-cod](https://github.com/Paras-cod)
    *   Email: [parasbansl22@gmail.com](mailto:parasbansl22@gmail.com)
---
## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Paras-cod/Quiz-Game/issues).
