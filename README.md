# 🍅 Tomato Leaf Disease Classification

Tomato is one of the most widely consumed vegetables in the world, and maintaining crop quality is critical for food supply and farmer income.  
Most tomato diseases begin at the **leaf stage**, and early detection prevents the infection from spreading to the stem, fruits, and nearby plants.

This project uses **Deep Learning (CNN)** to identify whether a tomato leaf is **Healthy or Diseased**, allowing early diagnosis and timely treatment.

---

## 📌 Dataset Details
This project uses the **PlantVillage dataset**, one of the most widely used datasets for plant disease research.

| Property | Details |
|---------|---------|
| Total Images | 20,000+ |
| Classes | 10 diseased + 1 healthy = **11 classes** |
| Image Types | Lab & field images |
| Goal | Diagnose tomato leaf disease from images |

---

## 🔧 Data Preprocessing
| Step | Description |
|------|-------------|
| Dataset Split | `train_dir` & `test_dir` to avoid data leakage |
| Bad Image Removal | Automatically removed corrupted/unreadable images |
| Image Resizing | All images resized to **128 × 128** |
| Batch Size | 32 |
| Normalization | Pixel values scaled **0–1** |

### 📌 Data Augmentation Techniques
To increase dataset variability and prevent overfitting:

- Random horizontal & vertical flip  
- Random rotation (±8%)  
- Random zoom (–10% to +10%)  
- Random contrast adjustment (+10%)  
- Random brightness adjustment (+10%)

---

## 🤖 Model Architecture
A **Convolutional Neural Network (CNN)** was trained to identify tomato leaf diseases.

Total parameters: 1,315,371

Trainable parameters: 1,312,427

Non-trainable parameters: 2,944

Model was trained with:
- **EarlyStopping**
- `restore_best_weights = True`

This ensures that the final saved model is the **best-performing version**, not the last epoch.

---

## 📈 Model Performance
| Dataset | Accuracy | Loss |
|---------|----------|------|
| Training | **94.45%** | 0.163 |
| Testing | **93.43%** | 0.224 |

The model generalizes well and is robust to real-world leaf image variations.

---

## 🌐 Streamlit Web Application
The trained model is deployed in a **Streamlit web app**, which allows users to:

✔️ Upload an image of a tomato leaf  
✔️ Get prediction — **Healthy or Diseased**  
✔️ View **confidence percentage**  
✔️ If diseased → **Receive the exact disease name**  
✔️ Display **general precaution/care suggestions for farmers**

This makes the system user-friendly for:
- Farmers  
- Agriculture professionals  
- Students & researchers  

---

## 🛠️ Technologies Used
- Python  
- TensorFlow
- Convolutional Neural Networks (CNN)  
- OpenCV / Image Processing  
- Streamlit  
