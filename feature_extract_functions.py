import language_check
import enchant
from textblob import TextBlob
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import PersonalityInsightsV2
from watson_developer_cloud import ToneAnalyzerV3

# Need to specify a username and password, from the IBM Bluemix Website
speech_to_text = SpeechToTextV1(username= "username",password= "pw", x_watson_learning_opt_out=False)
tone_analyzer = ToneAnalyzerV3(username= "username",password= "pw",version='2016-05-19')
tool = language_check.LanguageTool('en-GB')
d = enchant.Dict('en_US')
audio_loc = 'path_to_wav_file.wav'

def check_grammar(text):
	# Takes in text, and returns number of grammatical errors
	return len(tool.check(text))

def check_spelling(text):
	# Takes in text, and returns number of spelling errors
	errors = 0
	for word in text:
		if not d.check(word):
			errors += 1
	return errors

def check_sentiment(text):
	# Takes in text, and returns a tuple of the (polarity, sentiment) of the text
	blob = TextBlob(text)
	polarity = blob.polarity
	sentiment = blob.sentiment
	return (polarity, sentiment)

def transcribe(audio_loc):
	with open(audio_loc,'rb') as audio_file:
		transcription = speech_to_text.recognize(
			audio_file, content_type='audio/wav', timestamps=True,model='en-US_BroadbandModel',
			word_confidence=True,continuous = True)
		# print(transcription)
		transcript = transcription['results'][0]['alternatives'][0]['transcript']
		return transcript

def analyze_tones(transcript):
	# Takes in a transcript, returns an analysis of that transcript
	tone_analysis = tone_analyzer.tone(text=transcript)
	return tone_analysis


