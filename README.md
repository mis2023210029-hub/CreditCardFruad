# Credit Card Fraud Detection Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)
![Pandas](https://img.shields.io/badge/Library-Pandas-red.svg)

## Abstract
Credit card fraud is a significant global issue, resulting in billions of dollars in losses annually. This project proposes a machine learning-based approach to identify patterns indicative of fraudulent transactions. By training models on historical transaction data and evaluating them on unseen datasets, we aim to provide a robust solution for financial security.

**Keywords:** Credit Card Fraud Detection, K-Nearest Neighbors, Support Vector Machine, Logistic Regression, Decision Tree.

## Overview
With the number of credit card users reaching 2.8 billion worldwide, the security of digital transactions is more critical than ever. Reports of identity theft and fraudulent account usage rose significantly between 2019 and 2021. This project is motivated by the need to resolve these issues analytically, using different machine learning methods to detect fraud within large volumes of transaction data.

## Project Goals
The primary objective is to detect fraudulent transactions to ensure customers are not charged for unauthorized purchases. 
* Implement multiple ML techniques (KNN, SVM, Logistic Regression, Decision Tree).
* Compare model performance using accuracy, precision, and recall.
* Visualize the results through graphs to identify the most effective model.

## Data Source
The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset/data).
* **Format:** CSV (AIML Dataset.csv)
* **Attributes:** Includes transaction features such as `step`, `type`, `amount`, `oldbalanceOrg`, `newbalanceOrig`.
* **Target Variable:** `isFraud` (1 for fraudulent, 0 for legitimate).

## Algorithms Implemented
This project evaluates the following machine learning models:
1. **Logistic Regression (L.R.)** - Baseline linear classification.
2. **K-Nearest Neighbor (KNN)** - Instance-based learning.
3. **Decision Tree (D.T.)** - Rule-based classification.
4. **Support Vector Machine (SVM)** - High-dimensional space classification.

## Installation & Setup
To run this project locally, ensure you have your virtual environment activated and the required libraries installed:

```bash
# Clone the repository
git clone <your-repo-link>

# Install dependencies
pip install pandas scikit-learn matplotlib seaborn