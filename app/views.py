from flask import Flask,render_template,request,jsonify, url_for
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():

    search_tweet = "natural disaster"
    
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    result = jsonify({"success":True,"tweets":t})

    # return render_template('index.html', rows = result)
    return "Hello Prakash"

# @app.route("/search/",methods=['GET','POST'])
# def search():

#     search_tweet = request.form.get("search_query")
    
#     # t = [[]]
#     t = []
#     tweets = api.search(search_tweet, tweet_mode='extended')
#     for tweet in tweets:
#         polarity = TextBlob(tweet.full_text).sentiment.polarity
#         subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
#         t.append([tweet.full_text,polarity,subjectivity])
#         # t.append(tweet.full_text)

#     return jsonify({"success":True,"tweets":t})

if __name__ == '__main__' : 
	app.run(debug=True)
#---------------------------------------------------------------------------






