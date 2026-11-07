# Product Entity Resolution: Amazon vs Google

An end-to-end machine learning pipeline that finds which product records in two catalogs (Amazon and Google) refer to the same real-world product, even though the records share no common ID and differ in naming, formatting and completeness.

> **Status:** In progress. Steps 1-8 build the core pipeline, steps 9-11 package and present it. See the [Roadmap](#roadmap).

---

## Problem

Product data arrives from independent sources. The same product can appear as:

- `adobe photoshop cs3 for windows` in one catalog
- `photoshop cs3 win (adobe systems)` in another

Without a shared identifier, matching these records is **Entity Resolution (ER)**. Unlinked or duplicated records hurt price comparison, search quality and analytics.

**Task:** given an Amazon table and a Google table, predict the set of matching record pairs.

## Why this is hard

- Inconsistent names, abbreviations and word order
- Missing fields (the manufacturer is often absent)
- Long, noisy product descriptions
- One record can match several records, or none
- Comparing every pair is too slow (about 1,300 x 3,200 = 4M+ pairs for this small dataset, and it grows quadratically)

## Dataset

[Amazon-Google Products](https://dbs.uni-leipzig.de/research/projects/benchmark-datasets-for-entity-resolution) from the Database Group, University of Leipzig.

| File | Description |
|---|---|
| `Amazon.csv` | Amazon product records |
| `GoogleProducts.csv` | Google product records |
| `Amzon_GoogleProducts_perfectMapping.csv` | Ground-truth matching pairs |

Raw data is not committed to this repo. See [`data/raw/README.md`](data/raw/README.md) for download instructions.

## Approach

```
Raw data -> Cleaning -> Normalization -> Blocking -> Pair features -> Model -> Threshold tuning -> Matches
```

1. **Cleaning:** remove HTML, punctuation and extra whitespace, fix encoding, handle missing values.
2. **Normalization:** standardize abbreviations, extract brands, model numbers and versions.
3. **Blocking:** TF-IDF character n-gram nearest neighbours to generate a small set of candidate pairs.
4. **Pair features:** Jaccard, Jaro-Winkler, token-set ratio, TF-IDF cosine, model-number match, brand match, price difference.
5. **Model:** logistic regression baseline, then LightGBM.
6. **Threshold tuning:** choose the decision threshold that maximizes F0.5.

## Evaluation

The metric is **F0.5**, which weights precision twice as much as recall, because wrongly merging two different products is worse than missing a link.

```
F0.5 = (1.25 x Precision x Recall) / (0.25 x Precision + Recall)
```

Blocking is evaluated separately with **recall** (how many true matches survive) and **reduction ratio** (how many comparisons are avoided).

## Results

*To be filled in as the project progresses.*

| Method | Precision | Recall | F0.5 |
|---|---|---|---|
| Exact match on cleaned name | - | - | - |
| Fuzzy name match | - | - | - |
| Logistic regression | - | - | - |
| LightGBM | - | - | - |

Blocking recall: -  |  Reduction ratio: -

## Project structure

```
product-entity-resolution/
├── data/
│   ├── raw/            # original files (not committed)
│   ├── interim/        # cleaned data
│   └── processed/      # candidate pairs and features
├── notebooks/          # exploration and experiments
├── src/                # reusable pipeline code
├── models/             # trained models (not committed)
├── reports/figures/    # charts used in this README
├── app/                # Streamlit demo
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone <https://github.com/Nutan30/Product-Entity-Resolution>
cd product-entity-resolution

python -m venv venv
venv\Scripts\activate        # Windows (cmd)
# source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

Download the dataset and place the three files in `data/raw/`.

## Roadmap

- [x] Step 1: Project setup and problem definition
- [ ] Step 2: Data understanding and EDA
- [ ] Step 3: Data cleaning
- [ ] Step 4: Normalization and feature extraction
- [ ] Step 5: Blocking (candidate generation)
- [ ] Step 6: Pair feature engineering
- [ ] Step 7: Model training
- [ ] Step 8: Threshold tuning, evaluation and error analysis
- [ ] Step 9: Pipeline packaging
- [ ] Step 10: Streamlit demo
- [ ] Step 11: Documentation and polish
- [ ] Extension: add the Febrl dataset for address normalization and matching

## Tech stack

Python, pandas, NumPy, scikit-learn, RapidFuzz, LightGBM, Matplotlib / Seaborn, Streamlit

## Author

**Nutan Shewale**

## License

MIT