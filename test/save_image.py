from base64 import b64decode
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
# pip install screen-recorder-sdk
from screen_recorder_sdk import screen_recorder


def load_image():

    params = screen_recorder.RecorderParams()
    # initialize the screen recoder
    # screen_recorder.init_resources(params)
    # screen_recorder.start_video_recording ('sample.mp4', 30, 8000000, True)
    key = 'яблоко'
    url = f'https://www.google.com/search?q={key}&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X'

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # seconds
    driver.get(url)

    # find first image
    # LINK_DIVS = (By.XPATH, '//img[starts-with(@src, "data:image/jpeg;base64,")]')
    img = driver.find_elements(By.XPATH, '//img[starts-with(@src, "data:image/jpeg;base64,")]')
    img = img[12]

    src = img.get_attribute('src')
    print(src)

    src = src.split('data:image/jpeg;base64,')[1]
    print(src)
    img_data = b64decode(src)
    print(img_data)
    # сохранение картинки
    now_time = str(datetime.now())
    with open(f'../recourses/screenshot/{now_time}img.jpg', 'wb') as f:
        f.write(img_data)
    now_time = str(datetime.now())
    # Делаем скриншот результата
    driver.save_screenshot(f'../recourses/screenshot/{now_time}screenshot.png')
    # screen_recorder.stop_video_recording()
    driver.quit()


def load_image2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(0.5)
    driver.maximize_window()
    key = 'яблоко'
    url = f'https://www.google.com/search?q={key}&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X'
    driver.get(url)
    driver.save_screenshot("../recourses/screenshot/img000" + str(0) + ".png")
    for i in range(1, 5):
        driver.execute_script("window.scrollTo(0," + str(540*i) + ")")
        driver.save_screenshot("../recourses/screenshot/img000" + str(i) + ".png")

    img_list = driver.find_elements(By.XPATH, '//img[starts-with(@src, "data:image/jpeg;base64,")]')
    for i in range(14, 16):
        img = img_list[i]
        with open('../recourses/screenshot/img000' + str(i) + '.jpg', 'wb') as file:
            file.write(img.screenshot_as_png)
    driver.quit()


if __name__ == '__main__':
    load_image2()
    for i in range(1, 2):
        print(i)
