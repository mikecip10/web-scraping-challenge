# Import dependencies
from splinter import Browser, browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Scrape
def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser
# News
nasa_news={}
def nasa_scrape():
    browser = scrape()
    nasa_url = "https://redplanetscience.com/"
    browser.visit(nasa_url)

# Create HTML object with beautiful soup
    html = browser.html
    soup = bs(html, "html.parser")

    nasa = soup.find('div', class_='list_text')

    news_title = nasa.find('div',class_='content_title').text
    news_info= nasa.find('div',class_='article_body').text

    nasa_content = {'title': news_title, 'info':news_info}
    nasa_news['nasa_content'] = nasa_content
    return nasa_news

# Images
def image_scrape():
    browser = scrape()
    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    featured_image = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url=image_url+featured_image

    image = featured_image_url
    nasa_news['image']=image
    return nasa_news

# Facts
def fact_scrape():
    facts_mars = "https://galaxyfacts-mars.com/"

    facts_table = pd.read_html(facts_mars)

    df = facts_table[0]
    header = df.iloc[0]
    mars_facts_df = df[1:]
    mars_facts_df.columns = header

    nasa_news['fact_scrape'] = fact_scrape
    return nasa_news

# Hemisphere
def hem_scrape():
    browser = scrape()
    hemisphere_url = "https://marshemispheres.com/"
    browser.visit(hemisphere_url)
    image_urls = []

    browser.visit(hemisphere_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    mars_url = soup.find_all('div', class_='item')
    titles=[]
    hemisphere_image_urls=[]

    for x in mars_url:

        title = x.find('h3').text
        url = x.find('a')['href']
        mars_image_url= hemisphere_url+url
    
        browser.visit(mars_image_url)
        html = browser.html
        soup = bs(html, 'html.parser')
        hemisphere_one= soup.find('div',class_='downloads')
        hemisphere_two=hemisphere_one.find('a')['href']

        print(hemisphere_two)
        img_data=dict({'title':title, 'img_url':hemisphere_two})
        hemisphere_image_urls.append(img_data)

    nasa_news['hemisphere_image_urls'] = hemisphere_image_urls
    
    return nasa_news