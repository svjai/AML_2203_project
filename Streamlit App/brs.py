import streamlit as st
import pandas as pd
import pickle
import base64


# Load data
LOGO_IMAGE = "1.png"
st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
    }
    .logo-img {
        margin: 0 auto; /* Center image horizontally */    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)

df = pd.read_pickle('book.pkl')
similarity_scores = pd.read_pickle('cosine_sim.pkl')

def get_recommendations(title):
    book_index = df.index[df['Book_title'] == title].tolist()[0]
    similarity_score = list(enumerate(similarity_scores[book_index]))
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    similarity_score = similarity_score[1:11]
    book_indices = [i[0] for i in similarity_score]
    return df.iloc[book_indices][['Book_title', 'author_name(s)']]

def main():
    st.title('BookNest: Navigate Your Next Read')

    user_input = st.text_input('Enter a Book Title:', '')  # User input as text
    
    if st.button('Get Recommendations'):
        if user_input:
            recommendations = get_recommendations(user_input)
            st.subheader('Recommended Books')
            st.write(recommendations)
        else:
            st.warning('Please enter a book title.')

if __name__ == '__main__':
    main()
