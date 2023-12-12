from selenium import webdriver
from selenium.webdriver.common.by import By


def scraping_bdm2(url):
    print (url)
    driver = webdriver.Chrome('')
    driver.get(url)

    article_dict = {}
    articles = driver.find_elements(By.CLASS_NAME, 'pdt-item')

    for article in articles:
        id = article.get_attribute('id')

        title = article.find_element(By.CLASS_NAME, 'title-3').text

        try :
            image = article.find_element(By.TAG_NAME, 'img').get_attribute('src')
        except:
            image = None

        try:
            link = article.find_element(By.TAG_NAME, 'a' ).get_attribute('href')           
        except:
            link = None

        price = article.find_element(By.CLASS_NAME, 'price').text

        #stars = article.find_element(By.XPATH, '//html/body/div[4]/div/div[3]/div/div/div[2]/div[2]/ul[1]/li[14]/div[2]/div[1]/div[2]/a/span').tex

        elements = driver.find_elements(By.CSS_SELECTOR,'[class^="star-"]')

# Parcourez chaque élément et récupérez la partie après "star-"
        for element in elements:
            classe = element.get_attribute("class")
            partie_apres_star = classe.split("star-")[1]
       

        article_dict[id] = {'title': title, 'notation': partie_apres_star,
                            'link': link, 'image': image, 'prix': price}
    return article_dict