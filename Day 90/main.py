import PyPDF2 as Reader
from gtts import gTTS
import os
from playsound import playsound


filename = 'book.pdf'
try:
    os.mkdir(filename.split('.')[0])
except:
    pass
with open(filename, 'rb') as file:
    pdf = Reader.PdfFileReader(file)
    print(pdf.numPages)
    os.chdir(filename.split('.')[0])
    for num in range(pdf.numPages):
        page = pdf.getPage(num)
        text = page.extractText()
        print(text)
        tts = gTTS(text)
        savefile = f'{str(num)}.mp3'
        tts.save(savefile)
        playsound(savefile)