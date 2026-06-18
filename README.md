# Bioinformatics — Programming Homework, Fall 2024

> Course assignments for the **Bioinformatics** course at Sharif University of Technology, Fall 2024.  
> **Author:** Nasim Javdani · [GitHub](https://github.com/javdaninasim) · [LinkedIn](https://linkedin.com/in/nasim-javdani-810a9932a)

---

## Overview

This repository contains three programming homework assignments covering fundamental bioinformatics algorithms, implemented in Python. The assignments span sequence alignment, phylogenetic tree construction, and biological database querying.

---


## Assignments

### `SequenceAlignment_Fall_2024/` — Sequence Alignment
Implementation of pairwise sequence alignment algorithms:
- **Needleman-Wunsch**: global alignment using dynamic programming
- **Smith-Waterman**: local alignment for finding conserved regions
- Custom scoring matrices (match, mismatch, gap penalty)
- Alignment visualization and score analysis

### `NeighborJoining_Fall_2024/` — Neighbor Joining
Distance-based phylogenetic tree construction:
- Computation of pairwise distance matrices from aligned sequences
- Implementation of the Neighbor Joining (NJ) algorithm
- Tree visualization and interpretation of evolutionary relationships

---

## Technologies

| Tool | Purpose |
|---|---|
| Python 3 | Core programming language |
| Biopython | Biological sequence handling and database queries |
| NumPy | Numerical computation (distance matrices) |
| Matplotlib | Visualization of alignments and trees |

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/javdaninasim/BioInformatics_PHW_Fall-2024.git
   cd BioInformatics_PHW_Fall-2024
   ```
2. Install dependencies:
   ```bash
   pip install biopython numpy matplotlib jupyter
   ```
3. Open the relevant assignment folder and run the notebook or script.

---

## Course Info

- **Course:** Bioinformatics
- **Institution:** Sharif University of Technology, Department of Computer Engineering
- **Presenter:** Ali Sharifi Zarchi
- **Semester:** Fall 2024
