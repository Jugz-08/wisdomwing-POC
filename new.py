import streamlit as st
from openai import OpenAI


#------------------Setting------------------
api_key_openai=st.secrets["api_key_openai"]
organization_key=st.secrets["organization"]
project_key=st.secrets["project"]
#------------------Setting------------------

client=OpenAI(api_key=api_key_openai,organization=organization_key, project=project_key)

messages=st.empty()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def generate_response(book_name, summary_type):
    if summary_type == "Chapter-wise Summary":
        prompt = f'''As an expert book reviewer, please provide a chapterwise summary, \
            key takeaways, and actionable items along with chapter names from the book {book_name}'''
    else:
        prompt = f'''As an expert book reviewer, please provide a complete summary, \
            key takeaways, and actionable items from the book {book_name}'''
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ {"role":"user", "content": prompt }]
    )
    return response.choices[0].message.content

# Create a Streamlit app
st.title("WisdomWing")

# Define a list of predefined book names
book_options = ["Rich Dad Poor Dad by Robert Kiyosaki",
                "How to win friends and influence people by Dale Carnegie",
                "The 7 Habits of Highly Effective People by Stephen Covey",
                "Thinking, Fast and Slow by Daniel Kahneman"]

# Create a dropdown menu for book selection
custom_book_name = st.text_input("Enter a custom book name (leave blank to select from below):")

# Create a dropdown menu for book selection, disabled if custom book name is not empty
selected_book = st.selectbox("Or Select a book:", book_options, disabled=bool(custom_book_name))

# Set the book name to the selected option from the dropdown menu or the custom book name
book_name = custom_book_name if custom_book_name else selected_book

# Get user selection for summary type
summary_type = st.selectbox("Select summary type:", ["Complete Summary", "Chapter-wise Summary"])

# Create a button to generate the response
if st.button("Generate"):
    response = generate_response(book_name, summary_type)
    st.write(response)