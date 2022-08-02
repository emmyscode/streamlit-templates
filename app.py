import streamlit as st
import time
import numpy
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

# Create a sidebar and populate with content
st.sidebar.title("About")
st.sidebar.info(
    """
    Web App URL: <*>
    \n
    GitHub Respository: <https://github.com/emmyscode/streamlit-templates>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Inspirit AI: <https://www.inspiritai.com>
    [GitHub](https://github.com/emmyscode) | [LinkedIn](https://www.linkedin.com/in/em-li)
    """
)

# Display text example
st.title("Streamlit Demo: Templates")
st.markdown("Welcome to the demonstration of a basic template used on Streamlit! With this library, you can deploy an interactive machine learning and data science application to share with anyone! Here, you can see a sampling of some basic features of Streamlit.")
st.markdown("Feel free to check out the source code in the left sidebar to see the Python code that enables this web app.")
st.markdown(" For additional reference material, check out our Streamlit Guide as well as the [Streamlit Docs](https://docs.streamlit.io).")

# Diplay an image
st.image("computer.jpg")
st.caption("Photo Credit: [Domenico Loia](https://unsplash.com/@domenicoloia?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/computer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText). ")

st.subheader("What is Streamlit?")
st.markdown("Streamlit is a free, open-source framework that turns your Python file into a shareable web app. Specifically, it’s a library that is excellent for sharing beautiful machine learning and data science apps to a wide audience. We use Streamlit in this course because it is compatible with Python libraries that you’re already familiar with (e.g. pandas, matplotlib, seaboard, Tensorflow, Pytorch, Keras, Plotly), and it doesn’t require you to learn any front-end programming languages (e.g. HTML, CSS, Javascript).")
st.subheader("Why use Streamlit?")
st.markdown("What sets Streamlit apart from simply creating a static site is two-fold: (1) Streamlit enables you run, deploy, and host machine learning models for free and (2) it allows you to build in interactive sections of your site to invite your audience to participate. With an API all created in pure Python code, there's no need to learn HTML, CSS, or another programming language to get started. Once you have your environment set up, it takes just minutes to go from your machine learning/data science project to a usable web application with as little friction as possible.")

st.markdown("Once you have edited your app file, all you need to run your app locally is run in command line")

# Display some code.
st.code("streamlit run app.py")

st.markdown("where `app.py` is whatever the name of your file is.")

st.subheader("Inserting Media")
st.markdown("You can also insert multimedia, such as audio and video content.")

# Insert audio and video
st.audio("welcome_audio.m4a")
st.video("video.mov")

# Add widgets for interactivity.
st.subheader("Buttons, Sliders, and More")
st.markdown("To take advantage of the interactivity enabled by Streamlit, we can get creative with the breadth of buttons and sliders to offer the user as they move through our data narrative.")
st.checkbox('Check Me!')
st.button('Click Me!')
st.radio("A hotdog is...", ['a sandwich', 'the best part of baseball', 'an incomplete corndog'])
st.selectbox('How would you rank pugs at the Westminster Dog Show?', ['stubbiest legs', 'ugly', 'the more folds the better'])
st.multiselect('Best Way to Eat an Egg', ['Raw', 'Shell On', 'Extra Shell'])
st.select_slider('Today feels like a...', ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday"])
st.slider('How many racoons is ideal?', 0, 50)

# Gathering User Input
st.subheader("Gathering User Input")
st.markdown("Sometimes, you want to prompt your user for information to customize ther experience of your app, and here are some ways to do so.")
st.number_input('Maximum you are willing to spend on the most delicious latte of your life.', 0,1000)
st.text_input('What is something that rhymes with machine?')
st.date_input('Choose a date with the ideal weather.')
st.time_input('What time does school start?')
st.text_area('Write a haiku.')
st.file_uploader('Upload a photo.')
st.color_picker('Choose a color that matches the sidebar.')

# Site Feedback
st.subheader("Site Feedback")
st.markdown("As any good web developer will tell you, you must build in messages to let your user know when things are working, when they're broken, and how to fix things if they run into problems. In Streamlit, you can create your own custom messages depending on whether things have gone to plan.")

st.success("🥳 Fantastic! Success! 🎉")
st.error("🫠 Oh no! Something is wrong 😰")
st.warning("🚧 Warning: Be Careful! 🚧")
st.info("🔍 Just a little information, for your information. 📚")
st.exception(RuntimeError("🐛 We ran into a few bugs back there. 🐞"))
