## Forward Tweets to Telegram with a bot

<b>What does this ? </b>

Follow the tweets in real time from any user

<b>Variables</b>

`API_KEY` , `API_SECRET_KEY` , `ACCESS_TOKEN` , `ACCESS_SECRET_TOKEN`  

`TWITTER_USERNAME` : the twitter username of whom you wish to receive their posts

`TOKEN` : Token from @BotFather

`CHAT_ID` : 

<b>The first is the first</b>

Request a [developer account]( https://developer.twitter.com/  ) on Twitter and get access token and API keys
the approval process takes a day or two

<img src="/image/20210730_011957.png"/>

They create a new application and add the option to "Read + Write + Direct Messages" in the permits

<img src="/image/20210729_135344.png"/>

Then generate and save the access tokens and keys

<details> 
<summary><b>Deploy on Heroku</b></summary> <br> 
<a href="https://heroku.com/deploy?template=https://github.com/inDemocratic/Forward-tweet-bot"> <img height="28px" width="164px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku"> </a> 
</details>


[tweepy documentation](https://docs.tweepy.org/en/latest/streaming.html?highlight=Stream#using-stream)

If you want more information you can rely on [this blog](https://platzi.com/blog/extraer-datos-twitter/)
