#import Libraries
from sqlalchemy import create_engine
from sqlalchemy import text
import psycopg2
from datetime import datetime
import pandas as pd
import requests
import BeautifulSoup
import re

def scrape_data():

    website_data = requests.get('https://www.football-data.co.uk/englandm.php')

    # this extracts the historical data of England Champion League

    content = BeautifulSoup(website_data.content, 'html.parser')
    links = content.find_all('a')

    """
    For season 2020/2021, these csv files corresponds to the right side titles:
    - https://www.football-data.co.uk/mmz4281/1920/E0.csv   'Premier League'
    - https://www.football-data.co.uk/mmz4281/0203/E1.csv   'Championship'
    - https://www.football-data.co.uk/mmz4281/1920/E2.csv   'League 1'
    - https://www.football-data.co.uk/mmz4281/1920/E3.csv   'League 2'

    For season 2019/2020, these csv files corresponds to the right side titles:
    - https://www.football-data.co.uk/mmz4281/1920/E4.csv   'Premier League'
    - https://www.football-data.co.uk/mmz4281/0203/E5.csv   'Championship'
    - https://www.football-data.co.uk/mmz4281/1920/E6.csv   'League 1'
    - https://www.football-data.co.uk/mmz4281/1920/E7.csv   'League 2'
    """

    # A list to aggregate the matched/desired csv links
    csv_links = []
    for link in links:
        if re.search(r'mmz\d+\/\d+\/(E0|E1|E2)\.csv', str(link)):
            csv_link = re.search(r'mmz\d+\/\d+\/(E0|E1|E2)\.csv', str(link)).group()
            csv_link = 'https://www.football-data.co.uk/'+ csv_link  # concatenate them
            csv_links.append(csv_link)
        else:
            continue
    return csv_links



#Read data from the csv links and merge into one data file
def extract_data():
    scrapped_links = scrape_data() # Create an object to recieve scrapped data
    data_files = []
    data_columns = ['Div','Date','HomeTeam','AwayTeam','FTHG','FTAG']
    # These are some of the selected column names from the csv files


    for link in scrapped_links:
        csv_data = pd.read_csv(link,usecols = data_columns,sep = ',', engine = 'python')
        data_files.append(csv_data)
    combined_data = pd.concat(data_files, axis=0, ignore_index=True)

    combined_data.to_csv('football_data.csv', header = ['div','date','home_team','away_team','fthg','ftag'], index = False)


def transform_data():
    football_data = pd.read_csv('football_data.csv')

    def convert_date(value):
        if re.search(r'\d+\/\d+\/\d\d\d\d', str(value)) or re.search(r'\d+\/\d+\/\d\d', str(value)):
            new_date = datetime.strptime(str(value), '%d/%m/%Y').date()
            return new_date
        else:
            pass

    # apply the function convert_date()
    football_data['date'] = football_data['date'].apply(convert_date)
    return football_data


def load_data_to_db():

    try:
        engine =
        create_engine('postgresql+psycopg2://{user}:{pw}@localhost/{db}'.\
        format(user = 'username', \
        pw = 'your_password', db = 'your_db_name'))
    except ConnectionError as error:
        print('Unable to connect to the database. Please try again!')
        print(error)

    # Create a table for holding the extracted data
    table = """
    CREATE TABLE IF NOT EXISTS football_data(
    id SERIAL PRIMARY KEY,
    div VARCHAR(5),
    date DATE,
    home_team VARCHAR(50),
    away_team VARCHAR(50),
    fthg INT DEFAULT(0),
    ftag INT DEFAULT(0));
    """

    # similarly, selected column names from the csv files

    with engine.connect() as connection:
        try:
            connection.execute(text(table))
        except psycopg2.Error as error:
            print('Unable to create the table.')
            print(error)

        football_data = transform_data()

        football_data.to_sql('football_data', con = engine, \
        if_exists = 'append', index= False)


        #print(football_data.head(10))

def main():
    extract_data()
    transform_data()
    load_data_to_db()

if __name__ == '__main__':
    main()
