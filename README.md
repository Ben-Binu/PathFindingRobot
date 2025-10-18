# 🤖 Path Planning Robot using A* Algorithm

This project demonstrates a **path planning robot simulation** built entirely in Python 🐍 using the **A\*** (A-Star) algorithm.  
It finds the optimal path from a start to a goal point on a grid while avoiding obstacles — similar to how autonomous robots navigate their environment.

---

## 🚀 Features

- Implements the **A\*** algorithm for efficient path planning  
- Visualizes the maze, obstacles, start and goal points, and the computed path  
- Simple and easy-to-understand implementation (great for learning!)  
- No external frameworks — just Python, NumPy, and Matplotlib  
- Fully customizable grid and obstacle setup  

---

## 🧩 Tech Stack

- **Language:** Python 3  
- **Libraries Used:**
  - `numpy` – for handling the maze grid  
  - `heapq` – for priority queue operations (A* open list)  
  - `matplotlib` – for visualizing the maze and path  

---

## 🧠 Algorithm Overview

The **A\*** algorithm is used for finding the shortest path between two points on a grid.  
It combines:
- **G(n):** The cost to reach a node  
- **H(n):** The heuristic (Manhattan distance in this case)  
- **F(n) = G(n) + H(n):** The total estimated cost  

This ensures that the robot finds the shortest and most efficient route to the goal 🚗💨

---

## 🛠️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ben-Binu/path-planning-robot.git
   cd path-planning-robot
