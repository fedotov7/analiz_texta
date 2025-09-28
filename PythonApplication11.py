import re
from collections import Counter
import matplotlib.pyplot as plt

def preprocess_text(text):
    
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text

def get_word_frequencies(text):
    words = text.split()
    return Counter(words)

def plot_frequencies(counter, top_n=10):
    most_common = counter.most_common(top_n)
    words, counts = zip(*most_common)
    plt.bar(words, counts)
    plt.xlabel('Слова')
    plt.ylabel('Частота')
    plt.title(f'Топ {top_n} слов в тексте')
    plt.show()

if __name__ == "__main__":
    sample_text = input('Введите текст для анализа:')
    processed_text = preprocess_text(sample_text)
    word_counts = get_word_frequencies(processed_text)
    plot_frequencies(word_counts, top_n=5)
