import streamlit as st

# Custom CSS for alignment
st.markdown(
    """
    <style>
    .container {
        display: flex;
        align-items: flex-end;
    }
    .image-container {
        flex: 1;
    }
    .content-container {
        flex: 2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a container with custom classes for alignment
st.markdown(
    """
    <div class="container">
        <div class="image-container">
            <img src="image.jpg" style="width:100%; border-radius:10px;">
        </div>
        <div class="content-container">
            <h1>Mugdho Jeferson Rozario</h1>
            <p>
                I am an Engineering Physics student at McMaster University, passionate about advancing sustainable energy through innovation.
                During an internship, I developed a remote operation program for the autonomous robot <b>Elfin</b>, an experience that honed my
                problem-solving skills and reinforced my interest in cutting-edge technologies.
            </p>
            <p>
                Aspiring to specialize in nuclear energy, I aim to leverage these skills to design advanced reactors that redefine safety,
                efficiency, and sustainability in the global energy landscape.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("You can find some of the apps I have built in Python below. Feel free to contact me!")
