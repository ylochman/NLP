#!/bin/bash

# wget -P ./embeddings/ http://lang.org.ua/static/downloads/models/ubercorpus.lowercased.tokenized.word2vec.300d.bz2
# bzip2 -d ./embeddings/ubercorpus.lowercased.tokenized.word2vec.300d.bz2

wget -P ./embeddings/ http://lang.org.ua/static/downloads/models/ubercorpus.cased.tokenized.word2vec.300d.bz2
bzip2 -d ./embeddings/ubercorpus.cased.tokenized.word2vec.300d.bz2

wget -P ./embeddings/ http://lang.org.ua/static/downloads/models/ubercorpus.lowercased.tokenized.glove.300d.bz2
bzip2 -d ./embeddings/ubercorpus.lowercased.tokenized.glove.300d.bz2

wget -P ./embeddings/ http://lang.org.ua/static/downloads/models/ubercorpus.cased.tokenized.glove.300d.bz2
bzip2 -d ./embeddings/ubercorpus.cased.tokenized.glove.300d.bz2
