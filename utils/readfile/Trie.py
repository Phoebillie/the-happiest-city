# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:44:51 2021

@author: Bilei Zhu, Shuyu Li
"""

import mpi4py
import csv

class TrieNode():
    def __init__(self):
        self.children = {}
        self.senti_score = 0
    def is_end_node(self):
        return not bool(self.children)

class Trie():
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def add(self, key, score):
        crawl = self.root
        for i in range(len(key)):
            char = key[i]
            if char not in crawl.children:
                new_node = self.get_node()
                if i == len(key) - 1:
                    new_node.senti_score = score
                crawl.children[char] = new_node 
                
            crawl = crawl.children[char]
            
    def batch_add(self):
        """to do"""
        pass 
   
    def match(self, key):
        crawl = self.root
        for char in key:
            if char not in crawl.children:
                return None
            crawl = crawl.children[char]
        return crawl

    def find(self, key):
        node = self.match(key)
        return node.senti_score if node else 0
    
    
if __name__ == "__main__":
    dummy = [
        ['apple', 2],
        ['banana', 3],
        ['aids', -4]
        ] 
    T = Trie()
    for e in dummy:
        T.add(e[0], e[1])
    assert(T.find('appl') == 0)
    # with open('AFINN.txt') as f:
    #     reader = csv.reader(f, delimiter="\t")
    #     d = list(reader)
    # print(d[10][0]) # 248
        
    
    
    