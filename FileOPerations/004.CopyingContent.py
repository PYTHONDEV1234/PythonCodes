def CopyContent(source_file, destination_file):
    try:
        with open(source_file,'r') as src:
            content = src.read()
            with open(destination_file,'w') as dest :
                dest.write(content)
        print("Data copied successfully!!!!!!!!")
        
    except FileNotFoundError:
        print("File not found")

CopyContent('example.txt','dest.txt')