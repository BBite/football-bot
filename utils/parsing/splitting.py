def split_table(teams: list) -> tuple:
    logos = [team['logo'] for team in teams]
    nums = list()
    names = list()
    plays = list()
    wins = list()
    draws = list()
    losses = list()
    goals = list()
    points = list()
    for team in teams:
        nums.append(team['pos'] if int(team['pos']) > 9 else '  ' + team['pos'])
        names.append(team['name'])
        plays.append(team['played'] if int(team['played']) > 9 else ' ' + team['played'])
        wins.append(team['won'] if int(team['won']) > 9 else ' ' + team['won'])
        draws.append(team['draw'] if int(team['draw']) > 9 else ' ' + team['draw'])
        losses.append(team['lost'] if int(team['lost']) > 9 else ' ' + team['lost'])
        goals.append((team['for'] if int(team['for']) > 9 else '  ' + team['for']) + ':' + team['against'])
        points.append(team['points'] if int(team['points']) > 9 else ' ' + team['points'])
    return logos, nums, names, plays, wins, draws, losses, goals, points


def split_scorers(scorers: list) -> tuple:
    nums = list()
    names = list()
    teams = list()
    goals = list()
    plays = list()
    for scorer in scorers:
        nums.append(scorer['pos'] if int(scorer['pos']) > 9 else '  ' + scorer['pos'])
        names.append(scorer['name'])
        teams.append(scorer['team'])
        goals.append(scorer['goals'] if int(scorer['goals']) > 9 else ' ' + scorer['goals'])
        plays.append(scorer['played'] if int(scorer['played']) > 9 else ' ' + scorer['played'])
    return nums, names, teams, goals, plays


def split_assists(players: list) -> tuple:
    nums = list()
    names = list()
    teams = list()
    assists = list()
    plays = list()
    for player in players:
        nums.append(player['pos'] if int(player['pos']) > 9 else '  ' + player['pos'])
        names.append(player['name'].split('(')[0].rstrip())
        teams.append(player['team'])
        assists.append(player['assists'] if int(player['assists']) > 9 else ' ' + player['assists'])
        plays.append(player['played'] if int(player['played']) > 9 else ' ' + player['played'])
    return nums, names, teams, assists, plays
