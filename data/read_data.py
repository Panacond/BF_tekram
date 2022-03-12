import csv


class SearchData:
    def __init__(self, path_file):
        self.path_file = path_file
        self.data = self.__read_file()

    def __read_file(self):
        fill_name_file = str(self.path_file) + '.csv'
        data_list = []
        with open(fill_name_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                data_list = data_list + [row]
        return data_list

    def search_element(self, key_word):
        data_list = []
        for i in self.data:
            if i[0] == key_word:
                data_list.append(i[1])
        if len(data_list) == 1:
            result = data_list[0]
        else:
            result = data_list
        return result

    def read_all_list(self):
        data_list = []
        for i in self.data:
            data_list.append(i)
        return data_list

    def list_element_by_before_name(self, name):
        data_list = self.read_all_list()
        list_by_name = []
        for i in data_list:
            for index, text in enumerate(i):
                if text == name:
                    list_by_name.append(i[index+1])
        return list_by_name

def write_csv(path, data_list):
    with open(path + "_save.csv", 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in data_list:
            writer.writerow(row)


if __name__ == '__main__':
    path = "../recourses/data"
    data = SearchData(path)
    assert data.search_element("test") == "hello_word!", "incorrect file initial data"
    list_data = [["first", "01"],
                 ["second", "02"]
                 ]
    write_csv(path, list_data)
    data_save = SearchData(path +"_save")
    assert data_save.search_element("first") == "01", "incorrect file save data"

