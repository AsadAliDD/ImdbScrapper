from selectorlib import Extractor
import requests




URL='https://www.imdb.com/title/'
SEASON_URL='https://www.imdb.com/title/{}/episodes?season={}'





def scrape_main_page(content_id):


    url=URL+content_id+'/?ref_=tt_ov_inf'

    main = Extractor.from_yaml_file('./imdb_main.yml')
    seasons_e=Extractor.from_yaml_file('./imdb_seasons.yml')
    episodes_e=Extractor.from_yaml_file('./imdb_episodes.yml')



    # getting MainPage Info for Content 
    r = requests.get(url)
    data_main = main.extract(r.text)
    
    print(data_main)


    



    # Getting Number of Seasons
    url="https://www.imdb.com"+data_main['Episodes']
    r=requests.get(url)    
    data=seasons_e.extract(r.text)
    seasons=data['ss'].split()


    print (data)
    print (seasons)
    

    for season in seasons:
        season_url=SEASON_URL.format(content_id,season)


        r=requests.get(season_url)
        data_episodes=episodes_e.extract(r.text)
        print (data_episodes)

        







scrape_main_page('tt0386676')