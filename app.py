import streamlit as st
from PIL import Image
import numpy as np


@st.cache_resource
def load_my_model():
    from tensorflow.keras.models import load_model
    return load_model("best_model.keras")

model = load_my_model()


st.title("Tomato Leaf Disease Prediction")
st.write('''
         Upload the image of a Tomato leaf.
         This application will analyze the image and predict whether the leaf is **healthy** or 
         affected by one of **10 common tomato leaf diseases**. You'll also receive simple care suggestions to 
         help manage or prevent the issue.
         ''')


uploaded_file = st.file_uploader("Upload the image", type = ["jpg","jpeg","png"])

if st.button("Predict"):
    if uploaded_file is not None:

        st.image(uploaded_file, caption = "Uploaded Image")
        image = Image.open(uploaded_file)
        image = image.convert("RGB")
        image = image.resize((128,128))
        
        image = np.array(image)
        image = np.expand_dims(image, axis = 0)

        predict = model.predict(image)
        predict_class = np.argmax(predict)
        confidence = np.max(predict)
        
        DISCLAIMER = "⚠️ *This information is provided for general educational purposes only. Please verify with your local agricultural expert before taking any action.*"

        if confidence < 0.7:
            st.warning('''Confidence of the prediction is Low.
                       Please upload a clear image of tomato leaf''')
        else:
            st.success(f"Confidence of the prediction: {confidence*100:.2f}%")

            if predict_class == 0:
                st.info("Bacterial spot")
                st.write('''   
                         **Suggestions:**
                         - Remove infected leaves and avoid overhead watering.  
                         - Use copper-based fungicides if infection spreads.  
                         - Ensure proper plant spacing for air flow.
                         ''')
                st.caption(DISCLAIMER)

            elif predict_class == 1:
                st.info("Early blight")
                st.write('''              
                         **Suggestions:**
                         - Remove affected leaves early and water at soil level.  
                         - Apply neem oil or a fungicide with chlorothalonil if needed.  
                         - Rotate crops to prevent reinfection.
                         ''')
                st.caption(DISCLAIMER)

            elif predict_class == 2:
                st.info("Late blight")
                st.write('''
                         **Suggestions:**
                         - Destroy heavily infected plants immediately.  
                         - Use fungicides with mancozeb or copper under expert guidance.  
                         - Avoid high humidity and wet leaves.
                         ''')
                st.caption(DISCLAIMER)
                         
            elif predict_class == 3:
                st.info("Leaf Mold")
                st.write('''
                         **Suggestions:**
                         - Increase air circulation and avoid overhead watering.  
                         - Use sulfur-based fungicides if the problem worsens.  
                         - Remove lower leaves to reduce moisture buildup.
                         ''')
                st.caption(DISCLAIMER)
                         
            elif predict_class == 4:
                st.info("Septoria leaf spot")
                st.write('''                 
                         **Suggestions:**
                         - Prune lower leaves and water at the base of plants.  
                         - Remove infected debris regularly.  
                         - Apply fungicides containing chlorothalonil or mancozeb.
                         ''')
                st.caption(DISCLAIMER)
                         
            elif predict_class == 5:
                st.info("Spider mites Two spotted spider mite")
                st.write('''
                         **Suggestions:**
                         - Spray neem oil or insecticidal soap under leaves.  
                         - Increase humidity and rinse leaves with clean water.  
                         - Remove heavily infested areas.
                         ''')
                st.caption(DISCLAIMER)
                         
            elif predict_class == 6:
                st.info("Target Spot")
                st.write('''
                         **Suggestions:**
                         - Remove infected leaves immediately.  
                         - Avoid excess leaf moisture and maintain spacing.  
                         - Apply preventive fungicide sprays if necessary.
                         ''')
                st.caption(DISCLAIMER)

            elif predict_class == 7:
                st.info("Tomato yellow leaf Curl Virus")
                st.write('''
                         **Suggestions:**
                         - Remove infected plants to stop the spread.  
                         - Control whiteflies with sticky traps or neem oil.  
                         - Use virus-resistant tomato varieties in the future.
                         ''')
                st.caption(DISCLAIMER)     

            elif predict_class == 8:
                st.info("Tomato Mosaic Virus")
                st.write('''
                         **Suggestions:**
                         - Remove infected plants and disinfect garden tools.  
                         - Avoid handling plants after smoking or touching tobacco.  
                         - Choose resistant tomato varieties.
                         ''')
                st.caption(DISCLAIMER)

            elif predict_class == 9:
                st.info("Healthy")
                st.write('''
                         **Your plant looks healthy!**
                         - Maintain balanced watering (not too wet or too dry).  
                         - Ensure good airflow and proper sunlight.  
                         - Regularly inspect for early signs of disease.
                         ''')
                         
            elif predict_class == 10:
                st.info("Powdery mildew")
                st.write('''
                         **Suggestions:**
                         - Improve air circulation and avoid wetting leaves.  
                         - Use sulfur or potassium bicarbonate sprays for control.  
                         - Remove infected leaves early.
                         ''')
                st.caption(DISCLAIMER)
                         

    else:
        st.warning("⚠️ Please upload an image before clicking Predict.")
