from textblob import TextBlob
import matplotlib.pyplot as plt
import sys, tweepy

def percentage(part, whole):
    return 100 * float(part)/float(whole)

consumerkey = ""
consumersecret = ""
accessToken = ""
accessTokenSecret = ""

authenticate = tweepy.OAuthHandler(consumer_key=consumerkey, consumer_secret=consumersecret)
authenticate.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(authenticate)
hastag = input('enter the hastag for analysis: ')
nOT = int(input('Enter the number of tweetes you want to analyse: '))

tweets = tweepy.Cursor(api.search, q=hastag).items(nOT)
positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:

    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    if analysis.sentiment.polarity == 0:
        neutral += 1
    elif analysis.sentiment.polarity < 0.00:
        negative += 1
    elif analysis.sentiment.polarity > 0.00:
        positive += 1
positive = percentage(positive, nOT)
negative = percentage(negative, nOT)
neutral = percentage(neutral, nOT)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')
print(f'The maximum reaction  of the {hastag} from the {nOT} tweets is:')
if polarity == 0:
    print('Neutral')
elif polarity > 0:
    print('Positive')
elif polarity < 0:
    print('Negative')

labels = ['positive [' + str(positive) + '%]', 'Negative [' + str(negative) + '%]',
          'Neutral [' + str(neutral) + '%]']
size = [positive, negative, neutral]
color = ['green', 'red', 'blue']
patches, texts = plt.pie(size, colors=color, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title(f'The maximum reaction  of the {hastag} from the {nOT} tweets is:')
plt.axis('equal')
plt.tight_layout()
plt.show()
