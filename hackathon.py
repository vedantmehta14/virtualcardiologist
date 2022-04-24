from unicodedata import name
from click import style
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import json
from stat import SF_APPEND 
import pickle
import numpy as np
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import csv


with st.sidebar:
    
    choose = option_menu("Welcome", ["Home", "Predictor", "Precautions", "Nearby Doctors", "About", "Contact Us"],
                         icons=['house', 'calculator', 'exclamation-triangle','geo-alt', 'person lines fill'],
                         menu_icon="activity", default_index=0, 
                         styles={
                            "container": {"padding": "5!important", "background-color": "#1a1a1a"},
                            "icon": {"color": "White", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#4d4d4d"},
                            "nav-link-selected": {"background-color": "#4d4d4d"},
                        }
    )   
 
hack_Data = ""
 
if choose == "Home":
    st.title("Virtual Cardiologist")
    
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
 
    lt_url_hello = "https://assets6.lottiefiles.com/packages/lf20_1yy002na.json"
    lottie_hello = load_lottieurl(lt_url_hello)
 
    st_lottie(
            lottie_hello,  
            key="hello",
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
            height=400,
            width=400            
    )
    st.subheader("Welcome to the next generation cardiologist!")
 
elif choose == "Predictor":
 
    st.title("Heart Disease Prediction ")
 
    st.write("")
    age = st.slider("Age",25, 80)
 
    st.write("")
    status = st.radio("Select Gender", ('Male', 'Female'))
    sex=1
    if (status == 'Male'): sex=1
    else: sex=0
    cp=0
    
    st.write("")
    status = st.radio("Chest Pain", ('No','Yes'))
    if (status == 'Yes'): 
        st.warning(" It is advisable to see a doctor about any unexplained chest pain, even if it goes away on its own.")
        cp=1
    else: cp=0
    
    st.write("")
    trestbps = st.slider("Blood Pressure", 90, 200)
    st.write("Check out this [device](https://www.1mg.com/otc/dr-morepen-combo-pack-of-b.p.-monitor-bp-09-glucometer-with-25-test-strips-and-thermometer-otc472270?wpsrc=Google%20AdWords&wpcid=1917998304&wpsnetn=u&wpkwn=&wpkmatch=&wpcrid=350029945870&wpscid=72306276684&wpkwid=pla-306938878264&gclid=CjwKCAjwx46TBhBhEiwArA_DjMKWz199kEL7D_d0WIUUBwQfWOGsgTOxxQPD8fCWI2fC9CYu2IxrRxoC6vcQAvD_BwE) which helps you to measure blood pressure.")
    if trestbps>120: st.warning("Salty foods in particular can cause high blood pressure. Sugary foods and foods high in saturated fats can also increase blood pressure. Reduce their intake.")
    st.write('Selected value of blood pressure: {}'.format(trestbps))
    
    
    st.write("")
    chol=st.slider("Cholesterol", 120, 570)
    st.write("Check out this [device](https://www.netmeds.com/non-prescriptions/contour-plus-one-meter-with-25-strips-device-1-s?source_attribution=ADW-CPC-Shoppingadsnew&utm_source=ADW-CPC-Shoppingadsnew&utm_medium=CPC&utm_campaign=ADW-CPC-Shoppingadsnew&gclid=CjwKCAjwx46TBhBhEiwArA_DjMZ-cbBg756R2K-UNsU9hoNaxz8oKmqGJeKylzbd1wto6Rjul_NdQhoCSOYQAvD_BwE) which helps you to measure cholesterol.")
    if chol>200: st.warning("Exercise on most days of the week for at least 30 minutes. Eat a low-salt diet that emphasizes fruits, vegetables and whole grains.")
    st.write('Selected value of cholesterol: {}'.format(chol))
 
    st.write("")
    fbs=0
    status = st.radio("High Blood Sugar", ('No','Yes'))
    st.write("Check out this [device](https://www.1mg.com/otc/dr-morepen-combo-pack-of-b.p.-monitor-bp-09-glucometer-with-25-test-strips-and-thermometer-otc472270?wpsrc=Google%20AdWords&wpcid=1917998304&wpsnetn=u&wpkwn=&wpkmatch=&wpcrid=350029945870&wpscid=72306276684&wpkwid=pla-306938878264&gclid=CjwKCAjwx46TBhBhEiwArA_DjMKWz199kEL7D_d0WIUUBwQfWOGsgTOxxQPD8fCWI2fC9CYu2IxrRxoC6vcQAvD_BwE) which helps you to measure blood sugar level.")
 
    if (status == 'Yes'): 
        fbs=1
        st.warning("Exercise to help lower blood sugar. Work with your healthcare provider to make a daily activity plan. Follow your meal plan if you have one. Learn how carbohydrates impact your blood sugar, and work with your diabetes care team to find the best meal plan for you. Maintain a healthy weight.")
    else: fbs=0
    
    st.write("")
    restecg=0
    status = st.radio("Resting Electrocardiographic Results", ('0', '1' ,'2'))
    st.write("Visit a labarotary for these results.")
    if (status == '1'): restecg=1
    elif (status == '2'): restecg=1
    else: restecg=0
 
    st.write("")
    thalach= st.slider("Maximum Heart Rate",70,175)  
    if thalach>100: st.warning("Manage stress. Avoid caffeine and nicotine. Maintain a healthy weight.")
    st.write("How to calculate heart rate?") 
    st.write("To check your pulse at your wrist, place two fingers between the bone and the tendon over your radial artery — which is located on the thumb side of your wrist. When you feel your pulse, count the number of beats in 15 seconds. Multiply this number by four to calculate your beats per minute.")
    st.write('Selected value of heart rate : {}'.format(thalach))
    
    st.write("")
    exang=0
    status = st.radio("Exercise induced Angina", ('No','Yes'))
    st.write("What is exercise induce angina?")
    st.write("During times of low oxygen demand — when resting, for example — the heart muscle may still be able to work on the reduced amount of blood flow without triggering angina symptoms. But when the demand for oxygen goes up, such as when exercising, angina can result.")
    if (status == 'Yes'): exang=1
    else: exang=0
 
    st.write("")
    oldpeak= st.slider("ST depression induced by exercise relative to rest", 0.0, 6.2)   
    st.write("Visit a labarotary for these results.")
    st.write('Selected: {}'.format(oldpeak))
 
    st.write("")
    slope=0
    status = st.radio("The Slope Of The Peak Exercise ST Segment", ('0', '1' ,'2'))
    st.write("Visit a labarotary for these results.")
    if (status == '1'): slope=1
    elif (status == '2'): slope=1
    else: slope=0
 
    st.write("")
    ca=0
    status = st.radio("Number Of Major Vessels Colored By Flourosopy", ('0', '1' ,'2','3','4'))
    st.write("Visit a labarotary for these results.")
    if (status == '1'): ca=1
    elif (status == '2'): ca=2
    elif (status == '3'): ca=3
    elif (status == '4'): ca=4
    else: ca=0
 
    st.write("")
    thal=1
    status = st.radio("Thalassemia", ('Normal', 'Fixed Defect' ,'Reversable Defect'))
    st.write("Thalassemia is an inherited blood disorder that causes your body to have less hemoglobin than normal. Hemoglobin enables red blood cells to carry oxygen. Thalassemia can cause anemia, leaving you fatigued. If you have mild thalassemia, you might not need treatment. Thalassemia can be calculated by blood tests.")
    if (status == 'Normal'): thal=1
    elif (status == 'Fixed Defect'): thal=2
    elif (status == 'Reversable Defect'): thal=3
    ok = st.button("Submit")
    def load_model():
        with open('saved_steps.pkl', 'rb') as file:
            data = pickle.load(file)
        return data
    data = load_model()
    rfc = data["model"]
    # sc = data["sc"]
    if ok:
        X = np.array([[age, sex,cp, trestbps,   chol,   fbs,    restecg ,thalach,   exang   ,oldpeak,   slope,  ca, thal]])
        # X=sc.fit_transform(X)
        X = X.astype(float)
 
        pred = rfc.predict(X)
        if pred[0]==1: st.error('You are having Heart Disease')
        elif pred[0]==0: st.success('You are not having Heart Disease')
 
    s="\t\tRECOMMENDED MEDICINES\n"
    s+="---------------------------------------------\n"
    if ok:
        st.subheader("Recommended medicines: ")
        if cp==1:
            st.write("For Chest Pain: ".ljust(30," ") +"Artery relaxers")
            s+="For Chest Pain: ".ljust(30," ") +"Artery relaxers\n"
        if trestbps>120:
            st.write("For Blood Pressure: ".ljust(30," ")+"Lisinopril")
            s+="For Blood Pressure: ".ljust(30," ")+"Lisinopril\n"
        if chol>=200:
            st.write("For Cholesterol: ".ljust(30," ")+"Statins")
            s+= "For Cholesterol: ".ljust(30," ")+"Statins\n"
        if fbs==1:
            st.write("For High Blood Sugar: ".ljust(30," ")+"Metformin")
            s+="For High Blood Sugar: ".ljust(30," ")+"Metformin\n"
        if thalach>100:
            st.write("For High Heartrate: ".ljust(30," ")+"Metoprolol")
            s+="For High Heartrate: ".ljust(30," ")+"Metoprolol\n"
        if exang==1:
            st.write("For Angina pain: ".ljust(30," ")+"Dolo")
            s+="For Angina pain: ".ljust(30," ")+"Dolo\n"
        if thal==2:
            st.write("For Fixed Defect in Thalassemia:".ljust(30," ")+" Deferoxamine")
            s+="For Fixed Defect in Thalassemia:".ljust(30," ")+" Deferoxamine\n"
        with open("prescription.txt","w") as f:
            f.write(s)
        with open('prescription.txt') as f:
            st.download_button('Download Prescription', f)
    s=""
 
elif choose == "Precautions":
    st.title("Precautions")
    st.subheader("What are the heart disease risk factors that I cannot change?")
    st.write("Age: Your risk of heart disease increases as you get older. Men of age 45 and older and women of age 55 and older have a greater risk.")
    st.write("Sex: Some risk factors may affect heart disease risk differently in women than in men. For example, estrogen provides women some protection against heart disease, but diabetes raises the risk of heart disease more in women than in men.")
    st.write("Family history: You have a greater risk if you have a close family member who had heart disease at an early age.")
    st.subheader("What can I do to lower my risk of heart disease?")
    st.write("Fortunately, there are many things you can do to reduce your chances of getting heart disease:")
    st.write("1. Control your blood pressure. It is important to get your blood pressure checked regularly - at least once a year for most adults, and more often if you have high blood pressure. Take steps, including lifestyle changes, to prevent or control high blood pressure.")
    st.write("2. Keep your cholesterol and triglyceride levels under control. Lifestyle changes and medicines (if needed) can lower your cholesterol.")
    st.write("3. Stay at a healthy weight. Being overweight or having obesity can increase your risk for heart disease. Controlling your weight can lower risks.")
    st.write("4. Eat a healthy diet. Try to limit saturated fats, foods high in sodium and added sugars. Eat plenty of fresh fruit, vegetables, and whole grains. ")
    st.write("5. Get regular exercise. Exercise has many benefits, including strengthening your heart and improving your circulation. It can also help you maintain a healthy weight and lower cholesterol and blood pressure.")
    st.write("6. Limit alcohol. Drinking too much alcohol can raise your blood pressure. It also adds extra calories, which may cause weight gain. Men should have no more than two alcoholic drinks per day, and women should not have more than one.")
    st.write("7. Don't smoke. Cigarette smoking raises your blood pressure and puts you at higher risk for heart attack and stroke.")
    st.write("8. Manage stress. Stress is linked to heart disease in many ways. It can raise your blood pressure. Extreme stress can be a 'trigger' for a heart attack. Some ways to help manage your stress include exercise, listening to music, focusing on something calm or peaceful, and meditating.")
    st.write("9. Manage diabetes. Having diabetes doubles your risk of diabetic heart disease. It is important to get tested for diabetes, and if you have it, to keep it under control.")
    st.write("10. Make sure that you get enough sleep. If you don't get enough sleep, you raise your risk of high blood pressure, obesity, and diabetes. Most adults need 7 to 9 hours of sleep per night. Make sure that you have good sleep habits. If you have frequent sleep problems, contact your health care provider.")
 
elif choose == "About":
    st.title("About")
    st.subheader("Aim:")
    st.write("This website is used to predict whether a person is suffering from a heart disease or not.")
    st.write("To calculate the results for the same we have trained a machine learning model using datasets related to heart diseases.")
    st.write("Our model has an accuracy of 98.05%.")
    st.write("Our main aim is to give users the facility to check whether they are suffering from a heart disease before going for costly checkups.")
    st.write("")
    st.subheader("Designed by: ")
    st.write("1. Rahil Shah")
    st.write("2. Vedant Mehta")
    st.write("3. Nayan Senjaliya")
    st.write("4. Yash Pandya")
 
elif choose == "Nearby Doctors":
    with open("hospitals.txt") as f:
        for i in range(16):
            content=f.readline().split(",")
            st.dataframe(content)

elif choose == "Contact Us":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Roboto'; color: #ffffff;} 
    </style> """, unsafe_allow_html=True)
    st.title("How can we help?")
    st.subheader("We value your feedback!")
    with st.form(key='columns_in_form2',clear_on_submit=True): 
        Name=st.text_input(label='Enter Your Name') #Collect user feedback
        Email=st.text_input(label='Enter Your Email') #Collect user feedback
        Message=st.text_area(label='Enter Your Message',height=200,max_chars=500) #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for contacting us. We will answer your doubts as soon as possible!')
 
        hack_Data = "Name: " +  Name + "\n" + "Email: " + Email + "\n" + "Message: " + Message + "\n"
 
    with open("hackthon_data.txt","a+") as f:
        f.write(hack_Data)
    pass