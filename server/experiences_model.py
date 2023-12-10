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
        self.relu = nn.ReLU()

    def forward(self, input, hidden):
        input = self.encoder(input.view(1, -1))
        output, hidden = self.gru(input.view(1, 1, -1), hidden)
        output = self.decoder(output.view(1, -1))
        output = self.relu(output)
        return output, hidden

    def init_hidden(self):
        return Variable(torch.zeros(self.n_layers, 1, self.hidden_size))

# class RNN(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size, n_layers):
#         super(RNN, self).__init__()
#         self.hidden_size = hidden_size
#
#         self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
#         self.i2o = nn.Linear(input_size + hidden_size, output_size)
#         self.o2o = nn.Linear(hidden_size + output_size, output_size)
#         self.dropout = nn.Dropout(0.1)
#         self.softmax = nn.LogSoftmax(dim=1)
#         self.n_layers= n_layers
#
#     def forward(self, input, hidden):
#         input_combined = torch.cat((input, hidden), 1)
#         hidden = self.i2h(input_combined)
#         output = self.i2o(input_combined)
#         output_combined = torch.cat((hidden, output), 1)
#         output = self.o2o(output_combined)
#         output = self.dropout(output)
#         output = self.softmax(output)
#         return output, hidden
#
#     def init_hidden(self):
#         return torch.zeros(1, self.hidden_size)


# preps data for experience bullet points
def prep_data():
    data_file = open("..\\data\\bulletpoints.txt")
    lines = data_file.readlines()
    # have each line, now clean
    data_string = " ".join(lines)
    data_string = data_string.replace("\n", "")
    data_string = data_string.replace(",", " ,")
    data_string = data_string.replace(". ", " . ")
    data_string = data_string.replace("(", " ")
    data_string = data_string.replace(")", " ")
    return data_string


# trains a model for one epoch
def train_once(inp, target, decoder, criterion, decoder_optimizer, chunk_len):
    hidden = decoder.init_hidden()
    decoder.zero_grad()
    loss = 0

    for c in range(chunk_len):
        output, hidden = decoder(inp[c], hidden)
        loss += criterion(output, target[c])

    loss.backward()
    decoder_optimizer.step()

    return loss.data.item() / chunk_len


# trains entire model over all epochs
def train_all(input_data, output_data, voc_len, chunk_len, n_epochs=300,
              hidden_size=100,
              n_layers=1,
              lr=0.015):
    print("TRAINING")
    decoder = RNN(voc_len, hidden_size, voc_len, n_layers)
    decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(1, n_epochs + 1):
        loss = train_once(input_data, output_data, decoder, criterion, decoder_optimizer, chunk_len)
        print("EPOCH " + str(epoch) + " done.")

    return decoder


def make_word_dict(cleaned_string):
    vocab = set(cleaned_string)
    return {word: i for i, word in enumerate(vocab)}


# build entire model
def build_experience_model(data_path, n_epochs):
    cleaned_string = prep_data().split()
    trigrams = [([cleaned_string[i], cleaned_string[i + 1]], cleaned_string[i + 2])
                for i in range(len(cleaned_string) - 2)]
    chunk_len = len(trigrams)
    # make vocab
    vocab = set(cleaned_string)
    voc_len = len(vocab)
    # assign next number 1,,3....n to all n words in vocab so each are unique
    word_to_ix = {word: i for i, word in enumerate(vocab)}

    # make input and output lists
    inp = []
    tar = []
    for context, target in trigrams:
        context_idxs = torch.tensor([word_to_ix[w] for w in context], dtype=torch.long, device="cpu")
        inp.append(context_idxs)
        targ = torch.tensor([word_to_ix[target]], dtype=torch.long)
        tar.append(targ)

    trained_model = train_all(inp, tar, voc_len, chunk_len, n_epochs=n_epochs)

    torch.save(trained_model.state_dict(), data_path)


# Generates a sentence with the given model, word dictionary and priming string
def generate_sentence(decoder, word_to_ix, prime_str='Developed a', predict_len=10, temperature=0.8):
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


# test the model
def test_model(model_path):
    clean_string = prep_data().split()
    vocab = set(clean_string)
    voc_len = len(vocab)
    the_model = RNN(voc_len, 100, voc_len, 1)
    the_model.load_state_dict(torch.load(model_path))
    word_ix = make_word_dict(clean_string)

    print(generate_sentence(the_model, word_ix, "Developed a"))
    print(generate_sentence(the_model, word_ix, "Implemented a"))
    print(generate_sentence(the_model, word_ix, "Worked on"))
    print(generate_sentence(the_model, word_ix, "Assisted in"))
    print(generate_sentence(the_model, word_ix, "Developed a"))
    print(generate_sentence(the_model, word_ix, "Implemented a"))
    print(generate_sentence(the_model, word_ix, "Worked on"))
    print(generate_sentence(the_model, word_ix, "Assisted in"))


# how to run:
# uncomment first line to build the model, can tweak params,
# uncomment second to test model, can switch the sentence generation in test function
if __name__ == '__main__':
    working_path = ".\\pytorch_models\experience_model__RELU2.pth"
    build_experience_model(working_path, 100)
    # test_model(working_path)
