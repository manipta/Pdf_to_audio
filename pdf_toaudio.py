import PyPDF2,pyttsx3
import keyboard as kb
import streamlit as st
def d():
    speak=pyttsx3.init()
    ftext=""
    for pages in range(pdfReader.numPages):
        text=pdfReader.getPage(pages).extractText()
        ftext=ftext+text 
    speak.save_to_file(ftext,'PdfToAudio.mp3')
    speak.runAndWait() 
    speak.stop()
def s():
    flag=0
    speak=pyttsx3.init()
    ftext=""
    for pages in range(pdfReader.numPages):
        text=pdfReader.getPage(pages).extractText()
        speak.say(text)
        speak.runAndWait()
        if(kb.read_key()=="s"):
                flag=1
                break
        ftext=ftext+text 
    if(st.button("Download Audio")):
        speak.save_to_file(ftext,'PdfToAudio.mp3')
        speak.runAndWait() 
    speak.stop()

columns = st.columns((1, 1, 4))
columns[2].header("PDF TO SPEECH!!")    
path=st.file_uploader("Please Upload a single pdf file",type="pdf")
if path:
    pdfReader=PyPDF2.PdfFileReader(path)
    st.markdown("----", unsafe_allow_html=True)
    columns = st.columns((2, 1,1, 2))
    start = columns[1].button('Speak !')
    end = columns[2].button('Download !')
    st.markdown("----", unsafe_allow_html=True)
    st.markdown("**NOTE** : You can't stop once audio is played. So don't Play if audio is long, else you need to close this tab.\nIf you know how to fix it, you are most welcome to fix it. Go on my [repo](https://github.com/manipta/Pdf_to_audio/blob/main/pdf_toaudio.py) pls.Thnx.", unsafe_allow_html=True)
    
    if(start):
        s()
    if(end):
        d()
    
        
                