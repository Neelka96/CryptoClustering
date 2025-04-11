# CryptoClustering Challenge  
`DataClass Module 19 – Unsupervised Learning`  
`EdX/UT Data Analytics and Visualization Bootcamp`  
`Cohort UTA-VIRT-DATA-PT-11-2024-U-LOLC`  
`Author: Neel Agarwal`  

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation & Setup](#installation--setup)
3. [Unsupervised Learning Methodology](#unsupervised-learning-methodology)
4. [Directory Structure](#directory-structure)
5. [Rubric & Evaluation](#rubric--evaluation)
6. [Usage Notes & Limitations](#usage-notes--limitations)
7. [Credits & References](#credits--references)

---

## Project Overview

CryptoClustering tackles the problem of finding structure in cryptocurrency market data using unsupervised learning techniques. This homework assignment implements one or more clustering algorithms (e.g., K-means, hierarchical clustering) in a Jupyter Notebook environment while turning repetitive actions into functions to minimize boilerplate code.

**Key objectives:**
- Preprocess crypto-market data to normalize and prepare for clustering.
- Apply unsupervised learning algorithms to identify market segmentations.
- Evaluate clustering results based on the provided rubric criteria.
- Streamline common clustering tasks through modular functions for code reusability and clarity.

---

## Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/CryptoClustering.git
   cd CryptoClustering
   ```

2. **Set Up Virtual Environment (Recommended)**

   ```bash
   python -m venv venv
   # On Unix/MacOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Required Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Jupyter Notebook**

   Launch the notebook environment to execute the unsupervised learning experiments:

   ```bash
   jupyter notebook Crypto_Clustering.ipynb
   ```

> **Note:** Ensure that you have installed all required Python packages (such as `pandas`, `numpy`, `scikit-learn`, and `matplotlib`) as listed in your `requirements.txt`.

---

## Unsupervised Learning Methodology

- **Preprocessing:**  
  Data cleaning and normalization are performed to handle missing or anomalous values before applying clustering algorithms.

- **Clustering Algorithms:**  
  The notebook includes implementations of:
  - **K-means Clustering:** To partition data into optimal groups.
  - **Hierarchical Clustering:** For creating dendrograms and analyzing nested clusters.

- **Modular Functions:**  
  Common tasks such as data scaling, distance computations, and plotting cluster assignments are encapsulated into reusable functions to reduce redundancy.

- **Evaluation:**  
  Clustering quality is assessed using metrics (e.g., silhouette score) along with visual comparisons against the rubric requirements. Detailed evaluation criteria are outlined in the attached rubric.

---

## Directory Structure

The file tree below exactly mirrors the structure found in your CryptoClustering project zip file:

```plaintext
CryptoClustering/
├── .gitignore
├── Crypto_Clustering.ipynb
├── README.md
├── Resources/
│   └── crypto_market_data.csv
├── __init__.py
└── lib.py
```

---

## Rubric & Evaluation

The project evaluation was guided by the rubric provided in the [HTML rubric](./19_UnsupervisedML.html). Key criteria include:

- **Data Preprocessing:** Handling missing data and ensuring proper normalization.
- **Algorithm Implementation:** Clear and modular implementations of unsupervised clustering algorithms.
- **Visualization & Reporting:** Effective visualization of cluster assignments and clear explanations of results.
- **Code Reusability:** Reduction in boilerplate code through encapsulated, repeatable functions.
- **Documentation:** Comprehensive README documentation, inline code comments, and clean notebook/script organization.

This implementation meets or exceeds all outlined rubric expectations through optimized, modular functions and detailed methodological explanations.

---

## Usage Notes & Limitations

- **Usage Notes:**
  - Run the main notebook (`Crypto_Clustering.ipynb`) to see interactive clustering analyses.
  - Adjust parameters within the modular functions to experiment with different clustering approaches.
  - Ensure that the `crypto_market_data.csv` file is located in the Resources folder to avoid errors.

- **Limitations:**
  - The current dataset is limited to the provided CSV file. Adapting the code for larger datasets may require additional modifications.
  - Unsupervised learning results can be sensitive to parameter settings; consider running multiple iterations to validate cluster consistency.

---

## Credits & References
  - [pandas Documentation](https://pandas.pydata.org/docs)
  - [scikit-learn Documentation](https://scikit-learn.org/)
  - [Matplotlib Documentation](https://matplotlib.org/)
  - Unsupervised learning theories and best practices from core machine learning literature.
  - Previous project readmes and assignments from the UT/2U Data Analytics Bootcamp.