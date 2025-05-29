import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('SocialMedia_Analytics_Combined.csv')

# Set title
st.title('Social Media Engagement by Platform')

# Group by platform and calculate total likes
platform_engagement = data.groupby('Platform')[['Likes', 'Comments', 'Shares']].sum().reset_index()

# Show data table
st.dataframe(platform_engagement)

# Bar chart for Likes
fig1, ax1 = plt.subplots()
ax1.bar(platform_engagement['Platform'], platform_engagement['Likes'], color='skyblue')
ax1.set_title('Total Likes by Platform')
ax1.set_xlabel('Platform')
ax1.set_ylabel('Likes')
plt.xticks(rotation=45)
st.pyplot(fig1)

# Bar chart for Comments
fig2, ax2 = plt.subplots()
ax2.bar(platform_engagement['Platform'], platform_engagement['Comments'], color='lightgreen')
ax2.set_title('Total Comments by Platform')
ax2.set_xlabel('Platform')
ax2.set_ylabel('Comments')
plt.xticks(rotation=45)
st.pyplot(fig2)

# Bar chart for Shares
fig3, ax3 = plt.subplots()
ax3.bar(platform_engagement['Platform'], platform_engagement['Shares'], color='salmon')
ax3.set_title('Total Shares by Platform')
ax3.set_xlabel('Platform')
ax3.set_ylabel('Shares')
plt.xticks(rotation=45)
st.pyplot(fig3)
