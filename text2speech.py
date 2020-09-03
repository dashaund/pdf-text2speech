import sys
from gtts import gTTS
import pdftotext

if len(sys.argv) == 1:
    print("Please input the filename as argument")
    sys.exit()
elif len(sys.argv) > 2:
    print("This program only takes one file, please try again")
    sys.exit()
else:
    filename = sys.argv[1]

with open(filename, "rb") as f:
    pdf = pdftotext.PDF(f)

text = ""
for i in pdf:
    text = text + i

speech = gTTS(text=text, lang='es')
speech.save("Generated Speech.mp3")