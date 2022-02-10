import csv


def read_file(name_file):
    fill_name_file = str(name_file) + '.csv'
    l = []
    with open(fill_name_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            l = l + [row]
    return l


def search_element(key_word):
    table_data = read_file('recourses/data')
    for i in table_data:
        if i[0] == key_word:
            return i[1]


if __name__ == '__main__':
    test = search_element("test")
    assert search_element("test") == "hello_word!", "incorrect file initial data"
