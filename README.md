# 🧠 Medical Diagnosis Classifier – Magshimim Final Project (magshimim-final-project-dnn)

This project is a deep learning classifier built as part of my final project in the national cyber program, **Magshimim**. It aims to predict patient diagnoses based on medical test results using a deep neural network (DNN).

---

## 📋 Project Overview

The goal: classify patients' medical diagnoses using data from real-world anonymized test results.

The project focuses on:
- Data cleaning and preprocessing
- One-hot encoding of categorical variables
- Normalization and preparation for training
- Designing, training, and evaluating a deep neural network

---

## 🔍 What Works

- Functional DNN model using TensorFlow
- Training and evaluation completed  
- Visualization of accuracy/loss over epochs

---

## 🩺 Dataset – MIMIC-III

This project uses data from **MIMIC-III** (Medical Information Mart for Intensive Care), a freely available, anonymized dataset developed by the MIT Lab for Computational Physiology.

MIMIC-III includes detailed clinical data of over 40,000 critical care patients, such as:
- Lab test results
- Vital signs
- Diagnoses (ICD-9)
- Prescriptions
- Demographics

We focused on extracting relevant medical test results and diagnosis codes for training the model.

Due to the complexity and variability of real-world medical data, especially in critical care, the correlation between tests and diagnoses was not always strong – which affected the model’s performance.

Learn more about MIMIC-III: [https://mimic.physionet.org/](https://mimic.physionet.org/)

---

## 📉 Current Limitations

The model currently does **not reach high accuracy**.  
After analysis, it appears that:
- The test data lacks strong enough correlation with the target diagnoses  
- Some tests are too generic or inconsistent across samples  
- Even after tuning the model architecture and training parameters, performance remains limited  

Still, this challenge provided deep insight into working with medical data and understanding model behavior under imperfect conditions.

---

## ⚙️ Technologies Used

- Python
- Pandas  
- TensorFlow 
- NumPy, pandas, matplotlib  
- Jupyter Notebook  
- Git for version control  

---

## 💡 Lessons Learned

- Importance of data quality and feature selection  
- Hands-on experience with DNN design  
- How to analyze why models fail and what could be improved  
- How to work with real-world, messy datasets

---

## 🧪 Future Improvements

- Use a more structured medical dataset
- Try other ML models like decision trees or ensemble methods  

---

## 🎓 Project Info

This project was developed as my final project in **Magshimim**, the Israeli national cyber education program for high school students. It reflects my growing interest in machine learning, data science, and solving real-world problems using AI.This project was developed together with another team member.


