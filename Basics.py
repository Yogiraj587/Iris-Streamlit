import streamlit as st

st.write("Hello World!")

### Adding Headers
st.header("This is a header")
st.subheader("This is a subheader")

### Adding sliders
slider = st.slider("Select a value",0,100)
st.write("Your selected value is", slider)

### Creating Buttons
button = st.button("Click Me!")
if button:
    st.write("You clicked the button!")

### Displaying data using pandas dataframe
import pandas as pd
df = pd.read_csv("Iris.csv")
st.dataframe(df)

### Adding Interactive Widgets
checkbox = st.checkbox("Show/Hide")
if checkbox:
    st.write("Checkbox is selected")
else:
    st.write("Checkbox is not selected")