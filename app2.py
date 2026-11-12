
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.title("Titanic Data Application")

# st.image("src/utils/tittanic_image.jpg", use_column_width=True , caption="Titanic Data Analysis")
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).parent

image_path = BASE_DIR / "src" / "utils" / "tittanic_image.jpg"

if image_path.exists():
    st.image(
        str(image_path),
        caption="Titanic Data Analysis",
        width="stretch"
    )
else:
    st.error(f"Image not found: {image_path}")

df = pd.read_csv("src/data/titanic.csv")
df.columns = df.columns.str.lower()

df["class"] = df["pclass"].map({
    1: "First",
    2: "Second",
    3: "Third"
})

df["survival"] = df["survived"].map({
    0: "Died",
    1: "Survived"
})

df["port"] = df["embarked"].map({
    "C": "Cherbourg",
    "Q": "Queenstown",
    "S": "Southampton"
})

df["family_size"] = df["sibsp"] + df["parch"] + 1

df["title"] = df["name"].str.extract(
    r",\s*([^\.]+)\.", expand=False
)

df["age_group"] = pd.cut(
    df["age"],
    [0, 12, 18, 35, 60, 80],
    labels=["child", "teen", "young adult", "adult", "senior"]
)

ORDERS = {
    "class": ["First", "Second", "Third"],
    "survival": ["Died", "Survived"],
    "age_group": ["child", "teen", "young adult", "adult", "senior"]
}

COLORS = {
    "Died": "#D95D4A",
    "Survived": "#0F766E"
}
##################################

st.subheader("Dataset Preview")
# to show or hide data
show_data = st.checkbox("Show raw data")
if show_data:
    st.write("### Raw Data")
    st.dataframe(df.head(10))
################### filtered data #######################3
classes=st.multiselect("Select classes", ["First", "Second", "Third"], default=["First", "Second", "Third"])
gender=st.multiselect("Select gender", ["male", "female"], default=["male", "female"])
data = df[(df["class"].isin(classes)) & (df["sex"].isin(gender))]

##########################3
c1,c2 = st.columns(2)
with c1:
    st.subheader("Class Distribution")
    class_counts = data["class"].value_counts()
    st.bar_chart(class_counts)
with c2:
    st.subheader("Survival Distribution")
    outcome = data['survived'].value_counts()
    fig3 = px.pie(names =['died', 'survived'], values = outcome.values,  hole=0.4)
    st.plotly_chart(fig3)
###################################33
fig1 = px.histogram(data, x = 'family_size')
st.plotly_chart(fig1)

##################################3
fig2 = px.box(data, x = 'class',y = 'fare', color = 'class', category_orders= {'class':['first', 'second', 'third']} )
st.plotly_chart(fig2)

#####################3
