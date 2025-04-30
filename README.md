<p align="center">
   <a href="https://dm-project-abcdeats-group37.streamlit.app/">
        <img src="./static/ABCDEats_Banner.png" alt="ABCDEats Banner" width="800">
    </a>
</p>

# 🍕 ABCDEats Inc. - Data Mining Project Dashboard 🚀 ([Live App](https://dm-project-abcdeats-group37.streamlit.app/))

This repository contains the Streamlit web application developed as the ***optional deployment part*** of the **Data Mining** project for the Master's in Data Science and Advanced Analytics at NOVA Information Management School (NOVA IMS).

<br>

## 🔗 Relation to Main Project

This dashboard visualizes the Exploratory Data Analysis (EDA) and Customer Segmentation findings from our comprehensive Data Mining project on ABCDEats Inc. The main project, including data preprocessing, clustering analysis, and detailed reports, can be found in the primary repository:

➡️ **Main Project Repository:** [Silvestre17/DM_24.25_Project](https://github.com/Silvestre17/DM_24.25_Project) ⬅️

<br>

#### 👥 Group 37

-   André Silvestre, 20240502
-   Filipa Pereira, 20240509
-   Umeima Mahomed, 20240543

<br>

## 📍 Dashboard Overview

This interactive application provides a user-friendly platform designed to empower stakeholders at ABCDEats Inc. It facilitates the exploration of customer data and the analysis of segmentation results. Key features include:

1.  **Interactive EDA Visualizations:** Presents key insights from the initial data exploration (**Part 1** of the main project) through dynamic charts and graphs (time series, histograms, scatter plots, sunburst charts, etc.). Facilitates easy interpretation of complex data trends and distributions.
2.  **Customer Segment Exploration:** Allows users to delve into the characteristics of the final customer segments derived from the clustering analysis (**Part 2** of the main project). Visualizes segment profiles and compositions based on various metrics.
3.  **Dynamic Filtering:** Enables users to apply multiple filters (e.g., cuisine preference, order day/time, region, age group, payment method, promo usage) to the dataset and observe their impact on both EDA plots and segment distributions in real-time.

<br>

## 🛠️ Technology Stack

This dashboard leverages the following Python libraries:

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>
  <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" /></a>
  <a href="https://www.streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" /></a>
  <a href="https://www.plotly.com/"><img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" /></a>
  <a href="https://www.numpy.org/"><img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" /></a>
  <a href="https://www.Scikit-Learn.org/"><img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" /></a>
  <a href="https://www.matplotlib.org/"><img src="https://img.shields.io/badge/Matplotlib-D3D3D3?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib" /></a>
  <a href="https://www.seaborn.pydata.org/"><img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn" /></a>
</p>

<br>

## 💻 Dashboard Setup Locally

To run this dashboard on your local machine, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Silvestre17/DM_Dashboard_Group37.git
    cd DM_Dashboard_Group37
    ```
2.  **Install the required libraries:** Make sure you have Python and pip installed. It's recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: The `requirements.txt` file lists all necessary dependencies.)*

3.  **Run the Streamlit application:**
    ```bash
    streamlit run dmproject_group37_streamlit.py
    ```
4.  **Access the dashboard:** Open your web browser and navigate to the local URL provided in the terminal (usually `http://localhost:8501`).

5.  Enjoy exploring the data! 🎉


---
