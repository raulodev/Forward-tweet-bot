
import config
import tweepy
import json
import threading

from tweepy import Stream

from tweepy.streaming import StreamListener

from tweepy import OAuthHandler

from telegram.ext import Updater , CommandHandler 

from telegram import Bot 


'''
          Authenticate
'''

auth = OAuthHandler(
	config.API_KEY,
	config.API_SECRET_KEY
	)

auth.set_access_token(
	config.ACCESS_TOKEN,
	config.ACCESS_TOKEN_SECRET
	)
api=tweepy.API(auth)


"""
Write the name of the user from whom we want to receive 
their tweets in real time in this case "TwitterDev"

"""

username="TwitterDev"

"""
get user id
"""
user = api.get_user(username)
user_id = str(user.id)

"""
this class will transmit the data of each new tweet 
made by the user
"""


class MyListener(StreamListener):
	
	def on_data(self,data):
		try:
			
			"""
			Get the tweet data
			"""
			decode=json.loads(data)
						
			tweet_id=decode["id"]
			
			tweet_text= decode["text"]			
			name_creator= decode["user"]["screen_name"]
									
			reply= decode["in_reply_to_status_id"]
			
                        """
                        This to prevent the bot from sending me 
                        the tweet every time someone retweets it

                        if tweet_text[:2]!="RT"

                        """			
			
			if tweet_text[:2] !="RT" and reply == None:
					
				
				bot = Bot(token=config.TOKEN)
				
				"""
				Create tweet link
				"""
				
				
				url=f"https://twitter.com/{name_creator}/status/{tweet_id}"
				"""
				send message to Telegram chat
				"""
				
				bot.send_message(
		                    chat_id=config.CHAT_ID   , 
		                    text=
		                    f"<i>{tweet_text}</i>"
		                    f'\n\n<b><a href="{url}"> {name_creator}</a></b>',
		                    parse_mode="html",
		                    disable_web_page_preview = True)
			
			return True
		
		except Exception as e:
			
			print(e)
		
		return True

def Sthread():
	

	"""
	create the transmission and 
	create filter passing it as a 
	parameter the user_id
	"""			
	
	twitter_stream=Stream(auth,MyListener())
	
	"""
	filter
	"""
	
	twitter_stream.filter(follow=[user_id])
	

def start(Update,context):
	
	Update.message.reply_text("Hello, When I find a new tweet I will send it to you") 


if __name__ == "__main__":
	
	updater=Updater(token=config.TOKEN , use_context=True)
	
	update = Updater
	dp = updater.dispatcher
	
	"""
	Thread so that the transmission 
	of twitter data does not affect 
	the other functions of the bot
	"""
	
	t1 = threading.Thread(target=Sthread)
	
	t1.start()
	
	dp.add_handler(CommandHandler('start', start))	
	
	
	
	updater.start_polling()
	print("Bot running")
	updater.idle()
	
