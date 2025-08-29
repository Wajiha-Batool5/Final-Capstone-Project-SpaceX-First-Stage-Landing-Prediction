# SpaceX Falcon 9 First Stage Landing Prediction

## Overview

This project aims to predict the success of SpaceX Falcon 9 first stage landings using publicly available data and machine learning techniques. By analyzing historical launch records, we identify key factors influencing landing outcomes and build predictive models to estimate the likelihood of successful landings. The project also provides interactive visualizations and dashboards for data exploration and insight generation.

---

## Table of Contents

- [Background](#background)
- [Objectives](#objectives)
- [Methodology](#methodology)
  - [Data Collection](#data-collection)
  - [Data Wrangling](#data-wrangling)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Interactive Visual Analytics](#interactive-visual-analytics)
  - [Predictive Modeling](#predictive-modeling)
- [Project Structure](#project-structure)
- [Usage Instructions](#usage-instructions)
- [Results & Insights](#results--insights)
- [Dependencies](#dependencies)
- [License](#license)
- [Contact](#contact)

---

## Background

SpaceX has revolutionized commercial spaceflight by reusing rocket stages, significantly reducing launch costs. Predicting the success of first stage landings is crucial for cost estimation and mission planning. This project leverages SpaceX API data, Wikipedia records, and advanced analytics to answer:

- How do payload mass, launch site, number of flights, and orbit affect landing success?
- Has the success rate improved over time?
- Which machine learning algorithm best predicts landing outcomes?

---

## Objectives

- **Data Acquisition:** Gather comprehensive launch data from SpaceX API and Wikipedia.
- **Data Preparation:** Clean, transform, and encode data for analysis and modeling.
- **EDA:** Visualize and quantify relationships between features and landing success.
- **Interactive Analytics:** Build dashboards and maps for dynamic data exploration.
- **Modeling:** Develop, tune, and evaluate classification models to predict landing outcomes.
- **Reporting:** Summarize findings and recommend the optimal predictive approach.

---

## Methodology

### Data Collection

- **SpaceX REST API:** Automated retrieval of launch details, rocket specifications, payloads, and landing outcomes.
- **Web Scraping:** Extraction of supplementary launch records from Wikipedia using BeautifulSoup.

### Data Wrangling

- Data cleaning: Removal of duplicates, handling of missing values, and correction of inconsistencies.
- Feature engineering: Extraction and transformation of relevant features (e.g., payload mass, launch site, orbit).
- One-hot encoding: Conversion of categorical variables for machine learning compatibility.

### Exploratory Data Analysis (EDA)

- Statistical summaries and distribution analysis.
- Visualization of feature relationships using Matplotlib, Seaborn, and Plotly.
- Temporal analysis of landing success rates.

### Interactive Visual Analytics

- **Folium Maps:** Geospatial visualization of launch sites and outcomes.
- **Plotly Dash:** Interactive dashboard for filtering, exploring, and visualizing launch data and model predictions.

### Predictive Modeling

- Model development: Logistic Regression, Decision Tree, Support Vector Machine (SVM), and K-Nearest Neighbors (KNN).
- Hyperparameter tuning using GridSearchCV.
- Model evaluation: Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.
- Comparative analysis to identify the best-performing algorithm.

---

## Project Structure

```
├── dataset_part_1.csv           # Cleaned and structured launch data
├── dataset_part_2.csv           # Data with landing outcome classification
├── dataset_part_3.csv           # One-hot encoded features for modeling
├── spacex_web_scraped.csv       # Wikipedia-scraped launch records
├── SpaceX.ipynb                 # Jupyter notebook: data pipeline, EDA, modeling
├── spacex_dash_app.py           # Plotly Dash dashboard application
├── README.md                    # Project documentation
```

---

## Usage Instructions

### 1. Install Dependencies

```bash
pip install pandas dash plotly seaborn matplotlib scikit-learn beautifulsoup4 requests folium
```

### 2. Run the Interactive Dashboard

```bash
python spacex_dash_app.py
```
- Access the dashboard at [http://127.0.0.1:8050/](http://127.0.0.1:8050/).

### 3. Explore the Jupyter Notebook

- Open `SpaceX.ipynb` in Jupyter Notebook or VS Code to review the full data pipeline, analysis, and modeling steps.

---

## Results & Insights

- **Feature Impact:** Payload mass, launch site, number of flights, and orbit type significantly influence landing success.
- **Temporal Trends:** Success rates have increased over the years, reflecting technological improvements.
- **Model Performance:** Multiple algorithms were evaluated; the best-performing model is highlighted in the final report based on accuracy and F1-score.
- **Visualization:** Interactive dashboards and maps enable dynamic exploration of launch data and model predictions.

---

## Dependencies

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- dash
- scikit-learn
- beautifulsoup4
- requests
- folium

---

## Contact

For questions or collaboration, please contact:

- **Author:** Wajiha Batool
