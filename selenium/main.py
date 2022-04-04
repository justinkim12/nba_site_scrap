from google import set_site
from extract import extract
from extract import extract_members as members
from save import save_data
#'ATL':1610612737,'BOS':1610612738,'CHA':1610612766,'CHI':1610612741,'BKN':1610612751,'CLE':1610612739,'DAL':1610612742,'DEN':1610612743,'DET':1610612765,
team_id={
        'GSW':1610612744,
         'HOU':1610612745,'IND':1610612754,'LAC':1610612746,'LAL':1610612747,'MEM':1610612763,
         'MIA':1610612748,'MIL':1610612749,'MIN':1610612750,'NOP':1610612740,'NYK':1610612752
        ,'OKC':1610612760,'ORL':1610612753,'PHI':1610612755,'PHO':1610612756,'POR':1610612757
        ,'SAC':1610612758,'SAS':1610612759,'TOR':1610612761,'UTA':1610612762,'WAS':1610612764}
years=['2020-21']

for i in team_id:   
     for year in years: #년도별로 조사
        html=set_site(team_id[i],year)
        datas=extract(html)#datas 출력
        datas=members(datas,team_id[i])# players 출력
        save_data(datas,i,year)

