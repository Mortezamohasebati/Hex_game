<div align="center">

<img src="assets/banner.svg" alt="HEX — AI Strategy Board Game" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-F5A623?style=flat-square)](LICENSE)
[![Algorithm](https://img.shields.io/badge/AI-Alpha--Beta%20Minimax-38B2FF?style=flat-square)]()
[![Board](https://img.shields.io/badge/Board-11%20×%2011-1a2840?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

</div>

---

## ♟ What is Hex?

**Hex** is a two-player abstract strategy game played on a rhombus-shaped board of hexagonal cells. First described by mathematician **Piet Hein** in 1942 and independently invented by **John Nash** in 1948, it is beloved for its elegant simplicity and deep strategic complexity.

> *"The first player who connects their two sides wins — and a draw is mathematically impossible."*

| Player | Symbol | Goal |
|--------|--------|------|
| Human | **X** (Amber) | Connect **Left ↔ Right** |
| AI    | **O** (Blue)  | Connect **Top ↕ Bottom** |

---

## ✨ Features

- 🧠 **Alpha-Beta Minimax AI** — depth-adaptive search with move ordering and pruning
- 📐 **Configurable Board Sizes** — 5×5, 7×7, 9×9, 11×11
- 🖥️ **Beautiful Web UI** — SVG hexagonal board with animated border stripes, glow effects, and win-path highlighting
- ⚡ **Fast Evaluation** — Dijkstra-based resistance distance heuristic (0-1 BFS shortest path)
- 🏆 **Score Tracking** — persistent win counters across multiple games
- 📜 **Move History Log** — full game record in the sidebar
- 🎯 **Smart Opening** — AI plays center on first move for optimal strategy

---

## 🚀 Quick Start

### Web Version (recommended)

Simply open `hex_game.html` in any modern browser — no installation required.

```bash
git clone https://github.com/Mortezamohasebati/Hex_game.git
cd Hex_game
open hex_game.html        # macOS
# or: start hex_game.html  (Windows)
# or: xdg-open hex_game.html (Linux)
```

### Python CLI Version

```bash
git clone https://github.com/Mortezamohasebati/Hex_game.git
cd Hex_game
python Hex__Game.py
```

**Requirements:** Python 3.8+ · No external dependencies

---

## 🎮 How to Play

```
 ← O connects top to bottom →

X   0 1 2 3 4 5 6 7 8     X
↕   O─────────────────O   ↕
↕ 0 │. . . . . . . . .│   ↕
↕ 1 │. . . . . . . . .│   ↕
↕ 2 │. . X . . . . . .│   ↕
↕ 3 │. . . O . . . . .│   ↕
↕ ...                      ↕
```

1. **Click** (web) or **type row column** (CLI) to place your stone
2. **First** to form an unbroken chain connecting your two borders **wins**
3. Stones can connect through shared edges — 6 neighbors per hex cell
4. **No draws possible** — one player must always win

### Strategic Tips

- 🎯 **Control the center** — the middle of the board gives maximum connectivity
- 🔗 **Build bridges** — two cells with a guaranteed connection gap are a virtual connection
- 🛡️ **Block opponent paths** — use the resistance distance to find critical cells
- ⚡ **Ladders and templates** — master classic Hex patterns for unstoppable threats

---

## 🤖 AI Algorithm

The AI uses a combination of classical game-tree search and graph-theory evaluation.

### Minimax with Alpha-Beta Pruning

```
minimax(board, depth, α, β, maximizing):
    if terminal or depth == 0: return evaluate(board)
    
    if maximizing (AI / O):
        best = -∞
        for each move in ordered_moves:
            board[move] = 'O'
            val = minimax(board, depth-1, α, β, False)
            best = max(best, val)
            α = max(α, val)
            if β ≤ α: break  ← prune!
        return best
    else: (symmetric for X)
```

| Board Size | Search Depth | Typical Think Time |
|---|---|---|
| 5 × 5  | 5 plies | < 0.1s |
| 7 × 7  | 3 plies | < 0.3s |
| 9 × 9  | 2 plies | < 0.5s |
| 11 × 11| 2 plies | < 1.0s |

### Resistance Distance Heuristic

The evaluation function computes the **virtual connection distance** for each player using a 0-1 Dijkstra shortest-path on the board graph:

```python
cost(cell) = 0  if cell belongs to player
             1  if cell is empty
             ∞  if cell belongs to opponent

score = distance(X, left→right) − distance(O, top→bottom)
```

A **positive score** means the AI (O) has a shorter path to victory. This heuristic is significantly stronger than simple piece-count evaluation.

### Win Detection

Uses **Depth-First Search (DFS)** from all source-side cells, checking connectivity to the target side. Time complexity: `O(n²)` per check.

---

## 📁 Project Structure

```
Hex_game/
├── hex_game.html          # ✨ Web UI — full game in a single file
├── Hex__Game.py           # 🐍 Original Python CLI implementation
├── assets/
│   └── banner.svg         # 🎨 Animated README banner
├── پروژه هوش مصنوعی.pdf  # 📄 Original AI project report (Persian)
├── پروژه هوش مصنوعی.docx # 📝 Original project document (Persian)
└── README.md
```

---

## 🧩 Technical Details

### Hex Board Geometry

Each cell has **6 neighbors** using axial hex coordinates:

```
Directions: (-1,0), (+1,0), (0,-1), (0,+1), (-1,+1), (+1,-1)
```

The board is a **parallelogram** (rhombus) shape — row `r`, column `c` offsets diagonally.

### SVG Rendering

The web UI renders hexagons as SVG `<polygon>` elements with pointy-top orientation:

```javascript
vertex(i) = center + radius × (cos(60°·i − 30°), sin(60°·i − 30°))
```

Border stripes for X (amber) and O (blue) follow the zig-zag outer edges of the board grid.

---

## 🛠️ Improvements Over Original

| Feature | Original CLI | New Web Version |
|---|---|---|
| Interface | Terminal text | SVG board with animations |
| Evaluation | Piece-count difference | Dijkstra resistance distance |
| Move ordering | None | Center-first (better pruning) |
| Opening strategy | None | Center capture |
| Win visualization | Text announcement | Glowing path highlight |
| Score tracking | None | Persistent session scores |
| Board sizes | Runtime input | 5×5 / 7×7 / 9×9 / 11×11 |
| AI depth | Fixed 3 | Adaptive by board size |

---

## 📚 References & Further Reading

- [Hex on Wikipedia](https://en.wikipedia.org/wiki/Hex_(board_game))
- [Piet Hein — Inventor of Hex](https://en.wikipedia.org/wiki/Piet_Hein_(scientist))
- [John Nash's Hex Strategy](https://www.cs.cmu.edu/~hde/hex/hexfaq/)
- [Virtual Connections in Hex](http://www.trmph.com/hex/strategy.html)
- [Resistance Distance Evaluation](https://webdocs.cs.ualberta.ca/~hayward/papers/)
- [Alpha-Beta Pruning — AIMA](https://aima.cs.berkeley.edu/)

---

## 🤝 Contributing

Contributions are warmly welcome! Ideas for improvement:

- 🔬 Monte Carlo Tree Search (MCTS) AI
- 🌐 Multiplayer over WebSocket
- 📱 Mobile-responsive layout
- 🎓 Tutorial / hint system
- 🔢 Board coordinates overlay
- 💾 Game save / load (PGN-like format)

```bash
# Fork, clone, branch, and PR
git checkout -b feature/mcts-ai
git commit -m "feat: Add MCTS AI with UCB1"
git push origin feature/mcts-ai
```

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

**Made with ♟ and 🧠 by [Morteza Mohasebati](https://github.com/Mortezamohasebati),  [Ali Abroudoust](https://github.com/luuucciiffeerr), [VAhid Seyyedy](https://github.com/vahidseyyedi) and  [Parsa Behjati](https://github.com/parsaB2004) **

*"In Hex, unlike Chess, there is always a winner — and always a lesson."*

</div>
