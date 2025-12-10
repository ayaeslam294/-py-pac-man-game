# 🎮 Pac-Man Mini AI

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
A simplified **Pac-Man game** developed in Python using **Pygame**, featuring **two ghost AI algorithms**: **BFS** and **Greedy**. This project demonstrates how different pathfinding algorithms behave in real-time.

---

## 🕹️ Game Overview

* **Player (Pac-Man) 🟡:** Moves with arrow keys. Collect dots to score points.
* **Ghosts:**

  * **Ghost 1 🔴 (BFS):** guarantees shortest path.
  * **Ghost 2 🟢 (Greedy):** moves towards Pac-Man using Manhattan distance.
* **Maze:** 7×7 grid with walls and dots.

---

## 🎯 Features

* Real-time ghost path visualization.
* Score tracking.
* Efficiency metrics for BFS and Greedy.
* Win/Lose state with stats display.

---

## ⚡ Demo 
<img width="480" height="270" alt="image" src="https://github.com/user-attachments/assets/8821f75a-109d-480b-992d-a08543031f79" />

```

## 🛠️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/pacman-mini-ai.git
```

2. Install dependencies:

```bash
pip install pygame
```

3. Make sure the images (`pacman.png`, `ghost1.png`, `ghost2.png`) are in the project folder.

4. Run the game:

```bash
python pacman.py
```

---

## 📊 AI Analysis

| Algorithm | Steps | Distance           | Efficiency |
| --------- | ----- | ------------------ | ---------- |
| BFS 🔴    | High  | Optimal            | Accurate   |
| Greedy 🟢 | Low   | Not always optimal | Fast       |

* **BFS 🔴**: Accurate, finds the shortest path.
* **Greedy 🟢**: Fast, may take longer paths

---

## 🎨 Colors Used in Game

* **Player:** 🟡 Yellow
* **Ghost BFS Path:** 🔴 Red
* **Ghost Greedy Path:** 🟢 Green
* **Walls:** 🔵 Blue
* **Dots:** ⚪ White



## 🔗 Links

* **Python**: [https://www.python.org/](https://www.python.org/)
* **Pygame**: [https://www.pygame.org/news](https://www.pygame.org/news)


## 📞 Contact

For questions or suggestions, please open an issue or contact:
**Aya Eslam Elsawy**
[LinkedIn](https://www.linkedin.com/in/aya-eslam-1b8792349) | [GitHub](https://github.com/ayaeslam294)
