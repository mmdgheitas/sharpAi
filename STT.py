import speech_recognition as sr
import pyttsx3 


# Initialize the recognizer 
r = sr.Recognizer() 



while(1): 
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input 
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say ",MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")




# import speech_recognition as sr

# # Initialize the recognizer
# recognizer = sr.Recognizer()

# # Capture audio from the microphone
# with sr.Microphone() as source:
#     print("Please speak into the microphone...")
#     audio = recognizer.listen(source)

#     try:
#         # Recognize speech using Google Web Speech API
#         text = recognizer.recognize_google(audio)
#         print("You said: " + text)
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand the audio.")
#     except sr.RequestError:
#         print("Sorry, my speech service is down.")