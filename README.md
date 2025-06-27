# Water Quality Prediction 

This is an ongoing project where I’m working on predicting multiple water quality parameters using machine learning. The approach uses a RandomForestRegressor wrapped with MultiOutputRegressor. It is being developed as part of a one-month **AICTE 4-Week Virtual Internship sponsored by Shell** in **June 2025**.



## 1. Project Motivation

Access to clean water is a critical global concern. Being able to forecast several water-quality metrics simultaneously helps flag contamination early and supports quicker remediation.



## 2. What I Did

| Stage          | Highlights                                                                                         |
| -------------- | -------------------------------------------------------------------------------------------------- |
| **Data**       | Gathered and cleaned real-world water-quality measurements.                                        |
| **Model**      | Implemented a multi-target regression pipeline (`MultiOutputRegressor` + `RandomForestRegressor`). |
| **Evaluation** | Assessed performance with **R²** and **MSE** for each target variable.                             |


## 3. Tech Stack

- **Python 3.12**
- **Pandas & NumPy** – data handling
- **Scikit-learn** – modelling + metrics
- **Matplotlib, Seaborn** – visualization
- **Colab Notebook** – experimentation environment



## 4. Target Variables Predicted

The model predicts multiple water quality parameters such as:

- NH4
- BOD5 (BSK5)
- Colloids
- O2, NO3, NO2, SO4, PO4 
- CL


## 5. Model Performance

The model achieved acceptable R² scores and low MSE across all targets (see notebook for detailed numbers).


## 6. Trained Model Link

-- https://drive.google.com/file/d/1bAC5j0R9WqCy_1aLlFiI5omxTudTRcQA/view?usp=drive_link


## 7. Internship Context

| Item          | Details                                       |
| ------------- | --------------------------------------------- |
| **Programme** | AICTE Virtual Internship – Edunet Foundation  |
| **Sponsor**   | Shell                                         |
| **Duration**  | June 2025 (1 month)                           |
| **Focus**     | Machine Learning for Environmental Monitoring |

---
