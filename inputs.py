
import os
import json
from dotenv import load_dotenv
import requests_oauthlib


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
    print(f"Request data to {res.url} status_code:{res.simport os
import requests
import json
from dotenv import load_dotenv
import requests_oauthlib
load_dotenv()tatus_code}")
    data = res.json()

    if res.status_code != 200:
        raise ValueError(f"Invalid response: {data['message']} .")
    return data'''
load_dotenv()

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

'''def get_tweets(user):
    my_auth = get_auth()
    url = f'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={user}=twitterapi&count=100&tweet_mode=extended'
    response = requests.get(url, auth=my_auth, stream=True)
    print(url, response)
    return response.json()'''

def searchTweets(query, lang, geo):
    '''
    Perform a query search request to Twitter with Tweepy. Parameters:
    - query: include a word or a complex query using operators
    - lang: language ISO code 639-1
    - geo: latitude, longitude and km or miles
    
    Returns a dataframe with the columns: query, date, id, user and text.
    '''
    print('Creating an empty dataframe with the first 10 tweets')
    try:
        count = 0
        #First request
        while count < 1:
            tweets = tweepy.Cursor(api.search,
                               q=query,
                               lang=lang,
                               geo=geo,
                               result_type='mixed').items(10)


            data = [[query,tweet.created_at, tweet.id, tweet.user.screen_name, tweet.text] for tweet in tweets]

            df_tw = pd.DataFrame(data=data, columns=['query','date', 'id', 'user', 'tweet_text'])
            print('Here you have your first 10 tweets')
            print(df_tw)

            count += 1

        #Add more tweets
        while count >= 1:
            tweets = tweepy.Cursor(api.search,
                                       q=query,
                                       lang=lang,
                                       geo=geo,
                                       result_type='mixed',
                                       max_id=df_tw.id.min()).items(1500)


            data = [[query, tweet.id, tweet.created_at, tweet.user.screen_name, tweet.text] for tweet in tweets]
            df2 = pd.DataFrame(data=data, columns=['query', 'id', 'date', 'user', 'tweet_text'])
            df_tw = df_tw.append(df2, sort=True)

            count += 1
            print('Adding 1500 to the dataframe')
            print('Your dataframe has a total of', df_tw.shape[0], 'tweets.')
            print('Oldest tweet is from', df_tw.date.min())

            return df_tw.to_csv('df_search.csv')
    except AttributeError:
        pass
    except NameError:
        pass