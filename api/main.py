import tkinter as tk
from tkinter import messagebox
import xgboost as xgb
import numpy as np
import json
import os


# --- 1. تحميل الموديل ذكاء اصطناعي ---
model = xgb.XGBRegressor()
model_filename = "calories_model.json"
model_loaded = False

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, model_filename)

if os.path.exists(model_path):
    try:
        # الطريقة الأولى: التحميل القياسي
        model.load_model(model_path)
        model_loaded = True
        print("✅ Model loaded successfully!")
    except Exception as e:
        print(f"⚠️ Standard load failed, trying Booster: {e}")
        try:
            # الطريقة الثانية: التحميل كمحرك (تجنب خطأ invalid map key)
            bst = xgb.Booster()
            bst.load_model(model_path)
            model._Booster = bst
            model_loaded = True
            print("✅ Loaded using Booster fallback!")
        except Exception as e2:
            print(f"❌ Critical Error: Both methods failed. {e2}")
            model_loaded = False
# --- 2. دالة التنبؤ ---
def predict_calories():
    # هذا السطر هو الحل! نخبر الدالة أن تستخدم المتغير الموجود في الأعلى
    global model_loaded 
    
    try:
        # جمع البيانات من الخانات السبعة
        data = [float(ent.get().strip()) for ent in entries]
        features = np.array([data])
    except ValueError:
        messagebox.showerror("Input Error", "Please ensure all fields contain valid numbers.")
        return

    # الآن سيعرف الكود ما هو model_loaded ولن يخرج خطأ الـ NameError
    if not model_loaded:
        messagebox.showerror("System Error", "The AI model is not loaded. Please check if 'calories_model.json' is in the folder.")
        return

    try:
        prediction = model.predict(features)[0]
        messagebox.showinfo("Prediction Complete", f"✨ Estimated Calories Burned: {prediction:.2f} kcal")
        
        # حفظ النتيجة في ملف خارجي كما هو مطلوب في مشروعك
        result = {"prediction": float(prediction), "status": "success"}
        with open('gui_output.json', 'w') as f:
            json.dump(result, f, indent=4)
            
    except Exception as e:
        messagebox.showerror("Prediction Error", f"Something went wrong: {e}")

# --- 3. بقية كود الواجهة (GUI) ---
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

root = tk.Tk()
root.title("Ganna | AI Premium Predictor")
root.geometry("480x750")
root.configure(bg="#1a1a1a")

logo_label = tk.Label(root, text="CALORIES PREDICTION", font=("Times New Roman", 24, "bold italic"), 
                    bg="#1a1a1a", fg="#d4af37", pady=30)
logo_label.pack()

frame = tk.Frame(root, bg="#1a1a1a")
frame.pack(pady=10)

labels_text = ["Gender (1:M, 0:F)", "Age", "Height (cm)", "Weight (kg)", 
               "Duration (min)", "Heart Rate", "Body Temp"]
entries = []

for text in labels_text:
    lbl = tk.Label(frame, text=text.upper(), fg="#a9a9a9", bg="#1a1a1a", 
                   font=("Verdana", 8, "bold"))
    lbl.pack(pady=(5, 0), anchor="w", padx=45)
    
    ent = tk.Entry(frame, font=("Segoe UI", 12), width=30, justify='center',
                   bg="#262626", fg="#d4af37", insertbackground='#d4af37', 
                   borderwidth=1, relief="flat", highlightthickness=1, 
                   highlightbackground="#404040", highlightcolor="#d4af37")
    ent.pack(pady=2, ipady=3)
    ent.insert(0, "0") 
    ent.bind("<Return>", focus_next_widget)
    entries.append(ent)

entries[-1].bind("<Return>", lambda event: predict_calories())

predict_btn = tk.Button(root, text="GET PREDICTION", command=predict_calories, 
                        bg="#d4af37", fg="#1a1a1a", font=("Arial", 11, "bold"),
                        width=25, pady=12, cursor="hand2", relief="flat")
predict_btn.pack(pady=25)

footer = tk.Label(root, text="PREMIUM AI ENGINE BY GANNA", 
                  bg="#1a1a1a", fg="#4d4d4d", font=("Arial", 7, "bold"))
footer.pack(side="bottom", pady=20)

root.mainloop()