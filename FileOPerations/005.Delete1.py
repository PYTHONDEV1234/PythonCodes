def delete(filename):
    try:
        with open(filename,'w'):
            pass

        print("File content deleted successfully")
    
    except FileNotFoundError:
        print("File not found")

delete('dest.txt')