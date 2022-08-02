import streamlit as st
import time
import numpy
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

# Create a sidebar and populate with content
st.sidebar.title("About")
st.sidebar.info(
    """
    Web App URL: <https://emmyscode-streamlit-templates-app-1n8x1w.streamlitapp.com>
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

# Data Visualizations
st.subheader("Data Visualization")
st.markdown("There are a lot of different methods to tell your story with data, and the one that we'll feature functionality for here is with `matplotlib.pyplot`.")
st.markdown("You've spent a lot of time in the weeds with your project data, but now it's time to display your data in a beautiful and intuitive way to communicate your findings with as broad an audience as possible.")

## Scatterplot Demo
# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
price_data = (cbook.get_sample_data('goog.npz', np_load=True)['price_data']
              .view(np.recarray))
price_data = price_data[-250:]  # get the most recent 250 trading days

delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Marker size in units of points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()
st.pyplot(fig)

## 3D Contour Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)

# Plot the surface.
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

# Tweak the limits and add latex math labels.
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
st.pyplot(fig)

## Frontpage 3D Example
dem = cbook.get_sample_data('jacksboro_fault_dem.npz', np_load=True)
z = dem['elevation']
nrows, ncols = z.shape
x = np.linspace(dem['xmin'], dem['xmax'], ncols)
y = np.linspace(dem['ymin'], dem['ymax'], nrows)
x, y = np.meshgrid(x, y)

region = np.s_[5:50, 5:50]
x, y, z = x[region], y[region], z[region]

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# To use a custom hillshading mode, override the built-in shading and pass
# in the rgb colors of the shaded surface calculated from "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
st.pyplot(fig)

## Simple Categorical Heatmap
vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])


fig, ax = plt.subplots()
im = ax.imshow(harvest)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(farmers)), labels=farmers)
ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Harvest of local farmers (in tons/year)")
fig.tight_layout()
st.pyplot(fig)

# Displaying Maps
st.subheader("Mapping Data")
st.markdown("For applications that deal with geographic data, Streamlit supports an interactive map feature that displays different locations.")
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(df)

# Summary
st.subheader("Summary")
st.markdown("In this example template, we've seen different features that are possible with Streamlit. However, we haven't gotten to the best part of Streamlit yet...the support for machine learning applications! We'll keep this template about the API usage. If you're interested in seeing specific demos for machine learning projects, check out our Github for some fun examples on specific models!")
