
import json
import playsound
from datetime import date
import os
import speech_recognition as sr
import random
import time
import datetime
import json
from main.data.speech.RealtimeSpeech import SpeechSynthesizer


class Initialisation:
	def __init__(self):

		# Define A Path for Json File Containing DB Data for User
		self.path = './user.json'
		# existence(variable -> checking for existence of path)
		self.existence = os.path.exists(self.path)

		# check_existence
		self.check_existence()
	
	def check_existence(self):
		# while existence
		if self.existence:
			self.runMain()
		
		# while existence not true
		else:
			self.welcomeUser()
			self.yourName()
	
	""" Task Execution """

	def speakData(self, data):
		try:
			SpeechSynthesizer(data)
		except:
			print(data)
	
	def listen_Data(self):
		
		try:

			# use the microphone as source for input.
			with sr.Microphone() as source:

				# Define the Recognizer
				r = sr.Recognizer()

				# the surrounding noise level
				r.adjust_for_ambient_noise(source, duration=0.2)

				# Use Pause Threshold
				r.pause_threshold = 1

				audio = r.listen(source)

				# Using google to recognize audio
				inputtext = r.recognize_google(audio)

				# Lower input text
				inputtext = inputtext.lower()

				# Replace empty spaces
				inputtext = inputtext.replace(" ", "")

				return inputtext

		except Exception as e:
			# print(e)
			# Say that again will be printed in case of improper voice
			print("Say that again please...")
			return self.listen_Data()

		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")

		except sr.RequestError as e:
			print(
				"Could not request results from Google Speech Recognition service{0}".format(e))

	def db_save(self, inputtext):

		dateCreated = str(datetime.date.today().day) + "/" + \
			str(datetime.date.today().month) + \
			"/" + str(datetime.date.today().year)
		jsonData = {"name": inputtext, "dateCreated": dateCreated}

		# Dump Data
		jsonString = json.dumps(jsonData)

		# Open Json File
		jsonFile = open("user.json", "w")

		# Write data
		jsonFile.write(jsonString)
		jsonFile.close()
	
	def startDocumentation(self, inputtext):
		try: 
			# Begin the app for marketing/explaining purposes
			self.speakData(
				f"{inputtext}, Follow through the documentation, and once you are done, just close the window and I'll be ready.")
			# Change Active Directory
			os.chdir("app")
			# if node_modules exists
			if os.path.isdir("node_modules"):
				# Start the app
				os.system("npm start")

			self.speakData("Installing Desktop App Packages. Executing Data. Predicting Output. Loading files... ")
			self.speakData("This will take some time depending on your internet connection. Please wait. ")
			# Install node_modules/electron packages    
			os.system("npm install --save-dev electron")
			# Start the app
			self.speakData("And Done. Starting the app. ")
			os.system("npm start")
		
		except Exception as AppStartBundleException:
			self.speakData(AppStartBundleException)
			self.speakData("Sorry. I have encountered an issue. Please try again later. For now you can manually try installing packages. Follow these instructions. ")
			self.speakData("Open your terminal.")
			self.speakData("Go to the directory where you installed Seven.")
			self.speakData("Change Directory to app by typing cd app")
			self.speakData("Type npm install --save-dev electron")
			self.speakData("Try again")

			pass

	""" Proccess Execution """
	def runMain(self):
		# json_file(variable -> opening the file)
		with open(self.path) as json_file:

			# data(variable -> reading the file)
			data = json.load(json_file)
			
			# close json_file
			json_file.close()

			# cd main/python main.py (redirect to main)
			os.chdir("main")
			os.system("python main.py")
	
	def welcomeUser(self):
		# welcome_user(variable -> welcome user)
		# Introduce Seven
		response = random.choice(["A new user I see. Welcome. Welcome to Seven. Allow me to introduce myself. I am Seven, made by Rishabh Mishra, Sarthak Rawool, and Shubham Mishra. And about me well, I'm a damn brilliant guy! Here let me get you through setup", "Hey. I am Seven. Let me introduce myself, As you know me I am Seven. I was made by a few brilliant idiots Rishabh Mishra, Shubham Mishra, Sarthak Rawool. The Guys, eh? Anyways, let me get you through setup. ", "Here's looking at you Kid. I'm Seven. I was made by Rishabh Mishra, Shubham Mishra, and Sarthak Rawool, Ya. Let me get you through setup. "])
		self.speakData(response)

	def yourName(self):
		# your_name(variable -> your name)
		# Introduce your name

		self.speakData("What is your name? ")

		# your_name(variable -> your name)
		# Get your name

		self.your_name = self.listen_Data()

		if self.your_name:
			self.speakData("Is {} your name? ".format(self.your_name))
			
			self.your_name_confirm = self.listen_Data()
			if "yes" in self.your_name_confirm.lower() or "yeah" in self.your_name_confirm.lower():
				self.speakData("Okay. Let's get started. ")          
				
			else:
				self.yourName()
		
		self.db_save(self.your_name)      
		self.startDocumentation(self.your_name)
		print("Processing, it will take less than a minute...")
		os.system("python ../main/main.py")



###############################
# Run Intialiasation Process
###############################

Initialisation = Initialisation()
