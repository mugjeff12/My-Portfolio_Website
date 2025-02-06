'''import streamlit as st
import pandas
# Create two columns
col1, col2 = st.columns(2)


with col1:
    st.image("image.jpg", use_container_width=True)


# Add the title and content inside st.info in the second column
with col2:
    st.title("Mugdho Jeferson Rozario")
    st.info("""
        I am an Engineering Physics student at McMaster University, passionate about advancing sustainable energy through innovation. 
        During an internship, I developed a remote operation program for the autonomous robot, **Elfin**, an experience that honed my 
        problem-solving skills and reinforced my interest in cutting-edge technologies.

        Aspiring to specialize in nuclear energy, I aim to leverage these skills to design advanced reactors that redefine safety, 
        efficiency, and sustainability in the global energy landscape.
    """)

# Add additional text below
st.write("You can find some of the apps I have built in Python below. Feel free to contact me!")

col3,empty_col,col4  = st.columns([1.5,0.5,1.5])

df = pandas.read_csv('data.csv',sep=';')

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")'''

import streamlit as st
import pandas

# Style improvements
st.markdown(
    """
    <style>
    .profile-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .header-text {
        text-align: center;
        font-weight: bold;
        font-size: 36px;
        margin-top: 20px;
        margin-bottom: 10px;
        font-family: 'Arial', sans-serif;
    }
    .description-text {
        text-align: center;
        font-size: 18px;
        line-height: 1.6;
        margin-bottom: 30px;
        font-family: 'Georgia', serif;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Profile picture
st.image("image_up.jpg",width=150, use_container_width=True)

# Header text
st.markdown("<div class='header-text'>Mugdho Jeferson Rozario</div>", unsafe_allow_html=True)

# Description text
st.markdown(
    """
    <div class='description-text'>
        I am an Engineering Physics student at McMaster University, passionate about advancing sustainable energy through innovation. 
        During an internship, I developed a remote operation program for the autonomous robot, <strong>Elfin</strong>, an experience that honed my 
        problem-solving skills and reinforced my interest in cutting-edge technologies.
        <br><br>
        Aspiring to specialize in nuclear energy, I aim to leverage these skills to design advanced reactors that redefine safety, 
        efficiency, and sustainability in the global energy landscape.
    </div>
    """,
    unsafe_allow_html=True
)

# Section for projects
st.header("My Projects")
st.write("You can find some of the apps I have built in Python below. Feel free to contact me!")

# Columns for displaying project cards
col1, col2 = st.columns(2)

# Sample data (replace with your actual CSV read operation)
df = pandas.read_csv('data.csv', sep=';')

# Projects displayed in columns
with col1:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'], use_container_width=True)
        st.write(f"[Source Code]({row['url']})")

with col2:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'], use_container_width=True)
        st.write(f"[Source Code]({row['url']})")
