import pandas as pd
import random
import torch
import torch.nn as nn
from torch.autograd import Variable


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
#     def __init__(self, input_size, hidden_size, output_size, n_categories):
#         super(RNN, self).__init__()
#         self.hidden_size = hidden_size
#
#         self.i2h = nn.Linear(n_categories + input_size + hidden_size, hidden_size)
#         self.i2o = nn.Linear(n_categories + input_size + hidden_size, output_size)
#         self.o2o = nn.Linear(hidden_size + output_size, output_size)
#         self.dropout = nn.Dropout(0.1)
#         self.softmax = nn.LogSoftmax(dim=1)
#
#     def forward(self, category, input, hidden):
#         input_combined = torch.cat((category, input, hidden), 1)
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


# gets list of company categories
def get_companies():
    companies = pd.read_csv("..\\data\\allcompanies.csv")
    companies = list(companies["Company"])
    return companies


# prep data for categorical company specific RNN
def prep_cat_data():
    data_file = open("..\\data\\bulletpoints.txt")
    lines = data_file.readlines()

    data_string = " ".join(lines)

    data_string = data_string.replace(",", " ,")
    data_string = data_string.replace(". ", " . ")
    data_string = data_string.replace("(", " ")
    data_string = data_string.replace(")", " ")
    lines = data_string.split("\n")
    data_string = data_string.replace("\n", "")
    vocab = set(data_string.split())
    lines = [line.strip("\n") for line in lines]
    companies = get_companies()
    lines_by_company = {"NO_COMPANY": []}
    for line in lines:
        found_company = False
        for company in companies:
            if company in line:
                if company in lines_by_company:
                    lines_by_company[company].append(line.lstrip().split())
                else:
                    lines_by_company[company] = [line.lstrip().split()]
                found_company = True
                break
        if not found_company:
            lines_by_company["NO_COMPANY"].append(line.lstrip().split())
    # print(lines_by_company)
    ret_companies = []
    for company in companies:
        if company in lines_by_company:
            ret_companies.append(company)
    return lines_by_company, vocab, ret_companies


# Random item from a list
def random_choice(choice_list):
    return choice_list[random.randint(0, len(choice_list) - 1)]

# check companies and make sure each company si represented, remove it if it has zero lines


# Get a random category and random line from that category
def random_training_pair(lines_by_company, companies):
    company_choice = random_choice(companies)
    line = random_choice(lines_by_company[company_choice])
    return company_choice, line


# One-hot vector for category
def category_tensor(company, companies, n_companies):
    li = companies.index(company)
    tensor = torch.zeros(1, n_companies)
    tensor[0][li] = 1
    return tensor


# One-hot matrix of first to last letters (not including EOS) for input
def input_tensor(line, vocab_size, vocab):
    tensor = torch.zeros(len(line), 1, vocab_size)
    for li in range(len(line)):
        word = line[li]
        tensor[li][0][vocab.index(word)] = 1
    return tensor


# ``LongTensor`` of second letter to end (EOS) for target
def target_tensor(line, vocab, vocab_size):
    letter_indexes = [vocab.index(line[li]) for li in range(1, len(line))]
    letter_indexes.append(vocab_size - 1) # EOS
    return torch.LongTensor(letter_indexes)


def random_training_example(lines_by_company, companies, vocab_size, vocab):
    category, line = random_training_pair(lines_by_company, companies)
    cat_tensor = category_tensor(category, companies, len(companies))
    input_line_tensor = input_tensor(line, vocab_size, vocab)
    target_line_tensor = target_tensor(line, vocab, vocab_size)
    return cat_tensor, input_line_tensor, target_line_tensor


def train(category_tensor, input_line_tensor, target_line_tensor, rnn, criterion, learning_rate):
    target_line_tensor.unsqueeze_(-1)
    hidden = rnn.init_hidden()

    rnn.zero_grad()

    loss = torch.Tensor([0]) # you can also just simply use ``loss = 0``

    for i in range(input_line_tensor.size(0)):
        output, hidden = rnn(category_tensor, input_line_tensor[i], hidden)
        l = criterion(output, target_line_tensor[i])
        loss += l

    loss.backward()

    for p in rnn.parameters():
        p.data.add_(p.grad.data, alpha=-learning_rate)

    return output, loss.item() / input_line_tensor.size(0)


# train v 2 model
def train_model_v_2(model_path):
    lines_by_company, vocab, companies = prep_cat_data()
    vocab = list(vocab)
    vocab_size = len(vocab)

    criterion = nn.NLLLoss()

    learning_rate = 0.0005

    rnn_model = RNN(vocab_size, 128, vocab_size, len(companies))

    n_iters = 1000

    for iter in range(1, n_iters + 1):
        print("training number : " + str(iter))
        output, loss = train(*random_training_example(lines_by_company, companies, vocab_size, vocab), rnn_model, criterion, learning_rate)

    torch.save(rnn_model.state_dict(), model_path)


# Sample from a category and starting letter
def generate_sent_v2(category, rnn, max_len, start_letter='Developed'):
    with torch.no_grad():  # no need to track history in sampling
        lines_by_company, vocab, companies = prep_cat_data()
        vocab = list(vocab)
        cat_tensor = category_tensor(category, companies, len(companies))
        input = input_tensor([start_letter], len(vocab), vocab)
        hidden = rnn.init_hidden()

        output_name = start_letter
        print("here")
        current_str = [start_letter]
        for i in range(max_len):
            output, hidden = rnn(cat_tensor, input[0], hidden)
            topv, topi = output.topk(1)
            topi = topi[0][0]
            if topi == len(vocab) - 1 and False:
                print("break")
                break
            else:
                word = vocab[topi]
                current_str.append(word)
            input = input_tensor([word], len(vocab), vocab)

        return " ".join(current_str)


def test_model_v2(model_path):
    lines_by_company, vocab, companies = prep_cat_data()
    vocab_size = len(vocab)
    the_model = RNN(vocab_size, 128, vocab_size, len(companies))
    the_model.load_state_dict(torch.load(model_path))
    print(generate_sent_v2("Amazon", the_model, 15))

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
def test_model(model_path, print_len):
    clean_string = prep_data().split()
    vocab = set(clean_string)
    voc_len = len(vocab)
    the_model = RNN(voc_len, 100, voc_len, 1)
    the_model.load_state_dict(torch.load(model_path))
    word_ix = make_word_dict(clean_string)

    print(generate_sentence(the_model, word_ix, "Developed a", print_len))
    print(generate_sentence(the_model, word_ix, "Implemented a", print_len))
    print(generate_sentence(the_model, word_ix, "Worked on", print_len))
    print(generate_sentence(the_model, word_ix, "Assisted in", print_len))
    print(generate_sentence(the_model, word_ix, "Developed a", print_len))
    print(generate_sentence(the_model, word_ix, "Implemented a", print_len))
    print(generate_sentence(the_model, word_ix, "Worked on", print_len))
    print(generate_sentence(the_model, word_ix, "Assisted in", print_len))


# makes a bullet point for the resume. THIS IS THE ONLY FUNCTION TO CALL FOR VERSION 1 MODELS
def make_version1_bullet_point(model_path, print_len, primer_str):
    clean_string = prep_data().split()
    vocab = set(clean_string)
    voc_len = len(vocab)
    the_model = RNN(voc_len, 100, voc_len, 1)
    the_model.load_state_dict(torch.load(model_path))
    word_ix = make_word_dict(clean_string)
    sentence = generate_sentence(the_model, word_ix, primer_str, print_len)
    return sentence


# how to run:
# uncomment first line to build the model, can tweak params,
# uncomment second to test model, can switch the sentence generation in test function
if __name__ == '__main__':
    working_path = ".\\pytorch_models\experience_model_1.1_100.pth"
    # build_experience_model(working_path, 100)
    # test_model(working_path, 10)
    # train_model_v_2(working_path)
    # test_model_v2(working_path)
