import configparser


def telegram():
    # pyautogui.screenshot(r"Fraud.png")
    config = configparser.ConfigParser()
    config.read('DATA/Keys/config.ini')

    config_viewer = config.items('TOKEN')
    token = config_viewer[0][1]
    up_url=config_viewer[1][1]

    print(token,"ddd",up_url)

telegram()
