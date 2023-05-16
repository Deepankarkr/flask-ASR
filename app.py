from random import random
from urllib import request
from flask import Flask, render_template, request, redirect, jsonify
import random
import speech_recognition as sr
app=Flask(__name__)
import wave

def convert_to_hindi(number):
    hindi_digits = {
        '0': '०',
        '1': '१',
        '2': '२',
        '3': '३',
        '4': '४',
        '5': '५',
        '6': '६',
        '7': '७',
        '8': '८',
        '9': '९'
    }

    hindi_number = ''.join(hindi_digits.get(digit, digit) for digit in str(number))

    hindi_number = hindi_number[::-1]
    hindi_number = ','.join(hindi_number[i:i+3] for i in range(0, len(hindi_number), 3))
    hindi_number = hindi_number[::-1]

    return hindi_number


@app.route('/', methods=['GET','POST'])
def indx():
        number = convert_to_hindi(random.randint(1,10))
        times = convert_to_hindi(random.randint(1,10))
        transcript = "_"
        # if request.method == "POST":
        #         if "file" not in request.files:
        #                 return redirect(request.url)
        #
        #         file = request.files["file"]
        #         if file.filename == "":
        #                 return redirect(request.url)
        #
        #         if file:
        #                 recognizer = sr.Recognizer()
        #                 audioFile = sr.AudioFile(file)
        #                 with audioFile as source:
        #                         data = recognizer.record(source)
        #                 transcript = recognizer.recognize_google(data, key=None,language="mr-IN")
        #
        #                 if number*times==int(transcript):
        #                        transcript="right answer:"+ str(transcript)
        #                 else:
        #                        transcript="wrong answer:"+ str(transcript)
        #                 return render_template("head.html",number=number,times=times,transcript=transcript)
        return render_template("base.html",number=number,times=times,transcript=transcript)


@app.route('/recording', methods=['GET','POST'])
def indx1():
    if request.method=='POST':
        if 'audio_data' in request.files:
            audio_file = request.files['audio_data']
            media_details = {
                'filename': audio_file.filename,
                'content_type': audio_file.content_type,
                'size': len(audio_file.read()),
            }

            print(media_details)
            # recognizer = sr.Recognizer()
            # audioFile = sr.AudioFile(audio_file)
            # with audioFile as source:
            #     data = recognizer.record(source)
            #     transcript = recognizer.recognize_google(data, key=None,language="mr-IN")
            # print(transcript)
            return str("test"), 200
        else:
            return 'No audio file received', 400
    else:
        return 'GET Not Allowed', 400

if __name__ == '__main__':
    app.run(port=3000,debug=True)