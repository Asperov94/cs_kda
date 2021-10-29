import requests
import json
import os

def save_to_json(func):
    """Save to JSON file """
    def wrapper(set_name_file, *args):
        with open(set_name_file, 'w', encoding='utf-8') as f:
            json.dump(func(*args), f, ensure_ascii=False, indent=4)
    return wrapper

@save_to_json
def go_to_fustcup(select):
    r =json.loads(requests.post('https://hasura.fastcup.net/v1/graphql', data = select).text)
    return r

def list_select(id_game):
    """form SELECT GAME HASURA GRAPHQL """
    select_list=[]
    select_list.append('{"operationName":"GetMatchMemberMapStats","variables":{"matchID":' + id_game +'},"query":"query GetMatchMemberMapStats($matchID: Int\u0021) {  match_member_map_stats(where: {match_id: {_eq: $matchID}}) { match_id user_id match_team_id match_map_id kills deaths    assists    headshots    damage_avg    first_kills_tt    first_kills_ct first_deaths_tt    first_deaths_ct    clutch_1v5    clutch_1v4    clutch_1v3    clutch_1v2 clutch_1v1    multikill_5k multikill_4k multikill_3k multikill_2k multikill_1k airshots oneshots noscopes wallbangs __typename }}"}')
    select_list.append('{"operationName":"GetMatch","variables":{"id":' + id_game + ',"gameID":1},"query":"fragment match_member on match_members { match_id hash ready match_team_id rating_diff connected is_leaver kills deaths assists role private { party_id rating user { id nickName: nick_name avatar online isMobile: is_mobile link stats( where: {game_id: {_eq: $gameID}, map_id: {_is_null: true}, game_mode_id: {_is_null: false}} ) { gameModeID: game_mode_id rating __typename } city { id regionID: region_id name_ru name_uk name_en name_de name_pl name_pt name_es name_hbs name_tr __typename } country { id name_ru name_uk name_en name_de name_pl name_pt name_es name_hbs name_tr iso2 __typename } __typename } __typename } __typename}query GetMatch($id: Int\u0021, $gameID: smallint\u0021) { match: matches_by_pk(id: $id) { id status game_status has_winner created_at started_at finished_at scheduled_at readiness_passed last_update server_instance_id teamspeak_server_id tv_address_hidden fake_server_region_id is_paused creator_id dev_build anticheat_enabled type best_of cancellation_reason password chat_id server_region_id game_id game_mode_id max_rounds_count map_banpick_config_id referee_check_requested result_confirmed maps(order_by: {number: asc}) { id number game_status started_at finished_at demo_url demo_deleted map_id __typename } teams(order_by: {id: asc}) { id captain_id name score size chat_id is_winner initial_side team { id name logo tag __typename } mapStats { match_team_id match_map_id score is_winner initial_side __typename } __typename } serverInstance { id ip port tv_port __typename } members { ...match_member __typename } tournament_group_id tournament { id name __typename } tournamentStage { id name groups { id name __typename } outgoings { id number matchLink { match_id __typename } __typename } __typename } tournamentRound { id name __typename } __typename }}"}')
    select_list.append('{"operationName":"GetMatchDuels","variables":{"matchID":' + id_game + '},"query":"query GetMatchDuels($matchID: Int\u0021) { match_duels(where: {match_id: {_eq: $matchID}}) { kills match_id victim_id killer_id match_map_id __typename }}"}')
    select_list.append('{"operationName":"GetMatch","variables":{"id":' + id_game + ',"gameID":1},"query":"fragment match_member on match_members { match_id hash ready match_team_id rating_diff connected is_leaver kills deaths assists role private { party_id rating user { id nickName: nick_name avatar online isMobile: is_mobile link stats( where: {game_id: {_eq: $gameID}, map_id: {_is_null: true}, game_mode_id: {_is_null: false}} ) { gameModeID: game_mode_id rating __typename } city { id regionID: region_id name_ru name_uk name_en name_de name_pl name_pt name_es name_hbs name_tr __typename } country { id name_ru name_uk name_en name_de name_pl name_pt name_es name_hbs name_tr iso2 __typename } __typename } __typename } __typename } query GetMatch($id: Int\u0021, $gameID: smallint\u0021) { match: matches_by_pk(id: $id) { id status game_status has_winner created_at started_at finished_at scheduled_at readiness_passed last_update server_instance_id teamspeak_server_id tv_address_hidden fake_server_region_id is_paused creator_id dev_build anticheat_enabled type best_of cancellation_reason password chat_id server_region_id game_id game_mode_id max_rounds_count map_banpick_config_id referee_check_requested result_confirmed maps(order_by: {number: asc}) { id number game_status started_at finished_at demo_url demo_deleted map_id __typename } teams(order_by: {id: asc}) { id captain_id name score size chat_id is_winner initial_side team { id name logo tag __typename } mapStats { match_team_id match_map_id score is_winner initial_side __typename } __typename } serverInstance { id ip port tv_port __typename } members { ...match_member __typename } tournament_group_id tournament { id name __typename } tournamentStage { id name groups { id name __typename } outgoings { id number matchLink { match_id __typename } __typename } __typename } tournamentRound { id name __typename } __typename } } "}')
    select_list.append('{"operationName":"GetGameDetails","variables":{"gameID":1},"query":"query GetGameDetails($gameID: smallint\u0021) { game_match_modes( where: {game_id: {_eq: $gameID}} order_by: [{team_size: desc}, {disabled: asc}] ) { id name_ru name_uk name_en name_de name_pl name_pt name_es name_hbs name_tr description_ru description_uk description_en description_de description_pl description_pt description_es description_hbs description_tr team_size disabled ranked __typename } maps( where: {game_id: {_eq: $gameID}} order_by: [{matches_count: desc}, {disabled: asc}] ) { id raw_name name type disabled matches_count matchmaking_enabled workshop_id __typename }}"}')
    return select_list
def kda(set_player):
    """Print KDA"""
    i = set_player
    print(f"ID пользователя: {i['private']['user']['id']} Килы:{i['kills']} Смерти: {i['deaths']} Ассисты: {i['assists']} Победитель: {i['win']}")
def winner(players,team_id_1,team_id_2):
    """SET WIN"""
    for player in players:
        if team_id_1['id'] == player['match_team_id']:
            player['win'] = team_id_1['win']          
        elif team_id_2['id'] == player['match_team_id']:
            player['win'] = team_id_2['win']
    return players

#--------------------------------------------------
#variable
id_game =input("ID_GAME: ")
players = []
#--------------------------------------------------

select_list = list_select(id_game)
for select in select_list:
   go_to_fustcup(id_game +'_data' + str(select_list.index(select)) + '.json', select)

with open(id_game + '_data3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    map_id      = data['data']['match']['maps'][0]['map_id']
    team_id_1   = {'id': data['data']['match']['teams'][0]['id'],'win': data['data']['match']['teams'][0]['is_winner']}
    team_id_2   = {'id': data['data']['match']['teams'][1]['id'],'win': data['data']['match']['teams'][1]['is_winner']}
    for i in data['data']['match']['members']:
        players.append(i)

players = (winner(players, team_id_1,team_id_2))
for i in players:
    kda(i)
