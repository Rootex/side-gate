__author__ = 'Sotaya'

'''
This module will enable us to provide reading the questions and options in audio
in case the users do not want to read, they can listen instead and provide the answer.
'''

import pyttsx


class Reader:

    def __init__(self):
        self.engine = pyttsx.init()
        self.engine.setProperty('rate', 70)

    def speak(self, text):
        if text != "":
            self.engine.say(text)

        self.engine.runAndWait()

#if __name__ == '__main__':
#    A = Reader()
#    A.speak("Whats up!")