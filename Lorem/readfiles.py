text_file = "test.txt"
def read_file(text_file):
    with open(text_file,"r") as handle:
        data = handle.read()
        print (data)


def read_file(text_file):
    """
    Function that reads a text file and returns the data from the text file

    Raises:
        FileNotFoundError:If it cannot the file
    """

    try:
        with open(text_file,"r") as handle:

            data = handle.read()
            return data
    except FileNotFoundError:

        return None

def word_count(text_file):
    handle = open (text_file, "r")
    data = handle.read()
    counter = 0
    for word in data.split():
         if word == "Lorem":
             counter +=1
    print (counter)
word_count(text_file)
read_file(text_file)