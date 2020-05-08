'''
Chatbot main.py
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import torch
from torch.jit import script, trace
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
import csv
import random
import re
import os
import unicodedata
import codecs
from io import open
import itertools
import math





def printLines(file, n=10):
    with open(file, 'rb') as datafile:
        lines = datafile.readlines()
    for line in lines[:n]:
        print(line)



def run():
	corpus_name = "cornell movie-dialogs corpus"
	corpus = os.path.join("dataset", corpus_name)
	printLines(os.path.join(corpus, "movie_lines.txt"))





if __name__ == '__main__':
	run()