# speech to text
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def speech_rec():
    while True:
        try:
            with sr.Microphone() as source2:
                # the listening and recognizing text
                r.adjust_for_ambient_noise(source2, duration=0.3)
                audio2 = r.listen(source2)

                Atext = r.recognize_google(audio2, language="en-UK")

                return Atext

        except sr.RequestError as e:
            print("\n", "could not request results:", e)

        except sr.UnknownValueError:
            print("\n", "unintelligible")


def clear_op():
    with open("op.txt", "w") as f:
        f.write("")


if __name__ == "__main__":
    while True:
        text = speech_rec()
