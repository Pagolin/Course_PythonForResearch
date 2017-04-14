import string as str
import os # directory for miscellaniouse operating system interfaces
import pandas as pd # named after panel data-> multidimensional data
import matplotlib.pyplot as plt
text = ""

def count_words(text):
    text = text.lower()
    escape = (str.punctuation)
    for ch in escape:
        text= text.replace(ch, " ")

    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

"""
And now the advanced version
"""
from collections import Counter
def count_words_fast(text):
    text = text.lower()
    escape = (",",".",";",":","'",'"')
    for ch in escape:
        text = text.replace(ch, " ")

    word_counts = Counter(text.split(" "))
    return word_counts

def read_book(title_path):
    """
    Read a book and return it as a string replacing \n and \r
    :param title_path: file path 
    :return: string of book contend
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", " ").replace("\r", " ")
    return text

def word_stats(word_counts):
    """Return number of unique words and word frequencies     
    :param word_counts is a dictionary of "word:int" 
    :return: tuple(int, list) number key and list[int] of values
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

book_dir = "../WeekThree/books"

#using os to loop through directories
#using pandas to create a DataFrame

stats = pd.DataFrame(columns = ("Language", "Author", "Title", "Length", "Unique_Words"))
def get_books_from_dir(dir):
    """
    This is the realy cool word statistic function looping throug the book directory, wrinting the word statistics
    into a stats...a pandas DataFrame     
    :param dir: book direction with subs laguage/author/booktitle.txt
    :return: none, just fills the stats DataFrame
    """
    row_count = 1
    for language in os.listdir(dir):
        for author in os.listdir(dir +"/"+ language):
            for title in os.listdir(dir +"/"+ language +"/"+ author ):
                inputfile =dir +"/"+ language +"/"+ author +"/"+ title
                text = read_book(inputfile)
                (num_uni, w_counts) = word_stats(count_words_fast(text))
                stats.loc[row_count] = language, author.capitalize(), title.replace(".txt", ""), sum(w_counts), num_uni
                row_count += 1


"""
text = read_book("../WeekThree/books/English/shakespeare/Romeo and Juliet.txt")
word_counts = count_words(text)
(nr_of_unique_words, frequencies) = word_stats(word_counts)

g_text = read_book("../WeekThree/books/German/shakespeare/Romeo und Julia.txt")
g_word_counts = count_words(g_text)
(nr_of_unique_g_words, g_frequencies) = word_stats(g_word_counts)

print("English: Unique Words ", nr_of_unique_words, "Words ", sum(frequencies))

print("German: Unique Words ", nr_of_unique_g_words, "Words ", sum(g_frequencies))
"""
get_books_from_dir(book_dir)
print(stats.Author)
print(stats[stats.Language == "Portuguese"])
plt.plot(stats.Length, stats.Unique_Words, "bo")

plt.figure(figsize=(10,10))
subset = stats[stats.Language == "English"]
plt.loglog(subset.Length, subset.Unique_Words, "o", label ="English", color= "crimson")
subset = stats[stats.Language == "French"]
plt.loglog(subset.Length, subset.Unique_Words, "o", label ="French", color= "forestgreen")
subset = stats[stats.Language == "German"]
plt.loglog(subset.Length, subset.Unique_Words, "o", label ="German", color= "orange")
subset = stats[stats.Language == "Portuguese"]
plt.loglog(subset.Length, subset.Unique_Words, "o", label ="Portuguese", color= "blue")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")

plt.show()