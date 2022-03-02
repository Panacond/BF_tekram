from base64 import b64decode
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
# pip install screen-recorder-sdk
from screen_recorder_sdk import screen_recorder


def load_image():

    # params = screen_recorder.RecorderParams()
    #intialize the screen recoder
    # screen_recorder.init_resources(params)
    # screen_recorder.start_video_recording ('sample.mp4', 30, 8000000, True)
    key = 'яблоко'
    url = f'https://www.google.com/search?q={key}&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X'

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # seconds
    driver.get(url)

    # Поиск первой картинки
    # LINK_DIVS = (By.XPATH, '//img[starts-with(@src, "data:image/jpeg;base64,")]')
    img = driver.find_elements(By.XPATH, '//img[starts-with(@src, "data:image/jpeg;base64,")]')
    # find_element_by_xpath('//img[starts-with(@src, "data:image/jpeg;base64,")]')
    img = img[12]

    src = img.get_attribute('src')
    # print(type(src))

    src = src.split('data:image/jpeg;base64,')[1]
    # print(type(src))
    img_data = b64decode(src)
    # сохранение картинки
    now_time = str(datetime.now())
    with open(f'../recourses/screenshot/{now_time}img.jpg', 'wb') as f:
        f.write(img_data)
    now_time = str(datetime.now())
    # Делаем скриншот результата
    driver.save_screenshot(f'../recourses/screenshot/{now_time}screenshot.png')
    # screen_recorder.stop_video_recording()
    driver.quit()


if __name__ == '__main__':
    load_image()
