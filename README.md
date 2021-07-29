# Capstone_Data_Collection

football-data.co.uk
football-data.co.uk is a betting and odds website that has made a lot of historical league data available as csv files. The data includes results and a lot of betting/odds related data. I have tried to aggregate and clean up the data in the following repo github.com/jokecamp/FootballData.

Some of the key observations from jokecamp github repo:

Leagues and divisions included:

England Football Results    Premiership & Divs 1,2,3 & Conference
Scotland Football Results   Premiership & Divs 1,2 & 3
Germany Football Results    Bundesligas 1 & 2
Italy Football Results      Serie A & B
Spain Football Results      La Liga (Premera & Segunda)
France Football Results     Le Championnat & Division 2
Netherlands Football Results    KPN Eredivisie
Belgium Football Results    Jupiler League
Portugal Football Results   Liga I
Turkey Football Results     Ligi 1
Greece Football Results     Ethniki Katigoria
The key/legend of all the field abbreviations gives you idea of what is available in the CSV files:

Div = League Division
Date = Match Date (dd/mm/yy)
HomeTeam = Home Team
AwayTeam = Away Team
FTHG = Full Time Home Team Goals
FTAG = Full Time Away Team Goals
FTR = Full Time Result (H=Home Win, D=Draw, A=Away Win)
HTHG = Half Time Home Team Goals
HTAG = Half Time Away Team Goals
HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)

In essence, https://www.football-data.co.uk/englandm.php is the website that I implemented my python scrape script. 
It does not include all the datasets I will be using, as the process is constantly updating. But it gives a snapshot of 
the data collection process.
