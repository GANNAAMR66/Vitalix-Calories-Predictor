#  **Calories Burn Prediction System**

### **AI-Powered Calorie Burn Prediction Using Machine Learning**

---

##  **Developer Information**

* **Name:** Ganna Amr Emad
* **Faculty:** Faculty of Artificial Intelligence
* **University:** Kafrelsheikh University

**Supervision:**

* **Dr.** Mahmoud Yassin
* **Eng.** Hassan Saad

---

##  **Project Overview**

The **Calories Burn Prediction System** is a desktop-based AI application designed to estimate the number of calories burned during physical activity.

The system utilizes a **Machine Learning regression model (XGBoost)** trained on physiological and activity-related data to provide **accurate, real-time predictions**.

The application is built with a **modern dark-themed graphical interface (GUI)** enhanced with gold accents to deliver a premium user experience.

---

##  **Objectives**

* Apply Machine Learning concepts in a real-world application
* Build a complete AI system from model training to deployment
* Design an intuitive and user-friendly interface
* Ensure reliable and accurate calorie prediction

---

##  **Key Features**

*  **High-Accuracy Prediction** using XGBoost Regressor
*  **User-Friendly GUI** built with Tkinter
*  **Real-Time Input Validation** for data accuracy
*  **Automatic Data Logging** in JSON format
*  **Robust Error Handling** for model loading and execution
*  **Professional Dark Theme UI** with modern styling

---

##  **Machine Learning Model**

### **Model Details**

* **Algorithm:** XGBoost Regressor
* **Task Type:** Regression
* **Library:** XGBoost

### **Training Information**

The model was trained using a dataset containing user physiological and activity data such as:

* Age
* Gender
* Height
* Weight
* Heart Rate
* Body Temperature
* Activity Duration

### **Evaluation Metrics**

* RMSE (Root Mean Square Error)
* R² Score

>  *Note: Performance may vary depending on dataset split and preprocessing.*

---

##  **Application Interface**

The application provides a clean and interactive interface where users can input their data and instantly receive calorie predictions.

### Features of the Interface:

* Smooth navigation between input fields
* Clear input structure
* Instant result display
* Error alerts for invalid data

---

##  **Input Parameters**

| Parameter  | Description                 |
| ---------- | --------------------------- |
| Gender     | 1 = Male, 0 = Female        |
| Age        | User age                    |
| Height     | In centimeters (cm)         |
| Weight     | In kilograms (kg)           |
| Duration   | Activity duration (minutes) |
| Heart Rate | Average heart rate          |
| Body Temp  | Body temperature            |

---

##  **Output**

* Predicted number of calories burned
* Automatically saved in:

```bash
gui_output.json
```

---

##  **Project Structure**

```text
Calories-Prediction-AI/
│
├── api/
│   └── main.py              # Main GUI application
│
├── model/
│   └── calories_model.json  # Trained ML model
│
├── assets/
│   ├──  json_outpu.jpg            # Screenshots
│   ├──  result.jpg.jpg             
|   └──  project_demo_video.mp4           # Demo video
│ 
├── gui_output.json          # Prediction logs
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```

---

##  **Installation & Setup**

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Calories-Prediction-AI.git
cd Calories-Prediction-AI
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python api/main.py
```
---
##  **Demo**

 A full demonstration video is available in:

```bash
assets/project_demo_video.mp4
```

---

##  **Use Case Example**

**Input:**

* Gender: Male
* Age: 25
* Height: 175 cm
* Weight: 70 kg
* Duration: 30 min
* Heart Rate: 120 bpm
* Body Temp: 37°C

![Result](assets/result.jpg)


**Output:**
 Predicted Calories Burned: *~230 kcal*

![JSON Output](assets/images/json_outpu.jpg)
د
---

##  **Academic Value**

This project demonstrates:

* Practical implementation of Machine Learning models
* Integration between AI and GUI development
* Real-world problem solving using data-driven approaches
* Software engineering best practices

---

##  **Error Handling & Robustness**

* Handles missing or corrupted model files
* Prevents invalid inputs
* Provides user-friendly error messages

---

##  **License**

This project is for **academic and educational purposes only**.

---

##  **Final Note**

This project represents a complete pipeline from **data processing → model training → deployment → user interaction**, reflecting strong skills in **Artificial Intelligence, Python development, and system design**.
