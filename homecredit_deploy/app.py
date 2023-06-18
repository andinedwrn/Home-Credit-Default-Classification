import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title = 'Home Credit: Credit Exploration - EDA',
    layout = 'wide',
    initial_sidebar_state= 'expanded'
)

def run():
    st.title('Home Credit')
    st.subheader('Credit Exploration')

    image = Image.open ('Home Credit.png')
    st.image(image, caption= 'Home Credit', use_column_width=True)

    st.write('Page written by **Geraldine Dewarani**')

    st.markdown('---')

    # Show Data Frame 
    df = pd.read_csv ('bureau.csv')

    #barplot Credit Status Count
    st.write ('#### Credit Status Count')
    fig = plt.figure(figsize= (15,5))
    credit_status_counts = df['CREDIT_ACTIVE'].value_counts()
    sns.barplot(x=credit_status_counts.index, y=credit_status_counts.values)
    plt.xlabel("Credit Status")
    plt.ylabel("Count")
    plt.title("Credit Status Counts")
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

    #boxplot credit type
    st.write ('#### Credit Type')
    fig = plt.figure(figsize= (15,5))
    credit_type_group = df.groupby('CREDIT_TYPE')
    mean_credit_amount = credit_type_group['AMT_CREDIT_SUM'].mean()
    sns.barplot(x=mean_credit_amount.index, y=mean_credit_amount.values)
    plt.xticks(rotation=45)
    plt.xlabel("Credit Type")
    plt.ylabel("Credit Amount")
    plt.title("Amount by Credit Type")
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

    #barplot of credit currency
    st.write ('#### Credit Currency')
    credit_currency_counts = df['CREDIT_CURRENCY'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(credit_currency_counts.index, credit_currency_counts.values)
    plt.xlabel('Credit Currency')
    plt.ylabel('Count')
    plt.title('Credit Currency Distribution')
    plt.show()
    st.pyplot(fig)

    
if __name__ == '__main__':
    run()
