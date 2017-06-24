import language_check
import enchant
from textblob import TextBlob

tool = language_check.LanguageTool('en-GB')
d = enchant.Dict('en_US')

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

