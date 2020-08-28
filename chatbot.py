import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import re
import random
import requests, json
import urllib.request
import urllib.parse
import pyautogui
from PIL import Image, ImageGrab

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
My_dict = ['wake up', 'hello']
# link_list = {'search on youtube', 'in youtube', 'youtube', 'on youtube', 'search youtube'}
# name_list = ['what is your name', 'who are you', 'may i have your name', 'what is your name again', 'again say', 'again', 'say again', 'again say your name', 'may i have your name', 'what do you call yourself', 'may i ask your name']

def speak(audio):
	global name_list
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		speak("Good Morning")
	elif hour >= 12 and hour < 18:
		speak("Good Afternoon")
	else:
		speak("Good Evenning")

	speak("I am Tokyo, How can I help You")

def takeCommand():
	# It take input and return output
	global name_list
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		r.energy_threshold = 350
		audio = r.listen(source)

	try:
		print("recognizing...")
		query = r.recognize_google(audio, language='en-us')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Say Again")
		return "None"
	return query

def take_break(content):
	global My_dict
	return total_time

def task_kill(task):
	browserExe = f"{task}.exe"
	os.system("taskkill /f /im "+browserExe)

def celcius_temp():
	
	return celcius

def task_kill(task):
	browserExe = f"{task}.exe"
	os.system("taskkill /f /im "+browserExe)



def se_t(q1):
	pass
	
		
	

if __name__ == "__main__":
	wishMe()
	while True:
		query = takeCommand().lower()
		if 'search' in query:
			webbrowser.open(f"https://www.google.com/search?sxsrf=ALeKk02e28IzxuXboTw6Xc3ohzJ5dXGK9A%3A1591436642597&source=hp&ei=YmXbXrTMIqDA3LUP4diEiAE&q={query}&btnK=Google+Search")
			speak(f"I found some information, check it")
		elif 'what is' in query or 'who is' in query or 'where is' in query:
			speak('searching...')
			# query = query.replace("what is", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			print(results)
			speak(results)

		elif 'who are you' in query or 'what is your name' in query:
			speak(f"I am Tokyo your assistant")

		elif 'search on youtube' in query or 'video' in query or 'search youtube' in query:
			try:
				for pattern in link_list:
					pat = pattern.split()
					pattern_list = "+".join(pat)
				link = re.split(r'\s', query)
				lin_add = "+".join(link)
				pattern_list = lin_add.replace(pattern_list, "")
				webbrowser.open(f"https://www.youtube.com/results?search_query={pattern_list}")	

			except Exception as e:
				print(e)

		elif 'play' in query:
			query = query.replace("play", "")
			query_string = urllib.parse.urlencode({"search_query": query})
			html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
			x = html_content.read().decode()
			search_results = re.findall(r'href=\"\/watch\?v=(.{11})', x)
			webbrowser.open(f"http://www.youtube.com/watch?v={search_results[0]}", new=0)
			try:
				i = 1
				while True:
					q1 = takeCommand()
					if "next" in q1:
						i += 2
						if len(search_results) < i:
							break
						browserExe = "firefox.exe"
						os.system("taskkill /f /im "+browserExe)
						webbrowser.open(f"http://www.youtube.com/watch?v={search_results[i]}", new=0)
					
					elif "exit" in q1:
						break	
				se_t(q1)
			except Exception as e:
				print(e)
			

		elif 'play music' in query:
			music_dir = "Choose your directory(ex:c://music)"
			songs = os.listdir(music_dir)
			# print(songs)
			os.startfile(os.path.join(music_dir, random.choice(songs)))

		elif 'what time it is' in query or 'time' in query or 'time now' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"The time is {strTime}")

		elif 'open browser' in query:
			browserPath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
			os.startfile(browserPath)

		elif 'change voice' in query:
			engine.setProperty('voice', voices[0].id)
			speak("Voice changed")

		elif 'take a break' in query:

			speak('As your wish')
			try:
				word_split = [word for word in query.split(" ") if word.isdigit()]
				collect_integer = int("".join(word_split)) #convert string to int
				total_time = collect_integer * 10
				g = [count for count in range(total_time)]
				print(g)
				# My_dict = ['wake up', 'hello']
				for word_list in My_dict:
					print(word_list)
				try:
					content = takeCommand()
					if content in My_dict:
						time.sleep(0)
						speak("Hello")
					else:
						time.sleep(total_time)
				except Exception as e:
					print(e)
				take_break(content)
			except Exception as e:
				print(e)

		elif 'weather' in query:
			try:
				query = query.replace("temperature", "")
				url = f"http://api.weatherapi.com/v1/current.json?key=5d08daedb17e430eac672747200606&q={query}"
				response =requests.get(url).text
				my_json = json.loads(response)
				arts = my_json["current"]
				condi = my_json["current"]["condition"]["text"]
				humidity = (arts["humidity"])
				celcius = ((arts["temp_c"]))
				speak(f"The temperature of {query} is {celcius}, it is {condi} day and the humidity is {humidity}")
				celcius_temp()
			except Exception as e:
				print(e)
		
		elif 'close' in query:
			task = query.replace("close", "")
			task_kill(task)

		elif 'screenshot' in query:
			speak(f"Ok its my duty")
			pyautogui.hotkey('winleft', 'PrtScr')



		elif 'bye' in query:
			exit()

