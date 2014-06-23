'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'JbmtGuxIsZKc8gsZ5o7zo2NHw'
MY_CONSUMER_SECRET = '3i71Rks7rfm8Qyob1IcslaU8VbvdNLis06Jc0LF85DNFo1b1Pg'
MY_ACCESS_TOKEN_KEY = '2584109700-R46Szl0rc0eh0NwZscFicxoEAQH6GiCqdQIIqgO'
MY_ACCESS_TOKEN_SECRET = 'BkWOfRPJioIXXpGlvKRdSGULEQZNKg58icq81arOZTwih'

SOURCE_ACCOUNTS = ["zschomburg", "kellyschirmann", "salt_lock", "EmilyKendalFrey", "MathiasSvalina", "sexualboat", "poetry_daily", "poetry_society", "poetryfound"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 4 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "garbage_poet" #The name of the account you're tweeting to.
