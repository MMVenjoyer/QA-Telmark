from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def test_token_mismatch():
    print('\n' + '#' * 10 + ' Тест ошибки 419 ' + '#' * 10)
    BROWSER = webdriver.Chrome()
    BROWSER.get('https://telmark.ru/')
    BROWSER.delete_all_cookies()
    BROWSER.refresh()
    BROWSER.find_element(By.XPATH, '//button[@class="Button_main__EcZ27 Button_blue__TMtwW  AddToCartBtn_add_to_cartBtn__00aNM"]').click()
    time.sleep(3)
    try:
        BROWSER.find_element(By.XPATH, '//div[@class="ActionError_wrapper__6epJU"]')
        res = 0
    except:
        res = 1
    assert res == 1


def test_change_cities():
    print('\n' + '#' * 10 + ' Тест смены городов ' + '#' * 10)
    BROWSER = webdriver.Chrome()
    BROWSER.get('https://telmark.ru/')
    BROWSER.delete_all_cookies()
    BROWSER.refresh()


    #========================================= ТЕСТ Москва =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Москва').click()
    assert BROWSER.current_url == 'https://moskva.telmark.ru/'


    #========================================= ТЕСТ Санкт-Петербург =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Санкт-Петербург').click()
    assert BROWSER.current_url == 'https://spb.telmark.ru/'


    #========================================= ТЕСТ Волгоград =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Волгоград').click()
    assert BROWSER.current_url == 'https://volgograd.telmark.ru/'


    #========================================= ТЕСТ Екатеринбург =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Екатеринбург').click()
    assert BROWSER.current_url == 'https://ekaterinburg.telmark.ru/'


    #========================================= ТЕСТ Казань =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Казань').click()
    assert BROWSER.current_url == 'https://kazan.telmark.ru/'


    #========================================= ТЕСТ Нижний Новгород =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Нижний Новгород').click()
    assert BROWSER.current_url == 'https://nn.telmark.ru/'


    #========================================= ТЕСТ Новосибирск =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Новосибирск').click()
    assert BROWSER.current_url == 'https://novosibirsk.telmark.ru/'


    #========================================= ТЕСТ Омск =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Омск').click()
    assert BROWSER.current_url == 'https://omsk.telmark.ru/'


    #========================================= ТЕСТ Ростов-на-Дону =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Ростов-на-Дону').click()
    assert BROWSER.current_url == 'https://rostov.telmark.ru/'


    #========================================= ТЕСТ Самара =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Самара').click()
    assert BROWSER.current_url == 'https://samara.telmark.ru/'


    #========================================= ТЕСТ Уфа =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Уфа').click()
    assert BROWSER.current_url == 'https://ufa.telmark.ru/'


    #========================================= ТЕСТ Челябинск =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Челябинск').click()
    assert BROWSER.current_url == 'https://chelyabinsk.telmark.ru/'


    #========================================= ТЕСТ Красноярск =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Красноярск').click()
    assert BROWSER.current_url == 'https://krasnoyarsk.telmark.ru/'


    #========================================= ТЕСТ Краснодар =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Краснодар').click()
    assert BROWSER.current_url == 'https://krasnodar.telmark.ru/'


    #========================================= ТЕСТ Воронеж =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Воронеж').click()
    assert BROWSER.current_url == 'https://voronezh.telmark.ru/'


    #========================================= ТЕСТ Пермь =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Пермь').click()
    assert BROWSER.current_url == 'https://perm.telmark.ru/'


    #========================================= ТЕСТ Другой =========================================#

    BROWSER.find_element(By.XPATH, '//button[@class="MobileMenuBtn_openMenu__hGPHk "]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//button[@class="SelectCity_btn__bv_Oy MobileNavigation_mobileHeaderSelectCityBtn__9BgSJ"]').click()
    time.sleep(1)
    BROWSER.find_element(By.LINK_TEXT, 'Другой').click()
    assert BROWSER.current_url == 'https://telmark.ru/'


def test_cataloge_page():
    print('\n' + '#' * 10 + ' Тест открытия страницы каталога ' + '#' * 10)
    BROWSER = webdriver.Chrome()
    BROWSER.get('https://telmark.ru/cable')
    BROWSER.delete_all_cookies()
    BROWSER.refresh()
    title = BROWSER.find_element(By.XPATH, '//h2[@class="Typography_title_lg__IsjLG Typography_bold__W_J_c Typography_color_default__is4_E"]').text
    assert title == 'Кабельно-проводниковая продукция'


def test_mark_detail_page():
    print('\n' + '#' * 10 + ' Тест открытия детальной страницы марки ' + '#' * 10)
    BROWSER = webdriver.Chrome()
    BROWSER.get('https://telmark.ru/cable/atsdiv')
    BROWSER.delete_all_cookies()
    BROWSER.refresh()
    title = BROWSER.find_element(By.XPATH, '//h1[@class="Typography_title_xl____PZp Typography_bold__W_J_c Typography_color_default__is4_E"]').text
    assert title == 'АТСДИВ'


def test_mark_page():
    print('\n' + '#' * 10 + ' Тест открытия страницы марки ' + '#' * 10)
    BROWSER = webdriver.Chrome()
    BROWSER.get('https://telmark.ru/cable/kabeli-telefonnye')
    BROWSER.delete_all_cookies()
    BROWSER.refresh()
    title = BROWSER.find_element(By.XPATH, '//h1[@class="Typography_title_xl____PZp Typography_bold__W_J_c Typography_color_default__is4_E"]').text
    assert title == 'Кабели телефонные'


def test_product_page():
    print('\n' + '#' * 10 + ' Тест открытия страницы продукта ' + '#' * 10)
    BROWSER = webdriver.Chrome()
    BROWSER.get('https://telmark.ru/cable/atsdiv/atsdiv-4')
    BROWSER.delete_all_cookies()
    BROWSER.refresh()
    title = BROWSER.find_element(By.XPATH, '//h1[@class="Typography_title_xl____PZp Typography_bold__W_J_c Typography_color_default__is4_E"]').text
    assert title == 'Кабели АТСДИВ-4'


def test_add_to_basket():
    print('\n' + '#' * 10 + ' Тест добавления в корзину ' + '#' * 10)
    BROWSER = webdriver.Chrome()
    BROWSER.get('https://telmark.ru/cable/atsdiv/atsdiv-4')
    BROWSER.delete_all_cookies()
    BROWSER.refresh()
    BROWSER.find_element(By.XPATH, '//button[@class="Button_main__EcZ27 Button_blue__TMtwW  AddToCartBtn_add_to_cartBtn__00aNM"]').click()
    time.sleep(1)
    BROWSER.find_element(By.XPATH, '//a[@class="Button_main__EcZ27 Button_blue__TMtwW AddSuccess_btn__cU60w"]').click()
    time.sleep(1)
    try:
        BROWSER.find_element(By.XPATH, '//div[@class="ActionError_wrapper__6epJU"]')
        res = 0
    except:
        res = 1
    assert res == 1


def test_articles():
    print('\n' + '#' * 10 + ' Тест открытия страницы стетей ' + '#' * 10)
    BROWSER = webdriver.Chrome()
    BROWSER.get('https://telmark.ru/articles')
    BROWSER.delete_all_cookies()
    BROWSER.refresh()
    title = BROWSER.find_element(By.XPATH, '//h2[@class="Typography_title_lg__IsjLG Typography_bold__W_J_c Typography_color_default__is4_E"]').text
    assert title == 'Статьи'


def test_open_article():
    print('\n' + '#' * 10 + ' Тест открытия страницы конкретной статьи(не проверяет работают ли картинки) ' + '#' * 10)
    BROWSER = webdriver.Chrome()
    BROWSER.get('https://telmark.ru/articles/shagovoe-napryazhenie')
    BROWSER.delete_all_cookies()
    BROWSER.refresh()
    title = BROWSER.find_element(By.XPATH, '//h1[@class="Typography_title_xxl__yN1M2 Typography_bold__W_J_c Typography_color_default__is4_E"]').text
    assert title == 'Что такое шаговое напряжение'