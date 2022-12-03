from os.path import exists


class FileWriter:
    def __init__(self, file_name):
        self.file_name = "./wyniki/" + file_name

    def check_is_file(self):
        return exists(self.file_name)

    def write(self, output):
        with open(self.file_name, "w") as file:
            print(output, file=file)
