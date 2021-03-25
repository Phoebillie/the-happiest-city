import json
from nltk.tokenize import TweetTokenizer

class FeatureGrabber:

    def __init__(self):
        self.tknzr = TweetTokenizer()

    def pre_process(self, data_piece):
        """ 
        to do
        eage case handling

        @rtype: json 
        """
        return json.load(data_piece)

    def get_tweet(self, json_data):
        return json_data['doc']['text']
    
    def get_coordinates(self, json_data):
        return json_data['doc']['coordinates']['coordinates']

    def token_filter(self, tweet):
        pass

if __name__ == '__main__':
    # """ TEST """
    # print('test begin')
    # featGrabber = FeatureGrabber()
    # path = r'files/tinyTwitter.json'
    # with open(path, encoding='utf-8') as f:
    #     data = f.readlines()[1]
    #     data = data[:-2]
    # # print(data)
    # j = json.loads(data)
    # print(featGrabber.get_coordinates(j))
    # print(featGrabber.get_tweet(j))





    


