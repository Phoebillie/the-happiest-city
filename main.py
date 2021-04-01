# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils.readfile.Trie import Trie
from utils.readfile.read_afinn_txt import GirdReader, SentiScoreReader
from TwitterFeatureGrabber import FeatureGrabber
from mpi4py import MPI
import csv
import time
import tabulate

# Press the green button in the gutter to run the script.

start_time = time.time()
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

def test2():
    # edge case test for matching
    senti_score_trie = Trie()
    senti_reader = SentiScoreReader(senti_score_trie)
    feat_grabber = FeatureGrabber()
    path = r'.\files\AFINN.txt'
    senti_reader.read(path)
    #print(senti_reader.phrase_list)
    feat_grabber.add_phrase(senti_reader.phrase_list)
    #print(feat_grabber.phrase_list)
    test_tweet = '@pusher: cashing in not WORKING.. does not work.#'
    print(feat_grabber.token_filter(test_tweet))

    def init_counter(grids):
        return {g: [] for g in grids}
    
    def mpi_calc_happiness():
        comm = MPI.COMM_WORLD
        size = comm.Get_size()
        rank = comm.Get_rank()

        grid_reader = GirdReader()
        grids = grid_reader.read(r'.\files\melbGrid.json').keys()

        if rank == 0:
            result = init_counter(grids)
        else:
            result = init_counter(grids)

        print(size, 'core(s) used')

        print(result)


    def merge_result():
        pass 

    def print_output(grid_dict):
        """ 
        @params: grid_dict
        {'A1': [num_tweets, senti_score] 
        },...
        """
        grids = list(grid_dict.keys)
        num_score = list(dummy.values())

        for i in range(len(grids)):
            num_score[i][0] = format(num_score[i][0], ',')
            num_score[i][1] = '{:+}'.format(num_score[i][1])
            num_score[i].insert(0, grids[i])

        headers = ['Cell', '#Total Tweets', '#Overall Sentiment Score']
        colalign = ('center','center','center')

        print(tabulate(num_score, headers, colalign= colalign , tablefmt = 'fancy_grid'))
        print('running time: %.4f seconds' % (time.time() - start_time))


    def test3():
        mpi_calc_happiness()

    def main():
        pass


if __name__ == '__main__':
    test3()
    