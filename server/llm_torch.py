import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import string
import unidecode
import random
import torch
import torch.nn as nn
from torch.autograd import Variable
import time, math
import os


# helper function
def time_since(since):
    s = time.time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)


# GRU model for text generation
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers=1):
        super(RNN, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers

        self.encoder = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size * 2, hidden_size, n_layers, batch_first=True,
                          bidirectional=False)
        self.decoder = nn.Linear(hidden_size, output_size)

    def forward(self, input, hidden):
        input = self.encoder(input.view(1, -1))
        output, hidden = self.gru(input.view(1, 1, -1), hidden)
        output = self.decoder(output.view(1, -1))
        return output, hidden

    def init_hidden(self):
        return Variable(torch.zeros(self.n_layers, 1, self.hidden_size))


# main
if __name__ == '__main__':
    # get data
    train_df = pd.read_csv(os.getcwd() + '/../server/train.csv')
    author = train_df[train_df['author'] == 'EAP']["text"]
    print(author[:5])

    # data cleaning
    text = list(author[:100])

    def joinStrings(text):
        return ' '.join(string for string in text)

    text = joinStrings(text)
    # text = [item for sublist in author[:5].values for item in sublist]
    print(text)

    # remove stop words
    stop = set(nltk.corpus.stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = nltk.stem.wordnet.WordNetLemmatizer()

    def clean(doc):
        stop_free = " ".join([i for i in doc.split() if i not in stop])
        punc_free = "".join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        return normalized


    test_sentence = clean(text).lower().split()
    print(test_sentence)

    # trigrams
    trigrams = [([test_sentence[i], test_sentence[i + 1]], test_sentence[i + 2])
                for i in range(len(test_sentence) - 2)]
    chunk_len = len(trigrams)
    print(trigrams[:3])

    # make vocab
    vocab = set(test_sentence)
    voc_len = len(vocab)
    # assign next number 1,,3....n to all n words in vocab so each are unique
    word_to_ix = {word: i for i, word in enumerate(vocab)}
    print(word_to_ix)

    # make input and target lists
    inp = []
    tar = []
    for context, target in trigrams:
        context_idxs = torch.tensor([word_to_ix[w] for w in context], dtype=torch.long, device="cpu")
        inp.append(context_idxs)
        targ = torch.tensor([word_to_ix[target]], dtype=torch.long)
        tar.append(targ)

    print(inp)
    print(tar)


    def train(inp, target):
        hidden = decoder.init_hidden()
        decoder.zero_grad()
        loss = 0

        for c in range(chunk_len):
            output, hidden = decoder(inp[c], hidden)
            loss += criterion(output, target[c])

        loss.backward()
        decoder_optimizer.step()

        return loss.data.item() / chunk_len

    n_epochs = 300
    print_every = 100
    plot_every = 10
    hidden_size = 100
    n_layers = 1
    lr = 0.015

    decoder = RNN(voc_len, hidden_size, voc_len, n_layers)
    decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    start = time.time()
    all_losses = []
    loss_avg = 0
    for epoch in range(1, n_epochs + 1):
        loss = train(inp, tar)
        loss_avg += loss

        if epoch % print_every == 0:
            print('[%s (%d %d%%) %.4f]' % (time_since(start), epoch, epoch / n_epochs * 50, loss))
        #         print(evaluate('ge', 200), '\n')

        if epoch % plot_every == 0:
            all_losses.append(loss_avg / plot_every)
            loss_avg = 0


    def evaluate(prime_str='this process', predict_len=100, temperature=0.8):
        hidden = decoder.init_hidden()

        for p in range(predict_len):
            prime_input = torch.tensor([word_to_ix[w] for w in prime_str.split()], dtype=torch.long)
            inp = prime_input[-2:]  # last two words as input
            output, hidden = decoder(inp, hidden)

            # Sample from the network as a multinomial distribution
            output_dist = output.data.view(-1).div(temperature).exp()
            top_i = torch.multinomial(output_dist, 1)[0]

            # Add predicted word to string and use as next input
            predicted_word = list(word_to_ix.keys())[list(word_to_ix.values()).index(top_i)]
            prime_str += " " + predicted_word
        #         inp = torch.tensor(word_to_ix[predicted_word], dtype=torch.long)

        return prime_str


    print(evaluate('this process', 40, temperature=1))



