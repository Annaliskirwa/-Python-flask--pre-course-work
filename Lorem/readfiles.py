text_file = "test.txt"
def read_file(text_file):
    with open(text_file,"r") as handle:
        data = handle.read()
        print (data)
read_file(text_file)