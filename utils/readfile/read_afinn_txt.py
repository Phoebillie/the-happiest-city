import json
import csv
from collections import Counter
# from Trie import Trie

class Afinn:
    # 构造函数
    def __init__(self, path: str, infos: list):

        self.path = path  # 把path存储为属性
        self.infos = infos

        # 定义存储结果的集合
        # self.afinn_list = []  # list
        self.afinn_dict = []  # dict


    def read_afinn(self):
        # 读取文本文件
        # 使用异常处理的结构
        try:
            # 使用Open函数读取文件
            with open(self.path, 'r', encoding='utf-8') as fd:
                # 使用readline方法,读取第一行
                one_line = fd.readline()
                # 判断这一行是否有数据
                while one_line:  # 形成迭代
                    # 处理数据
                    one_line_list = one_line.strip().split('\t')
                    # 1.存储为list(嵌套list)
                    # self.afinn_list.append(one_line_list)

                    # 2.存储为list(嵌套dict)
                    # 定义一个临时的字典集合
                    temp_dict = {}
                    # 遍历list集合
                    for index, value in enumerate(self.infos):
                        # 把key和value拼接成字典
                        temp_dict[value] = one_line_list[index]
                    # 附加到list
                    self.afinn_dict.append(temp_dict)

                    # 读取下一行
                    one_line = fd.readline()

        except Exception as e:
            raise e


class GirdReader:

    def __init__(self):
        self.grid_geo_dict = {}

    def read(self, path: str) -> dict:
        with open(path) as f:
            data = json.load(f)
        try: 
            features = data['features']

            for feat in features:
                props = feat['properties']

                self.grid_geo_dict[props['id']] = [
                    props['xmin'],
                    props['xmax'],
                    props['ymin'],
                    props['ymax']
                ]
            return self.grid_geo_dict
        except json.decoder.JSONDecodeError as error:
            print(error)

class SentiScoreReader:

    def __init__(self, Trie):
        self.phrase_list = []
        self.word_trie = Trie

    def read(self, path:str):
        with open(path) as f:
            reader = csv.reader(f, delimiter="\t")
            word_score = list(reader)
            
            for word, score in word_score:
                if ' ' in word:
                    self.phrase_list.append(word)
                    self.word_trie.add(word.replace(' ', '_'), score)
                else:
                    self.word_trie.add(word, score)
    
    def find_senti_score(self, word):
        return self.word_trie.find(word)


# if __name__ == "__main__":
#     print('test begin')
#     file_path = r'../../files/melbGrid.json'
#     GReader = GirdReader()
#     grid_dict = GReader.read(file_path)
#     print(grid_dict)
    # print('test begin')
    # file_path = r'../../files/AFINN.txt'
    # SentiReader = SentiScoreReader()
    # SentiReader.read(file_path)
    # print(SentiReader.find_senti_score('can\'t_stand'))

        
