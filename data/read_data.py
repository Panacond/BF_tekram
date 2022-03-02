import csv


class SearchData:
    def __init__(self, path_file):
        self.path_file = path_file
        self.data = self.__read_file()

    def __read_file(self):
        fill_name_file = str(self.path_file) + '.csv'
        l = []
        with open(fill_name_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                l = l + [row]
        return l

    def search_element(self, key_word):
        for i in self.data:
            if i[0] == key_word:
                return i[1]


if __name__ == '__main__':
    data = SearchData("../recourses/data")
    assert data.search_element("test") == "hello_word!", "incorrect file initial data"
