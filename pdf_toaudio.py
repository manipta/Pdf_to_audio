import PyPDF2,pyttsx3
import streamlit as st
def s():
    speak=pyttsx3.init()
    ftext=""
    for pages in range(pdfReader.numPages):
        text=pdfReader.getPage(pages).extractText()
        speak.say(text)
        speak.runAndWait()
        ftext=ftext+text 
    if(st.button("Download Audio")):
        speak.save_to_file(text,'PdfToAudio.mp3')
        speak.runAndWait() 
    speak.stop()

columns = st.columns((1, 1, 4))
columns[2].header("PDF TO SPEECH!!")    
path=st.file_uploader("Please Upload a single pdf file",type="pdf")
if path:
    pdfReader=PyPDF2.PdfFileReader(path)
    st.markdown("----", unsafe_allow_html=True)
    columns = st.columns((2, 1, 2))
    start = columns[1].button('Speak !')
    st.markdown("----", unsafe_allow_html=True)
    
    if(start):
        s()
    
    
        