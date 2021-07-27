import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
fig = sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

st.pyplot(fig)

dots = sns.load_dataset("dots")
fig = sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)

st.pyplot(fig)

st.write(dots)

chart = alt.Chart(dots).mark_circle().encode(
    x="time",
    y="firing_rate",
    color="choice", size="coherence"
)

st.write(chart)

penguins = sns.load_dataset("penguins")

st.title("Hello")
fig = sns.pairplot(penguins, hue="species")
st.pyplot(fig)

fig, _ = plt.subplots()
one_tick = fig.axes[0].yaxis.get_major_ticks()[0]
st.write(type(one_tick))

st.write(fig)

st.pyplot(fig)