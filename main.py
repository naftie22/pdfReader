import pyttsx3
import PyPDF2

book = open('Jack Welch.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(8, 162):
    page = pdfReader.getPage(10)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()