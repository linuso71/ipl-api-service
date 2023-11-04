import numpy as np
import pandas as pd
ipl_matches = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTfVds6XnEDV0MAGZZ8JGuANQ9Sw4ukHESKLk2eUU6xkg5W1B-B5M2tEwfwHKeWaVfevV456CtR1Ym7/pub?gid=1836071008&single=true&output=csv'
matches = pd.read_csv(ipl_matches)
def teams():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))

    team_dict={
        'teams':teams
    }
    return team_dict

def teamVteam(team1,team2):
    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    if team1 and team2 in valid_teams:
        temp_df = matches[(matches['Team1'] ==team1) & (matches['Team2'] == team2 ) | (matches['Team1'] ==team2) & (matches['Team2'] == team1 )]
        total_matches = temp_df.shape[0]

        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]

        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
            'Total_matches':str(total_matches),
            team1: str(matches_won_team1),
            team2: str(matches_won_team2),
            'draw':str(draws)
            }

        return response
    else:
        return {'message':'invalid team name'}