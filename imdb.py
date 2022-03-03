from selectorlib import Extractor
import requests




URL='https://www.imdb.com/title/'
SEASON_URL='https://www.imdb.com/title/{}/episodes?season={}'





def scrape_main_page(browser,content_id):


    url=URL+content_id+'/?ref_=tt_ov_inf'

    e = Extractor.from_yaml_file('./imdb_main_nnn.yml')

    # Download the page using requests
    r = requests.get(url)
    # Pass the HTML of the page and create 
    data = e.extract(r.text)
    # Print the data 
    print(data)


    
    url="https://www.imdb.com"+data['Episodes']
    r=requests.get(url)


    seasons_e=Extractor.from_yaml_file('./imdb_seasons.yml')
    data=seasons_e.extract(r.text)


    seasons=data['ss'].split()


    print (data)
    print (seasons)


    for season in seasons:
        episodes_url=SEASON_URL.format(content_id,season)

        


    # browser.get(url)
    # time.sleep(2)
    
    # title=browser.find_elements(By.XPATH,'//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1/text()')
    # # title=browser.find_elements(By.XPATH,"//*[contains(text(),'Original title')]/text()")
    # print (title)





# browser=random_browser()
scrape_main_page("browser",'tt0386676')