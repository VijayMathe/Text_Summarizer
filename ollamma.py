import google.generativeai as genai
import streamlit as st

from dotenv import load_dotenv
import os

load_dotenv()

gap = os.getenv('g_key')

genai.configure(api_key=gap)

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

#  = input("Enter the text here")
# paragraph = "Vijay Mathe is a highly skilled and dedicated technology enthusiast with a strong academic background in Electronics and Telecommunication Engineering from Vishwakarma Institute of Technology. With proficiency in multiple programming languages including C/C++, Java, and Python, Vijay excels in areas such as data structures, algorithms, machine learning, and deep learning. His practical experience includes mentoring students, solving complex problems on platforms like LeetCode and Codeforces, and developing innovative projects such as a financial inclusion app for visually impaired people and a heart disease prediction model. Vijay’s commitment to continuous learning is evident through his involvement in advanced courses and his active participation in research and volunteer activities, demonstrating both technical prowess and a passion for community service."

# response = chat.send_message("Summarise this paragraph \n" + paragraph)

# print('\n\n')
##

# print(response.text)


def main():
    st.title("Text summarizer")
    paragraph = st.text_area("Enter the paragraph here to summarize")

    if paragraph:
        if st.button("Summarize"):
            summary = chat.send_message("Summarise this paragraph (reduce words to the half of its total words)\n" + paragraph)
            st.subheader("Summary")
            st.write(summary.text)


if __name__ == '__main__':
    main()