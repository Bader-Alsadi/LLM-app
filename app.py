import streamlit as st
from openai import OpenAI

# openai.api_key =st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key="sk-bhkn-oIEBZE1IkPHuZkAi2acBT3BlbkFJsGaF5VJgtaQQcQPkq15G")
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit app
st.title("Bader chat app")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def generate_response(user_input):
    # Append user message to the session state
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Call OpenAI's Chat Completion API
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=st.session_state["messages"]
    # )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state["messages"]
    )

    # Extract the assistant's reply
    # assistant_message = response["choices"][0]["message"]["content"]
    assistant_message = response.choices[0].message.content
    
    # Append assistant message to the session state
    st.session_state["messages"].append({"role": "assistant", "content": assistant_message})

    return assistant_message

user_input = st.text_input("You: ", "")

if user_input:
    response = generate_response(user_input)
    # st.write("Bot: " + response)

    for message in st.session_state["messages"]:
        role = "User" if message["role"] == "user" else "Bot"
        st.write(f"{role}: {message['content']}")

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])




# def get_gym_program(system_message, weight, tall, goal):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         temperature=0.7,
#         messages=[
#             {"role": "system", "content": f"{system_message}"},
#             {"role": "user", "content": f">>Bio stats: {weight}, {tall}\n\n>>Objective: {goal}"},
#         ]
#     )
#     return response.choices[0].message.content


# # User inputs and model parameters
# st.sidebar.header("Sbet parameters")
# prompt_message = "You are Sbet my GYM Trainer. \
#                     Based on my objective and my \
#                     Bio stats give me one week program. \
#                     Then add to it nutritionist advise for \
#                     the type of food and calories I need to consume."

# system_message = st.sidebar.text_area("System message:",
#                                       value=prompt_message)
# model_temp = st.sidebar.slider("Temp", step=0.01, min_value=0.0,
#                                max_value=2.0,
#                                value=1.0)
# max_token = st.sidebar.slider("Max Token", step=100, min_value=200,
#                               max_value=4000,
#                               value=512)

# st.sidebar.header("User based input:")
# goal = st.sidebar.text_input("User objective:",
#                              value="General fitness")
# weight = st.sidebar.number_input(
#     "Insert your weight", value=70, placeholder="Your weight in KG")
# tall = st.sidebar.number_input(
#     "How tall are you:", value=165, placeholder="Your length in CM")


# # Main page components
# st.title("🥗 Sbet the nutritionist")
# response = get_gym_program(system_message, weight, tall, goal)


# st.markdown(response)
