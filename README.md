
# MetaFlowScheduler

A customizable metaheuristic framework for solving multi-stage no-wait flowshop scheduling problems, based on real-world academic research.

## 🧩 Problem Overview

This project focuses on solving the **multi-stage no-wait flexible flowshop scheduling problem** (NWFSP), where jobs must pass through several machines in strict sequence, and no job can wait between stages. It's a classical NP-hard scheduling problem, often found in manufacturing, production, and logistics.

## 🎯 Objective

Minimize the **makespan** (total completion time) by assigning job sequences optimally across machines, using metaheuristic techniques such as:
- Particle Swarm Optimization (PSO)
- Genetic Algorithms (GA)
- Tabu Search (TS)

## 🛠 Features

- Modular solver design using the DEAP library
- Simulated benchmark job data
- Plotting of Gantt charts and convergence
- Configurable job instances and machine layouts

## 📁 Folder Structure

```
MetaFlowScheduler/
├── data/                # Simulated benchmark job data
├── notebooks/           # EDA, experimentation, and visualization
├── results/             # Logs, convergence plots, Gantt charts
├── src/                 # Core solver implementations
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 🚀 Getting Started

1. Clone the repo:
```bash
git clone https://github.com/mageed-ghaleb/MetaFlowScheduler.git
cd MetaFlowScheduler
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run a solver:
```bash
python src/run_pso_solver.py
```

## 📊 Visual Output

- Convergence plots of fitness over iterations
- Gantt chart visualizations of job schedules

## 👨‍💻 Author

Developed by Mageed Ghaleb – Co-Founder of MetaForge | Optimization & AI Specialist  
Based on peer-reviewed research in scheduling, metaheuristics, and industrial optimization.

## 📄 License

MIT License – Free to use with attribution.
