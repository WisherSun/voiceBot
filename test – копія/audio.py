import speech_recognition as sr
import subprocess
import gpt
import webbrowser
import gtts
import os
recognizer = sr.Recognizer()
def capture_voice_input():
    with sr.Microphone() as source:
        print("Слухаю...")
        audio = recognizer.listen(source)
    return audio
def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language = 'uk-UK')
        print("Ви сказали:" + text)
    except sr.UnknownValueError:
        text = ""
        print("Вибачте, я не зрозумів, повторіть ще раз")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text
def process_voice_command(text):
    if "привіт" in text.lower():
        print("Привіт! як я можу вам допомогти?")
    elif "як справи" in text.lower():
        print('погано')
    elif "прощавай" in text.lower():
        print("До побачення!Гарного дня!")
    elif "калькулятор" in text.lower():
        subprocess.call(['calc'])
    elif "джарвіс" in text.lower():
        result = gpt.generate(text)
        myobj = gtts.gTTS(text=result,lang='uk', slow=False)
        myobj.save('result.mp3')
        os.system('result.mp3')
        return result
       
    elif "логіка" in text.lower():
        webbrowser.open("https://learn.logikaschool.com/login")
    elif "код" in text.lower():
        code = gpt.generate(text)
        with open('generated_code.py','w',encoding='utf-8') as file:
            file.write(code)
def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        return process_voice_command(text)
if __name__ == '__main__':
    main()