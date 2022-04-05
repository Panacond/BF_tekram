# from data.read_data import SearchData


def group():
    data = SearchData('../recourses/data_marketplace')
    data_list = data.list_element_by_before_name("id")
    text = '21287'
    if text in data_list:
        return False
    return data_list


if __name__ == '__main__':
    # print(group())
    href = ['asf1dsfgd', 'sfsdf2rety', 'ertert5wdfgd']
    data = "1"
    for i in href:
       if data in i:
        print(i)

