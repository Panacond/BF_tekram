def group():
    text = "https://www.facebook.com/groups/735549537228274/"
    BUTTON_FOTO = "//a[@href='/groups/{group_id}/media/photos/']"


    # return re.search(r"\d{15}", text).group(0)
    group_id = "15000"
    return BUTTON_FOTO.format(group_id=group_id)

if __name__ == '__main__':
    print(group())
