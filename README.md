<div align="center">

<h1 align="center">🧬 Bioinformatics — Fall 2024</h1>
<h3 align="center">Programming Homework Assignments | Sharif University of Technology</h3>


[**GitHub**](https://github.com/javdaninasim/BioInformatics_PHW_Fall-2024) &nbsp; ⬩ &nbsp; [**University**](https://sharif.edu/)

</div>

---

### 📚 Course Overview

```python
class Bioinformatics:
    def __init__(self):
        self.institution = "Sharif University of Technology"
        self.instructor = "Ali Sharifi Zarchi"
        self.semester = "Fall 2024"
        self.language = "Python"
        
    def topics_covered(self):
        return {
            "Sequence Alignment": ["Local alignment", "Semi-global alignment", "Dynamic programming"],
            "Phylogenetics": ["Distance-based methods", "Neighbor Joining algorithm", "Evolutionary trees"]
        }
    
    def mission(self):
        return "Implement core bioinformatics algorithms for sequence analysis and tree construction."
```

---

### 📂 Repository Structure

```
BioInformatics_PHW_Fall-2024/
│
├── 🔬 SequenceAlignment/
│   └── sequence_alignment.py          # Semi-global sequence alignment with traceback
│
└── 🌳 NeighborJoining/
    └── neighbor_joining.py             # Phylogenetic tree construction via distance matrix
```

---

### 🎓 Assignments

#### **1. Sequence Alignment** 🔬

**File:** `SequenceAlignment/sequence_alignment.py`

**Algorithm:** Semi-Global Sequence Alignment (Gotoh-style)
- Uses dynamic programming to compute optimal local-to-global alignment
- Finds the best alignment **ending at the last character of sequence 2** (semi-global)
- Implements traceback to reconstruct the actual alignment

**Key Parameters:**
- Match score: `+1`
- Mismatch penalty: `-2`
- Gap penalty: `-2`

**Scoring Logic:**
- Insertion (I): gap in sequence 1
- Deletion (D): gap in sequence 2
- Match (M): alignment or mismatch

**Input:** Two sequences (as strings)
**Output:**
- Alignment score
- Aligned sequence 1
- Aligned sequence 2

---

#### **2. Neighbor Joining** 🌳

**File:** `NeighborJoining/neighbor_joining.py`

**Algorithm:** Neighbor Joining Tree Construction
- Agglomerative clustering method that builds an unrooted phylogenetic tree
- Uses distance matrix to identify closest neighbors
- Recursively joins neighbors and recalculates distances

**Key Components:**
- **dist_prime calculation:** Uses formula `(n-2) * d[a,b] - total_dist[a] - total_dist[b]`
- **Branch length calculation:** 
  - `len_a = 0.5 * (d[a,b] + (total_dist[a] - total_dist[b]) / (n-2))`
  - `len_b = 0.5 * (d[a,b] - (total_dist[a] - total_dist[b]) / (n-2))`
- **Distance update:** For new node k: `d[k,x] = 0.5 * (d[a,x] + d[b,x] - d[a,b])`

**Input:** 
- Distance matrix (square symmetric matrix)
- Optional: sequence labels

**Output:**
- Tree structure as adjacency list with edge weights
- Formatted edge list: `node_a -> node_b: distance`

**Tree Representation:**
- Nodes represented by indices (original sequences 0 to n-1, internal nodes n to 2n-2)
- Edges stored as bidirectional connections with branch lengths

---

### ⚡ Tech Stack

<div align="left">
  <img src="https://img.shields.io/badge/Python-1A1A1A?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/Algorithms-1A1A1A?style=for-the-badge&logo=python&logoColor=2E86C1" alt="Algorithms" />
</div>

<br>

> **Core Concepts:** `Dynamic Programming` ⬩ `Sequence Alignment` ⬩ `Distance Matrices` ⬩ `Graph Algorithms` ⬩ `Tree Construction`

---

### 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/javdaninasim/BioInformatics_PHW_Fall-2024.git
cd BioInformatics_PHW_Fall-2024

# 2. Run Sequence Alignment
python SequenceAlignment/sequence_alignment.py
# Input: Two sequences (one per line)
# Example:
# AGGTCGA
# AGGTACA

# 3. Run Neighbor Joining
python NeighborJoining/neighbor_joining.py
# Input: 
#   Line 1: number of sequences (n)
#   Lines 2 to n+1: distance matrix (n x n)
```

---

### 💡 Algorithm Details

#### Sequence Alignment Scoring

```
Scoring Matrix Construction:
- For each cell (i,j):
  - Deletion:  score[i-1][j] + gap_penalty
  - Insertion: score[i][j-1] + gap_penalty  
  - Match:     score[i-1][j-1] + (match_penalty if seq1[i-1]==seq2[j-1] else mismatch_penalty)
  - Take maximum of three

Traceback from best score in last row of sequence 2 (semi-global)
```

#### Neighbor Joining Algorithm

```
1. Initialize: all sequences as separate nodes
2. While more than 2 nodes:
   a. Calculate dist_prime for all pairs
   b. Find minimum dist_prime pair (min_a, min_b)
   c. Calculate branch lengths for both nodes
   d. Create new internal node
   e. Update distance matrix for remaining sequences
   f. Recursively apply to smaller matrix
3. Connect final two nodes
```

---

### 🎯 Learning Objectives

- ✨ Understand **dynamic programming** for sequence alignment
- 🧬 Implement **semi-global alignment** algorithms with traceback
- 📊 Master **distance-based phylogenetic** tree construction
- 🔬 Learn **neighbor joining** algorithm for evolutionary analysis
- 💪 Build efficient implementations of classical bioinformatics algorithms

---

### ℹ️ Course Information

| Detail | Information |
| :--- | :--- |
| **Institution** | Sharif University of Technology, Dept. of Computer Engineering |
| **Instructor** | Dr. Ali Sharifi Zarchi |
| **Semester** | Fall 2024 |
| **Language** | Python |
| **Prerequisites** | Data Structures, Algorithms, Basic Biology |

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=800080&height=100&section=footer" width="100%"/>
</div>
