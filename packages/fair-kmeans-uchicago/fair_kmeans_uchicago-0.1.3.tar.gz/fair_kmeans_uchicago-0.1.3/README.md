# **Fair K-Means Clustering**

**Ensuring demographic fairness in K-Means clustering with AI-driven adjustments.**

## **📌 Overview**

Fair K-Means is an enhanced clustering algorithm that incorporates **fairness constraints** to ensure proportional representation of **protected demographic groups** in cluster assignments. By leveraging **external fairness distributions** (via OpenAI API), this approach ensures **balanced and unbiased clustering** while maintaining clustering quality.

## **🚀 Installation**

Install the package from PyPI:

```bash
pip install fair-kmeans-uchicago
```

## **🛠 Usage**

Import and apply **Fair K-Means Clustering** to your dataset:

```python
from fair_kmeans import fair_kmeans

# Apply Fair K-Means on dataset
df, fairness_metrics = fair_kmeans(data, n_clusters=3, protected_col="gender")

# View fairness results
print(fairness_metrics)
```

---

## **🔹 How It Works**

### **1️⃣ Standard K-Means Clustering**

- **Cluster Assignment:** Assigns data points to the nearest centroid.
- **Centroid Update:** Updates centroids by averaging assigned points.
- **Convergence:** Stops iterating when centroids stabilize.

### **2️⃣ Fairness Constraints**

- Ensures the **distribution of protected attributes** (e.g., race, gender) in each cluster aligns with an expected **fairness distribution**.
- Retrieves fairness constraints dynamically via **OpenAI API**.

### **3️⃣ Fairness-Aware Adjustments**

- Identifies clusters where demographic representation **deviates from expected proportions**.
- Reassigns individuals from **overrepresented to underrepresented clusters**.
- Maintains clustering quality using **Silhouette Score** as a regulatory measure.

---

## **📊 Evaluation Metrics**

### **✔ Fairness Score Computation**

Fairness is measured as the **absolute deviation** between actual and expected demographic proportions:

```
Fairness Score = | Actual Proportion - Expected Proportion |
```

A **lower fairness score** indicates a **better-aligned demographic distribution**.

### **✔ Silhouette Score**

- Measures how well-separated and cohesive clusters are.
- Used to **prevent significant loss of clustering quality** during fairness adjustments.

---

## **🔹 Key Features**

✅ **Bias Mitigation:** Ensures fair representation across all clusters.\
✅ **Data-Driven Fairness:** Uses external fairness benchmarks instead of assuming equal distribution.\
✅ **Scalability:** Can handle large datasets efficiently.\
✅ **Interpretability:** Outputs **fairness scores** alongside clustering results.\
✅ **Regulatory Compliance:** Supports fair AI governance (GDPR, Equal Credit Opportunity Act).

---

## **📌 Limitations**

⚠ **Computational Overhead:** Fairness adjustments increase processing time.\
⚠ **Dependency on Fairness Data:** External fairness constraints (via OpenAI API) may introduce bias.\
⚠ **Potential Impact on Clustering Quality:** Enforcing fairness may slightly reduce clustering compactness.

---

## **💡 Applications**

- **📊 Customer Segmentation** – Fair clustering in marketing & consumer analytics.
- **📑 Hiring & Recruitment** – Ensures diverse and unbiased hiring pools.
- **🏦 Fair Credit Scoring** – Reduces demographic bias in financial decision-making.
- **🎓 University Admissions** – Promotes equitable student representation.
- **🚔 Predictive Policing** – Ensures fairness in criminal justice analytics.

---

## **📄 Citation & References**

If you use this package in your research, please cite it as:

```
@article{fairkmeans2024,
  title={Fair K-Means Clustering},
  author={ASR, AV, RV},
  journal={PyPI},
  year={2024}
}
```

For further details, refer to:

- Ghadiri et al., 2020 - "Socially Fair K-Means Clustering"
- Bateni et al., 2024 - "Individually Fair K-Means Clustering"

---

## **📬 Contact & Support**

For questions, issues, or contributions, visit our **GitHub repository**:\
🔗 [GitHub Repository](https://github.com/yourusername/fair_kmeans)\

---

**Fair K-Means: Where AI Meets Ethical Clustering! 🚀**

