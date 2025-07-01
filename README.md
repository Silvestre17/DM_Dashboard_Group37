<p align="center">
   <a href="https://dm-project-abcdeats-group37.streamlit.app/">
        <img src="./static/ABCDEats_Banner.png" alt="ABCDEats Banner" width="800">
    </a>
</p>

# 🍕 ABCDEats Inc. - Data Mining Project Dashboard 🚀 ([Live App](https://dm-project-abcdeats-group37.streamlit.app/))

## 📝 Description

This repository contains the source code for the **interactive Streamlit web application** that serves as the deployment component for our main Data Mining project. This dashboard is designed to bring the project's findings to life, providing an intuitive interface to explore customer data and interact with the final segmentation model for **ABCDEats Inc**.

<p align="center">
    <!-- Project Links -->
    <a href="https://github.com/Silvestre17/DM_FoodDeliveryClustering_MasterProject"><img src="https://img.shields.io/badge/Project_Repo-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Repo"></a>
    <a href="https://dm-project-abcdeats-group37.streamlit.app/"><img src="https://img.shields.io/badge/Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Dashboard"></a>
    <a href="https://github.com/Silvestre17/DM_Dashboard_Group37"><img src="https://img.shields.io/badge/Dashboard_Repo-100000?style=for-the-badge&logo=github&logoColor=white" alt="Dashboard Code Repo"></a>
</p>

<br>

## 🔗 Relation to Main Project

This dashboard visualizes the Exploratory Data Analysis (EDA) and Customer Segmentation findings from our comprehensive Data Mining project on ABCDEats Inc. The main project, including data preprocessing, clustering analysis, and detailed reports, can be found in the primary repository:

➡️ **Main Project Repository:** [Silvestre17/DM_FoodDeliveryClustering_MasterProject](https://github.com/Silvestre17/DM_FoodDeliveryClustering_MasterProject) ⬅️

<br>

## 🎓 Project Context

This dashboard was developed as the final deployment phase for the **Data Mining** course in the **[Master's in Data Science and Advanced Analytics](https://www.novaims.unl.pt/en/education/programs/postgraduate-programs-and-master-degree-programs/master-degree-program-in-data-science-and-advanced-analytics-with-a-specialization-in-data-science/)** program at **NOVA IMS** (2024/2025).

## 🛠️ Technology Stack

This application was built entirely in Python, using a modern stack for creating interactive, data-driven web apps.

#### Core Stack
<p align="center">
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>
    <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" /></a>
    <a href="https://numpy.org/"><img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" /></a>
</p>

#### Visualization & Web App
<p align="center">
    <a href="https://www.streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" /></a>
    <a href="https://www.plotly.com/"><img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" /></a>
    <a href="https://www.matplotlib.org/"><img src="https://img.shields.io/badge/Matplotlib-D3D3D3?style=for-the-badge&logo=matplotlib&logoColor=black" alt="Matplotlib" /></a>
    <a href="https://www.seaborn.pydata.org/"><img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn" /></a>
</p>

---

## 📍 Dashboard Features

This application is designed to empower stakeholders at ABCDEats Inc. with self-service analytics capabilities.

*   **📊 Interactive EDA:** Dynamic charts and graphs (time series, histograms, sunburst charts) that visualize the key insights from our initial Exploratory Data Analysis.
*   **🧑‍🤝‍🧑 Customer Segment Explorer:** A dedicated section to deep-dive into the characteristics of the final 5 customer segments, visualizing their profiles and compositions.
*   **🎛️ Dynamic Filtering:** Users can apply multiple filters—such as cuisine preference, order time, region, or promo usage—to the dataset and see their impact on all visualizations in real-time.


## 🖥️ Live Application & Showcase

Explore the interactive dashboard live:

➡️ **[dm-project-abcdeats-group37.streamlit.app](https://dm-project-abcdeats-group37.streamlit.app/)** ⬅️

<p align="center">
   <a href="https://dm-project-abcdeats-group37.streamlit.app/">
      <img src="./img/Dashboard_Showcase.png" alt="ChatMeter Streamlit App Showcase" width="800">
   </a>
</p>

## 🚀 Local Setup & Deployment

To run this dashboard on your local machine, please follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Silvestre17/DM_Dashboard_Group37.git
    cd DM_Dashboard_Group37
    ```

2.  **Install Dependencies:**
    It is highly recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # .\venv\Scripts\activate  # On Windows

    # Install requirements
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit Application:**
    ```bash
    streamlit run dmproject_group37_streamlit.py
    ```

4.  **Access the Dashboard:**
    Open your web browser and navigate to the local URL provided in the terminal (usually `http://localhost:8501`). Enjoy exploring the data! 🎉

---

## 👥 Team Members (Group 37)

*   **André Silvestre** (20240502)
*   **Filipa Pereira** (20240509)
*   **Umeima Mahomed** (20240543)
