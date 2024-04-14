def word_frequency(filename):
    try:
        with open(filename,'r') as file:
            content= file.read()
            word_list = content.split()
            word_dictionary ={}

            for word in word_list:
                word=word.strip('.,!?;:"')
                word = word.lower()
                if word in word_dictionary:
                    word_dictionary[word] +=1
                else:
                    word_dictionary[word] =1
            
            for word , frequency in word_dictionary.items():
                print(f'{word}:{frequency}')
        
    except FileNotFoundError:
        print("File not found.")

word_frequency('example.txt')