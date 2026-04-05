# Create an Audiobook from a PDF

import subprocess
subprocess.run(["pip", "install", "PyPDF2", "pyttsx3"])


# Extract text from PDF
import PyPDF2

# open the pdf file
pdf_file = open("Module_03_Text_Classification.pdf", "rb")

# create a pdf reader object
reader = PyPDF2.PdfReader(pdf_file)

# extract text from all pages
text = ""
for page in reader.pages:
    text += page.extract_text()

print("Text extraction done!")
print("Total characters:", len(text))

# print the extracted text
print(text)


# Convert the Text into Speech
import pyttsx3

# create a speaker object
speaker = pyttsx3.init()

print("Speaker ready!")

# convert the text to speech
speaker.say(text)

print("Text converted to speech!")

# save the speech as a wav file
speaker.save_to_file(text, "audiobook.wav")
speaker.runAndWait()

print("Audio saved as audiobook.wav!")
