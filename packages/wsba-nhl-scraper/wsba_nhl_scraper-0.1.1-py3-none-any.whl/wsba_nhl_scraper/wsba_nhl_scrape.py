import requests as rs
import pandas as pd
from datetime import datetime, timedelta
from .data_scrape import combine_pbp_data, combine_shifts

# MAIN FUNCTIONS
def wsba_scrape_game(game_ids):
    pbps = []
    shifts_data = []
    for game_id in game_ids:
        print("Scraping data from game " + str(game_id))

        game_id = str(game_id)
        season = str(game_id[:4])+str(int(game_id[:4])+1)

        api = "https://api-web.nhle.com/v1/gamecenter/"+game_id+"/play-by-play"
        report = "https://www.nhl.com/scores/htmlreports/"+season+"/PL"+str(game_id)[-6:]+".HTM"
        home_log = "https://www.nhl.com/scores/htmlreports/"+season+"/TH"+str(game_id)[-6:]+".HTM"
        away_log = "https://www.nhl.com/scores/htmlreports/"+season+"/TV"+str(game_id)[-6:]+".HTM"

        json = rs.get(api).json()
        html = rs.get(report).content
        home_shift = rs.get(home_log).content
        away_shift = rs.get(away_log).content

        pbp = combine_pbp_data(json,html)
        shifts = combine_shifts(home_shift,away_shift,json,game_id)

        pbps.append(pbp)
        shifts_data.append(shifts)
    
    pbp_df = pd.concat(pbps)
    shifts_df = pd.concat(shifts_data)

    remove = ['period-start','period-end','challenge','stoppage']
    return {"pbp":pbp_df.loc[~pbp_df['event_type'].isin(remove)],
            "shifts":shifts_df
    }
                          

def wsba_scrape_schedule(season,start = "09-01", end = "08-01"):
    api = "https://api-web.nhle.com/v1/schedule/"
    start = str(season[:4])+"-"+start
    end = str(season[:-4])+"-"+end

    form = '%Y-%m-%d'

    start = datetime.strptime(start,form)
    end = datetime.strptime(end,form)

    game = []

    day = (end-start).days+1
    if day < 0:
        day = 365 + day
    for i in range(day):
        inc = start+timedelta(days=i)
        print("Scraping games on " + str(inc)[:10]+"...")
        
        get = rs.get(api+str(inc)[:10]).json()
        gameWeek = list(pd.json_normalize(get['gameWeek'])['games'])[0]

        for i in range(0,len(gameWeek)):
            game.append(pd.DataFrame({
                "id": [gameWeek[i]['id']],
                "season": [gameWeek[i]['season']],
                "season_type":[gameWeek[i]['gameType']],
                "game_center_link":[gameWeek[i]['gameCenterLink']]
                }))
    
    df = pd.concat(game)
    return df.loc[df['season_type']>1]

def wsba_scrape_season(season,start = "09-01", end = "08-01", local=False):
    if local == True:
        load = pd.read_csv("schedule/schedule.csv")
        load = load.loc[load['season'].astype(str)==season]
        game_ids = list(load['id'].astype(str))
    else:
        game_ids = list(wsba_scrape_schedule(season,start,end)['id'].astype(str))

    df = []
    errors = {}
    for game_id in game_ids:
        try: df.append(wsba_scrape_game([game_id]))
        except KeyError as err: 
            print("An error occurred...")
            errors.update({
                "id": game_id,
                "error": err
            })

    
    pbp = pd.concat(df)
    errors = pd.DataFrame(errors)

    return {"pbp":pbp,
            "errors":errors}