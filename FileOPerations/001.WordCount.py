def count_words(filename):
    try:
        with open(filename,'r') as file:
            content = file.read()
            words = content.split()
            # print(words)
            words_count = len(words)
            print("Number of words in the file :", words_count)
    except FileNotFoundError:
        print("File not found.")

count_words('example.txt')


