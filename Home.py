import streamlit as st
import pandas
# Create two columns
col1, col2 = st.columns(2)

# Add the image in the first column
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
        st.write(f"[Source Code]({row['url']})")


