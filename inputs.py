
import os
import requests
import json
from dotenv import load_dotenv
import requests_oauthlib
load_dotenv()


def get_auth():

    load_dotenv()
    CONSUMER_KEY=os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET=os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
    ACCESS_SECRET=os.getenv("ACCESS_SECRET")
    my_auth=requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET,ACCESS_TOKEN, ACCESS_SECRET)
    return my_auth


'''def get_tweet(endpoint, apiKey=os.getenv('CONSUMER_KEY'), query_params={}):
    tweet_fields = "tweet.fields=lang,author_id"

    ids = "ids=1303677963200798720,1255542774432063488"
    baseUrl = "https://api.twitter.com/1.1/statuses/retweets/:id.json/"
    url = f"{baseUrl}{endpoint}"
    headers= {"Authorization": "Bearer {ApiKey}"}
    res=requests.get(url, params=query_params, headers=headers)
    print(f"Request data to {res.url} status_code:{res.status_code}")
    data = res.json()

    if res.status_code != 200:
        raise ValueError(f"Invalid response: {data['message']} .")
    return data'''

def Split_Tweets():
    all_tweets=Gather_Tweets()
    split= []
    for tweets in all_tweets:
        for tweet in tweets:
            Split_Tweets=tweet_split(" ")
            split.append(Split_Tweets)
    return split


def Sort_Covid():
    sort_list=Split_Tweets()
    cov= []
    for sentence in sort_list:
        for word in sentence:
            if word.startswith("Coronavirus") or ("Covid"):
                cov.append(word)
    return cov

def missing_value_of_data(df):
    total=df.isnull().sum().sort_values(ascending=False)
    percentage=round(total/df.shape[0]*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])

def get_tweets(user):
    my_auth = get_auth()
    url = f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={user}&count=100&tweet_mode=extended'
    response = requests.get(url, auth=my_auth, stream=True)
    print(url, response)
    return response.json()