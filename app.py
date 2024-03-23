from pathlib import Path

import streamlit as st
from PIL import Image

#-----PATH SETTINGS--
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" /"main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Profile.png"

#----General Settings---
PAGE_TITLE = "Digital Resume| Sukhpreet Kaur"
PAGE_ICON=":wave"
NAME="Sukhpreet Kaur"
DESCRIPTION="""
🚀 Data Science Voyager at Guru Nanak Dev Engineering College (2020-2024), wielding Python spells to decode data mysteries. 📊 Passionate about transforming insights into action and thriving in collaborative quests. 🎙️ Master storyteller and adaptability ninja, ready to conquer new challenges! 🔥 Join me in exploring the endless possibilities of the data universe! 🌌
"""
EMAIL = "kaurcs2001@gmail.com"
SOCIAL_MEDIA={
    "LinkedIn":"https://www.linkedin.com/in/sukhpreet-kaur-a0b6bb282/",
    "GitHub":"https://github.com/Sukhpreet2001"
}
PROJECTS = {
    "🏆Chat with PDF-This project provides a basic outline for how Langchain and LLM can be used to querying given PDF":"https://github.com/Sukhpreet2001/Chat_with_PDF",
    "🏆Intellicourse-This was a collaborative project academic purposes in light of the Major Project . A platform was created for automatic course generation using GPT-3.":" ",
    "🏆Titanic Classification-Task for Bharat Intern Virtual Internship.":"https://github.com/Sukhpreet2001/Bharat-Intern-Oct-2023",
    "🏆Number Recognition-Task for Bharat Intern Virtual Internship.":"https://github.com/Sukhpreet2001/Bharat-Intern-Oct-2023"
}

st.set_page_config(page_title=PAGE_TITLE , page_icon=PAGE_ICON)

#-----LOAD CSS , PDF & PROFILE PIC ----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#----HERO SECTION ----
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- 🌟 Currently pursuing BTech in Computer Science Engineering from Guru Nanak Dev Engineering College, Ludhiana
- 🌟 Data Science Intern at Sabudh, gaining valuable hands-on experience in real-world projects
- 🌟 Developing proficiency in Dataiku for data analysis and machine learning tasks
- 🌟 Strong foundation in Python programming
- 🌟 Exploring statistical principles and their applications in data science
- 🌟 Collaborative team player with a proactive approach to tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (NumPy, Pandas, Scikit-learn), SQL
- 📊 Data Visualization: Matplotlib, Seaborn
- 📚 Modeling: Regression, Decision Trees, Machine Learning Algorithms
- 🗄️ Databases: MySQL
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

