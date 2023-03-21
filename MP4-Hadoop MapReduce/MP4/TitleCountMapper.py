#!/usr/bin/env python3
# export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64
# zip MP4 TitleCountMapper.py TitleCountReducer.py TopTitlesMapper.py TopTitlesReducer.py TopTitleStatisticsMapper.py TopTitleStatisticsReducer.py OrphanPagesMapper.py OrphanPagesReducer.py LinkCountMapper.py LinkCountReducer.py TopPopularLinksMapper.py TopPopularLinksReducer.py PopularityLeagueMapper.py PopularityLeagueReducer.py
# docker cp 88d236cde3b5a86e71bdcc88e4ef260db24b1529756cc9c9bfd8f2866c1e4fd2:/MP4_HadoopMapReduce_Template/PythonTemplate/MP4.zip /Users/bodasong/desktop/cs498/mp4

import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
stopwords = []
delimiters = []

# TODO
with open(stopWordsPath) as f:
    # TODO
    for line in f:
        stopwords.append(line.rstrip('\n'))
    #print(stopwords)


#TODO 
with open(delimitersPath) as f:
    # TODO
    delim = f.read()
    delim = delim.rstrip('\n')
    delimiters = [d for d in delim]
    #print(delimiters)


for line in sys.stdin:
    # TODO
    for delim in delimiters:
        line = line.replace(delim, ' ')
    line = line.lower()
    words = line.split()
    for w in words:
        if w not in stopwords:
            output = w + '\t' + '1'
            print(output)
    # print('%s\t%s' % (  ,  )) pass this output to reducer


