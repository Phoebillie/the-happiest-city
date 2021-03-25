# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils.Trie import Trie
from utils.readfile.read_afinn_txt import GirdReader
from TwitterFeatureGrabber import FeatureGrabber
import csv
import time
import tabulate
# Press the green button in the gutter to run the script.
def test1():
    """ TEST---
    Tokenizer and Trie
    json preprocessing
    """
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
            continue

    def mpi_calc_happiness():
        pass


    def merge_result()；
        pass 

    def print_output(grid_dict):
        """ 
        @params: grid_dict
        {'A1': [] 
        },...
        """
        grids = list(grid_dict.keys)
        num_score = list(dummy.values())

        for i in range(len(grids)):
            num_score[i][0] = format(num_score[i][0], ',')
            num_score[i][1] = '{:+}'.format(num_score[i][1])
            num_score[i].insert(0, grids[i])

        headers = ['Cell', '#Total Tweets', '#Overal Sentiment Score']
        colalign = ('center','center','center')

        print(tabulate(num_score, headers, colalign= colalign , tablefmt = 'fancy_grid'))
        
    def main():
        pass


if __name__ == '__main__':
    pass
    