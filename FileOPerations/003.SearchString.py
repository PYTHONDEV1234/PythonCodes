def search_string(filename, search_string):
    try:
        with open(filename,'r') as file :
            content= file.read()

            frequency = content.lower().count(search_string.lower())

            print(f'Frequency of {search_string} in the file :{frequency}')

    except FileNotFoundError:
        print("File not found")

search_string('example.txt','Python')