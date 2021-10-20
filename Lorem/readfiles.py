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

        
read_file(text_file)