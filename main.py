# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils.Trie import Trie
from TwitterFeatureGrabber import FeatureGrabber
import csv
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    """ TEST---Tokenizer and Trie """
    senti_score_trie = Trie()
    feat_grabber = FeatureGrabber()
    with open(r'.\files\AFINN.txt') as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)
        for word, score in d:
            senti_score_trie.add(word, score)
    # print(senti_score_trie.find('abandon'))

    with open(r'.\files\tinyTwitter.json', encoding='utf-8') as f:
        lines = f.readlines()
    # print(len(lines))
    # print('test begin')
    i = 0
    for line in lines:
        i += 1
        print('_' * 30, i, '_' * 30)
        try:
            json_data = feat_grabber.convert2json(line)
            if json_data:
                print(feat_grabber.get_tweet(json_data))
                print('total score', feat_grabber.get_sentiment_score(json_data, senti_score_trie))
        except TypeError as e:
            # print(line)
            # print(json_data)
            # break
            print(e)
            pass