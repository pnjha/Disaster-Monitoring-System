from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'HcWuxEn7uMvsBth3z9oBNBWkQ'
consumer_secret = 'f5rM7IDFQF4yGCWa1VTvrOCukuHl3DPyeBw38E6hthiTRFQnxi'

access_token = '3065963708-IxpW6kwNtbp77qTHV6lCpq4MLny5LF3N23XlQfN'
access_token_secret = '8shltRS8a7DjjNd7IK5Pc2AYiSQvBzC7TIiUb4gC1SZON'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('/templates/index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})


#---------------------------------------------------------------------------


