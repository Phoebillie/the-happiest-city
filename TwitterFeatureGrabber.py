import json
import re
from nltk.tokenize import TweetTokenizer


class FeatureGrabber:

    def __init__(self):
        self.tknzr = TweetTokenizer()
        self.phrase_list = []

    def convert2json(self, line):
        """

        @rtype: json 
        """

        if line[-1] == '\n':
            line = line[:-1]
        if line[-2:] == ':[': # first line
            return None
        elif line[-2:] == ']}': # finnal line
            return json.loads(line[:-2])
        elif line[-2:] == '},': # common twitter line 
            return json.loads(line[:-1])
        else:
            print(line[-5:])
            raise ValueError('Irregular line found')
            

    def get_tweet(self, json_data):
        return json_data['doc']['text']
    
    def get_coordinates(self, json_data):
        return json_data['doc']['coordinates']['coordinates']

    def add_phrase(self, phrase_list):
        self.phrase_list = self.phrase_list + phrase_list

    def token_filter(self, tweet):
        # valid punctuation: !,?.'"
        # tokens = self.tknzr.tokenize(tweet)
        # tokens_LC = [t.lower() for t in tokens]
        tweet_LC = tweet.lower()

        phrase_list_US = [p.replace(' ', '_') for p in self.phrase_list]
        for phrase in self.phrase_list:
             tweet_LC = tweet_LC.replace(phrase, phrase.replace(' ', '_'))
        print(tweet_LC)
        # print(phrase_list_US)
        # for i in range(len(phrase_list_US)):
        #     tweet_LC.replace(self.phrase_list[i], phrase_list_US[i])
        #     print(tweet_LC)
        tokens = tweet_LC.split()
        pattern = '([a-z]+\_?[a-z]*)[\!\,\?\.\'\"]*$'
        # valid_tokens = [t for t in tokens_LC if re.match(pattern, t) != None]
        # valid_tokens = [t for t in tokens if re.match(pattern, t) != None]

        valid_tokens = [] 
        for t in tokens:
            match = re.match(pattern, t)
            if match:
                valid_tokens.append(match.group(1))
        return valid_tokens
    
    def get_sentiment_score(self, json_data, senti_score_trie) -> int:
        tweet = self.get_tweet(json_data)
        valid_tokens = self.token_filter(tweet)
        total_score = 0
        for t in valid_tokens:
            if int(senti_score_trie.find(t)) > 0:
                print(t)
            total_score += int(senti_score_trie.find(t))
        return total_score

    def get_sentiment_score(self, senti_score_trie):
        valid_tokens = self.token_filter(tweet)
        total_score = 0
        for t in valid_tokens:
            if int(senti_score_trie.find(t)) > 0:
                print(t)
            total_score += int(senti_score_trie.find(t))
        return total_score


# if __name__ == '__main__':
    # """ TEST """
    # print('test begin')
    # featGrabber = FeatureGrabber()
    # path = r'files/tinyTwitter.json'
    # with open(path, encoding='utf-8') as f:
        # data = f.readlines()[1]
        # print(data[-1] == '\n')
        # print(data[-2])
        # data = data[:-2]

        # first_line = f.readline()
        # print(first_line)
        # print(first_line[-1] == '\n')
        # print(first_line[-2] == '[')
    # print(data)
    # j = json.loads(data)
    # print(featGrabber.get_coordinates(j))
    # tweet = featGrabber.get_tweet(j)
    # tweet = 'I\'m @hello, hello! hello\' hello\" hello. hello? \
    # @Hello, heLlo! helLo\' HELlo\" heLlo. helLo?'
    # print(tweet)
    # print(featGrabber.token_filter(tweet))
