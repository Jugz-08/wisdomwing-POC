import streamlit as st
from openai import OpenAI
     



#------------------Setting------------------
api_key_openai=st.secrets["api_key_openai"]
#------------------Setting------------------

client=OpenAI(api_key=api_key_openai,organization=st.secrets["organization"], project=st.secrets["project"],)

messages=st.empty()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def generate_response(book_name):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[ {"role":"user", "content":f"As an expert book reviewer, please provide the summary, key takeaways, and actionable items from the book {book_name}"}]
       
    )
    return response.choices[0].message.content


st.title("WisdomWing")

def display_messages():
    for message in st.session_state["messages"]:
        if message["role"]=="user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])

initial_prompts = {
    "book1":"Rich Dad Poor Dad by Robert Kiyosaki",
    "book2":"How to win friends and influence people by Dale Carnegie",
    "book3":"The 7 Habits of Highly Effective People by Stephen Covey",
    "book4":"Thinking, Fast and Slow by Daniel Kahneman"
}

placeholder=st.empty()

with placeholder.form(key='my_form'):
    col1,col2=st.columns(2)
    with col1:
        firstQ=st.form_submit_button(label="Rich Dad Poor Dad by Robert Kiyosaki",use_container_width=True)
        thirdQ=st.form_submit_button(label="The 7 Habits of Highly Effective People by Stephen Covey",use_container_width=True)
    with col2:
        secondQ=st.form_submit_button(label="How to win friends and influence people by Dale Carnegie",use_container_width=True)
        fourthQ=st.form_submit_button(label="Thinking, Fast and Slow by Daniel Kahneman",use_container_width=True)

if firstQ:
    st.session_state["messages"].append({"role":"user","content":initial_prompts["book1"]})
    ans=generate_response(initial_prompts["book1"])
    st.session_state["messages"].append({"role":"assistant","content":ans})
    display_messages()
    placeholder.empty()

if secondQ:
    st.session_state["messages"].append({"role":"user","content":initial_prompts["book2"]})
    ans=generate_response(initial_prompts["book2"])
    st.session_state["messages"].append({"role":"assistant","content":ans})
    display_messages()
    placeholder.empty()

if thirdQ:
    st.session_state["messages"].append({"role":"user","content":initial_prompts["book3"]})
    ans=generate_response(initial_prompts["book3"])
    st.session_state["messages"].append({"role":"assistant","content":ans})
    display_messages()
    placeholder.empty()

if fourthQ:
    st.session_state["messages"].append({"role":"user","content":initial_prompts["book4"]})
    ans=generate_response(initial_prompts["book4"])
    st.session_state["messages"].append({"role":"assistant","content":ans})
    display_messages()
    placeholder.empty()

def user_query():
    prompt=st.chat_input("")
    if prompt:
        st.session_state["messages"].append({"role":"user", "content":f"{prompt}"})
        answer=generate_response(prompt)
        st.session_state["messages"].append({"role":"assistant", "content":answer})
        st.session_state["messages"]=st.session_state["messages"][-100:]
        display_messages()
        placeholder.empty()

user_query()