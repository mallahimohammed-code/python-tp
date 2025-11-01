import string

def word_count(text):
    words = [w.strip(string.punctuation) for w in text.split() if w.strip(string.punctuation) != ""]
    return len(words)

def word_frequency(text):
    freq = {}
    for word in text.split():
        word = word.strip(string.punctuation).lower()
        if word != "":
            freq[word] = freq.get(word, 0) + 1
    return freq

def average_word_length(text):
    words = [w.strip(string.punctuation) for w in text.split() if w.strip(string.punctuation) != ""]
    lengths = [len(w) for w in words]
    avg = sum(lengths) / len(lengths) if lengths else 0
    freq = word_frequency(text)
    max_occ = max(freq.values())
    most_used = [k for k, v in freq.items() if v == max_occ]
    return most_used, max_occ, round(avg, 2)

def find_palindromes(text):
    words = [w.strip(string.punctuation).lower() for w in text.split()]
    return [w for w in words if len(w) > 1 and w == w[::-1]]

def split_sentences(text):
    parts = text.replace('!', '.').replace('?', '.').split('.')
    return [p.strip() for p in parts if p.strip() != ""]

def sentence_lengths(sentences):
    return [len(s.split()) for s in sentences]

def used_punctuation(text):
    return {c for c in text if c in string.punctuation}

def top_words(freq_dict, n=10):
    return sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:n]

def least_used_words(freq_dict, n=10):
    return sorted(freq_dict.items(), key=lambda x: x[1])[:n]

def unique_vocabulary(freq_dict):
    return set(freq_dict.keys())

def repetitive_patterns(freq_dict, min_occ=3):
    return [word for word, count in freq_dict.items() if count >= min_occ]


with open("texte.txt", "r", encoding="utf-8") as f:
    data = f.read().strip()

num_words = word_count(data)
freq = word_frequency(data)
most_used, max_occ, avg_word_len = average_word_length(data)
palindromes = find_palindromes(data)
sentences = split_sentences(data)
sent_lengths = sentence_lengths(sentences)
avg_sent_len = sum(sent_lengths) / len(sent_lengths) if sent_lengths else 0
top10 = top_words(freq)
least10 = least_used_words(freq)
vocab = unique_vocabulary(freq)
patterns = repetitive_patterns(freq)
punct = used_punctuation(data)
