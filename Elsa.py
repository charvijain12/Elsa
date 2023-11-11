#!/usr/bin/env python
# coding: utf-8

# # Elsa - Relaxation Bot to help improve Mental Health
# 
# ### Author - Charvi Jain

# In[8]:


from gtts import gTTS
import os
import random
import speech_recognition as sr
import pyttsx3
import datetime

def load_stress_keywords(filename='stress_keywords.txt'):
    with open(filename, 'r') as file:
        stress_keywords = [line.strip() for line in file]
    return stress_keywords

stress_keywords = load_stress_keywords()

try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def greet():
        hour = int(datetime.datetime.now().hour)
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Time:", current_time)

        if hour >= 0 and hour < 12:
            greeting = "Good Morning!"
        elif hour >= 12 and hour < 18:
            greeting = "Good Afternoon!"
        else:
            greeting = "Good Evening!"

        print("Elsa:", greeting)
        speak(greeting)
        speak("Welcome, I am your personal relaxation bot, Elsa")
        speak("How can I help you today?")
        print("Speak one of the words from Words Corpus")
    greet()

    # Define relaxation techniques
    relaxation_options = {
        'Deep Breathing': 'Practice deep breathing exercises. Inhale slowly for 4 seconds, hold for 4 seconds, exhale for 4 seconds. Repeat.',
        'Guided Imagery': 'Try guided imagery. Close your eyes and imagine a peaceful place. Focus on the details.',
        'Progressive Muscle Relaxation': 'Practice progressive muscle relaxation. Tense and then relax each muscle group in your body, starting from your toes up to your head.',
        'Mindful Meditation': 'Engage in mindful meditation. Focus on your breath and bring your attention back whenever your mind starts to wander.',
        'Aromatherapy': 'Use aromatherapy. Inhale the calming scent of lavender, chamomile, or eucalyptus.',
        'Warm Bath': 'Take a warm bath. Allow the warm water to relax your muscles and calm your mind.',
        'Listening to Calming Music': 'Listen to calming music. Choose music with a slow tempo to help reduce stress.',
        'Journaling': 'Start journaling. Write down your thoughts and feelings to gain clarity and release emotional tension.',
        'Yoga': 'Practice yoga. Gentle yoga poses and stretches can promote relaxation and reduce stress.',
        'Laughter Therapy': 'Engage in laughter therapy. Watch a funny movie or spend time with people who make you laugh.',
        'Nature Walk': 'Take a nature walk. Spending time in nature can have a calming and rejuvenating effect.',
        'Visualization': 'Use visualization techniques. Imagine a peaceful scene or visualize yourself overcoming challenges.',
        'Coloring': 'Coloring can be a relaxing activity. Use coloring books or apps with calming designs.',
        'Self-Massage': 'Give yourself a self-massage. Focus on areas with tension and use gentle strokes.',
        'Breath Counting': 'Practice breath counting. Inhale deeply, count to four, exhale slowly. Repeat for several breaths.',
        'Positive Affirmations': 'Repeat positive affirmations. Remind yourself of your strengths and abilities.',
        'Social Connection': 'Connect with loved ones. Spend time with friends or family members who provide support.',
        'Disconnect': 'Take a break from technology. Unplug for a while to reduce information overload and screen time.',
        'Tea Routine': 'Create a tea-drinking routine. Enjoying a warm cup of herbal tea can be soothing.',
        'Stretching': 'Engage in gentle stretching exercises. Stretching can help release muscle tension and improve flexibility.',
    }

    # Function to check for stress keywords in user input
    def check_for_stress_keywords(user_input):
        return any(keyword in user_input.lower() for keyword in stress_keywords)

    # Function to get a response from the bot
    def get_bot_response(user_input):
        # Default response from the bot
        bot_response = "I'm not sure how to respond to that. Can you be more specific?"

        # If the user expresses stress, provide options
        if check_for_stress_keywords(user_input):
            print("Elsa: It sounds like you're going through a tough time. I'm here for you.")
            speak("It sounds like you're going through a tough time. I'm here for you.")
            print("Elsa: Here are some relaxation tips that might help:")
            speak("Here are some relaxation tips that might help, Please look at the screen:")
            for option, description in relaxation_options.items():
                print(description)
            return "I'm here to help you. Take care."

        return bot_response

    # Function to speak the bot's response
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    while True:
        # Initialize the speech recognition
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("You: Listening...")
            try:
                # Listen to the user's speech
                audio = recognizer.listen(source, timeout=5)
                user_input = recognizer.recognize_google(audio).lower()
                print("You:", user_input)

                # Exit the loop if the user says 'exit'
                if 'exit' in user_input or 'bye' in user_input:
                    speak("Goodbye!")
                    break

                # Get the bot's response
                bot_response = get_bot_response(user_input)

                # Print and speak the bot's response
                print("Elsa:", bot_response)
                speak(" " + bot_response)

            except sr.UnknownValueError:
                print("Elsa: Sorry, I couldn't understand that. Can you repeat?")
                speak("Sorry, I couldn't understand that. Can you repeat?")

            except sr.RequestError:
                print("Elsa: There was an error with the speech recognition service. Please try again later.")
                speak("There was an error with the speech recognition service. Please try again later.")

except Exception as e:
    print(f"An error occurred: {e}")


# In[ ]:




