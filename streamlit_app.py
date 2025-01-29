import streamlit as st
from streamlit_feedback import streamlit_feedback

def streaming_chatbot():

    st.title("💬 Streaming Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "feedback_key" not in st.session_state:
        st.session_state.feedback_key = 0

    feedback_kwargs = {
        "feedback_type": "faces",
        "optional_text_label": "Please provide extra information",
    }

    for n, msg in enumerate(st.session_state.messages):
        st.chat_message(msg["role"]).write(msg["content"])

        if msg["role"] == "assistant" and n > 0:
            feedback_key = f"feedback_{int(n/2)}"

            if feedback_key not in st.session_state:
                st.session_state[feedback_key] = None

            streamlit_feedback(
                **feedback_kwargs,
                key=feedback_key,
            )

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = "This is a sample response!"

            message_placeholder.markdown(full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
        streamlit_feedback(
            **feedback_kwargs, key=f"feedback_{int(len(st.session_state.messages)/2)}"
        )


streaming_chatbot()
