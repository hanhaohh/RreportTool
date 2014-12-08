# -*- coding: utf-8 -*-
import random
#import nltk
def cl(data):
    files='/home/jasonhao/recengine.org/recengine/djdata.csv'
    boa = open(files,"r")
    line = boa.readline()
    total = []
    while(line):
        a = line.strip().split(",")
        total.append(a)
        line = boa.readline()
    #print type(total),len(total)
    random.shuffle(total)
    #this is to get most frequent 10000 words in all the comments in order to give feature to each comment
    word_features = open("/home/jasonhao/recengine.org/recengine/features.csv","r").readlines()
    features=[]
    for i in word_features:
        features.append(i.strip('\n'))
    def document_features(document):
        document_words = document.split(' ')
        #print document_words
        features1 = {}
        for word in features:
            features1['contains(%s)' % word] = (word in document_words)
        #print features1
        return features1
    #turn the comment(i love boa) to the format like ({"contains i":Ture,"contains love":True,......},0)
    featuresets = [(document_features(i[0]),i[1]) for i in total[:200]]
    #print featuresets[4]
    
    train_set, test_set = featuresets[:50], featuresets[50:100]
    # classifier = nltk.NaiveBayesClassifier.train(train_set)
    print classifier.classify(document_features(data))
    return classifier.classify(document_features(data))
	
