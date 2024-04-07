import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title='Your Mental Health Matters',page_icon='::star::',layout='wide',initial_sidebar_state='expanded')

def is_all_numbers(text):
    try:
        float(text)
        return (True and float(text) < 4.00)
    except ValueError:
        return False

def preprocess(age,gender,rela,crs,gpa,stress,depress,anxiety,sleep,physic,socialSub,Family,Finance,gpa_grp,grad,academc):
    if gender == "Female":
        sex = 0
    else:
        sex = 1

    if rela == 'Single':
        relation = 2
    elif rela == 'Married':
        relation = 1
    else:
        relation = 0
    
    if crs == 'Computer Science':
        course = 1
    elif crs == 'Medical':
        course = 4
    elif crs == 'Business':
        course = 0
    elif crs == 'Engineering':
        course = 2
    elif crs == 'Law':
        course = 3
    else:
        course = 5
    # empty string or NULL 
    if gpa == "":
        GPa = 0
    else:
        GPa = float(gpa)


    if stress < 3:
        strss = 0
    elif stress >= 3:
        strss = 1

    if sleep == "Poor":
        slep = 0
    elif sleep == "Average":
        slep = 1
    else:
        slep = 2

    if physic == "Poor":
        phsic = 0
    elif physic == "Average":
        phsic = 1
    else:
        phsic = 2

    if socialSub == "Poor":
        social = 0
    elif socialSub == "Average":
        social = 1
    else:
        social = 2

    if Family_History == "No":
        fam=0
    else :
        fam=1

    if Finance <3 :
        finance=0
    elif Finance >= 3:
        finance=1

    if grad == "A":
        grade = 0
    elif grad == "B":
        grade = 1
    elif grad == "C":
        grade = 2
    elif grad == "D":
        grade= 3
    else:
        grade = 4

    if gpa_grp =="High GPA":
        gpagrp=0
    else :
        gpagrp=1

    if academc == "Freshmen":
        academc_class = 0
    elif academc == "Sophomores":
        academc_class = 1
    elif academc == "Juniors":
        academc_class = 2
    elif academc == "Seniors":
        academc_class = 3
    else:
        academc_class = 4
 

    if depress < 3 :
       depression= 0
    elif depress >= 3:
       depression = 1

    if anxiety < 3 :
       anx= 0
    elif anxiety >= 3:
       anx = 1   

    list = [age,sex,relation,course,GPa,strss,depression,anx,slep,phsic,social,fam,finance,gpagrp,grade,academc_class]   
    vals = np.array(list).reshape(-1,len(list))
    return vals



def clusterDef(pred):
    

     if pred[0] == 0:
          st.write('''You're doing okay on grades, but maybe something outside of College is getting you down. It could be life stuff, relationships, or even the pressure of Law courses (especially if you're in that group!). Here are some ideas:

* Let's Talk About It: Are there things outside of college that are stressing you out? Talking to a counselor or therapist can help you identify those stressors and develop strategies to manage them. Your campus probably has counseling services available, so don't hesitate to reach out.
* Chill Out Techniques: Feeling overwhelmed? Learning some relaxation techniques like deep breathing or meditation can be a lifesaver. Maybe there are workshops or resources offered on campus to help you learn these skills.''')
     if pred[0] == 1:
          st.write('''First year can be tough! Adjusting to college life, dealing with demanding courses like Medical or Engineering, and maybe even financial worries can all add up. Here's some support:

* Freshmen Survival Guide: Lots of colleges offer programs specifically for first-year students to help them adjust. Check out if yours has one - it could have tips on time management, navigating campus resources, and making friends.
* Time Management Ninja: Ever feel like there just aren't enough hours in the day? Learning some time management skills can be a game-changer. Many campuses offer workshops or resources on this.
* Money Matters: Feeling the financial squeeze? Check with your college's financial aid office to see what resources they offer, like scholarships or grants. Learning how to budget effectively can also be a big help.''')
     if pred[0] == 2:
          st.write('''You're crushing it academically, but maybe stress is still knocking on your door. This could be perfectionism, feeling like a fraud (imposter syndrome), or just wanting a better work-life balance. Here are some ideas:

* Stress Management for A+ Students: Workshops or support groups can help high achievers like you deal with stress in a healthy way. They can address things like perfectionism and managing your expectations.
* Time Management Masterclass: You're already good at managing your time, but there's always room to improve! Advanced time management techniques and study strategies can help you get even more done without burning yourself out.''')           
     if pred[0] == 3:
          st.write('''Grades might be feeling tough, and everything else seems super stressful. This can happen, especially with demanding courses like Medical or Computer Science on your plate. Let's see how we can help:

* Academic Support Squad: Your college likely has tutors, writing centers, or study skills workshops available. Don't be shy to get some extra help!
* Mental Health Check-in: Sometimes, feeling overwhelmed can be a sign of anxiety or depression. Don't hesitate to talk to a counselor or therapist - they can help you navigate these challenges.
* Time Management Coaching: Feeling like you're drowning in work? Working with a coach can help you develop personalized time management and study skills.
* Study Buddies: Sometimes having a study partner can make a big difference. Maybe there are peer mentoring programs at your college that can connect you with someone who's already been through what you're going through.
* Coursework Options: Some colleges offer flexible course options like online sections or lighter credit loads. Talk to your advisor to see if there are ways to manage your academic workload better.''')

     



model = joblib.load(open('Mental Health SVM','rb'))


with st.container():
    st.markdown("<h1 style='text-align: center;'>Your Mental Health Matters</h1>",unsafe_allow_html=True)

st.write('---')
st.subheader('Please Enter Your Data: ')

with st.container():
    Age = st.number_input("Age: ",min_value=18,max_value=45,value = 18,step=1)

    Gender = st.radio("Gender: ",['Male','Female'])

    Relationship = st.radio("Relation Ship Status: ",['Single','In A Relation', 'Married'])

    Course = st.radio("Course: ",['Computer Science','Medical','Law','Engineering','Business','Other'])

    CGPA = st.text_input("CGPA (Leave the field empty if none): ",)

    Stress = st.slider("On a Scale from 0 to 5 how would you rate your stress level: ",min_value=0,max_value=5)

    Depression = st.slider("On a Scale from 0 to 5 how would you rate your depression level: ",min_value=0,max_value=5)

    Anxiety = st.slider("On a Scale from 0 to 5 how would you rate your anxiety level: ",min_value=0,max_value=5)

    Sleep = st.radio('How do you describe your sleep quality?',['Good',"Average",'Poor'])

    Physical = st.radio('''Please indicate your current level of physical activity.
                            Low: If you do not engage in sports or gym activities.
                            Average: If you engage in sports or gym activities occasionally.
                            High: If you engage in sports or gym activities regularly.''',['Low',"Average",'High'])
    
    Social_sup = st.radio('''Please indicate your current level of social support from family and friends.
                            Low: If you feel you have limited social support from family and friends.
                            Average: If you feel you have moderate social support from family and friends.
                            High: If you feel you have strong social support from family and friends.''',['Low',"Average",'High'])
    
    Family_History = st.radio('''Do you have any family members (parents, siblings, grandparents) who have been diagnosed with or experienced mental health problems?''',['Yes',"No",'Not Sure'])

    Financial_Stress = st.slider('''Please indicate your current level of financial stress.
                                    financial stress include worries about paying bills,
                                    managing debt,
                                    saving for the future,
                                    or meeting basic needs such as food, housing, and healthcare.''',min_value=0,max_value=5)
    

    Gpa_Group = st.radio('What GPA group do you belong to?',['High GPA','Low GPA'])

    Grade = st.radio('Your Grade',['A','B','C','D','E','F'])


    Academic_Classification = st.radio('Which academic year you belong to?',['Freshmen.','Sophomore.','Juniour.','Senior.','Masters.'])


    
    if st.button("Discover The Insights"):
        if is_all_numbers(CGPA) or CGPA == '':
                data = preprocess(age=Age,gender=Gender,rela=Relationship,crs=Course,gpa=CGPA,stress=Stress,depress=Depression,anxiety=Anxiety,sleep=Sleep,physic=Physical,socialSub=Social_sup,Family=Family_History,Finance=Financial_Stress,gpa_grp=Gpa_Group,grad=Grade,academc=Academic_Classification)
                y_pred = model.predict(data)
                clusterDef(y_pred)
                st.write('''Remember, you're not alone!  Each of these groups has resources available on campus to help you succeed. Don't be afraid to ask for help, that's what support systems are for!''')
        else:
                st.error("Please enter a valid CGPA or leave the field empty")
        