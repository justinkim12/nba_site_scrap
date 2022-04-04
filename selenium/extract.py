from bs4 import BeautifulSoup
import requests
import json
def extract(html):
    soup=BeautifulSoup(html,'html.parser')
    links=soup.find('tbody').find_all('tr')
    datas=[]
    for link in links:
        link.find_all('td')
        search=[]
        href=link.find_all('a')
        search.append(href[-1].get('href'))
        for data in link:
            if (data.string!=None):
                if(data.string!='\n'and data.string!=' '):
                    search.append(data.string)
        datas.append(search)
    for i in datas:
        i=i[0:6]

    return datas

def extract_members(lists,id):#id는 구하고자 하는 팀의 id
    players_all=[]#전경기 데이터
    for href in lists:
        player=[]
        dic={}
        #날짜 형식 바꾸기 sql연산을 위해 바꿈
        href[1]=dates(href[1])
        dic['date']=href[1] #날짜
        if('vs.'in href[2]): 
            dic['matchup']=href[2].replace('vs.','@') #상대 팀 매치업 @로 통일
        else:
            dic['matchup']=href[2] 
        dic['w/l']=href[3] #승패여부
        dic['pts']=href[5] #총 득점
        player.append(dic)
        url=f"https://www.nba.com{href[0]}"
        #url=f"https://www.nba.com{href[0]}"
        #url='https://www.nba.com/game/0022100883/box-score'
        html=requests.get(url)
        #print(html)
        print("extracting..."+url)
        soup=BeautifulSoup(html.text,'html.parser')
        if soup.find('script',{"id":"__NEXT_DATA__"})!=None:
            soup=soup.find('script',{"id":"__NEXT_DATA__"}).string
            datas=json.loads(soup)
        else:
            continue
        teamid=datas['props']['pageProps']['game']['homeTeam']['teamId']
        hometeam=datas['props']['pageProps']['game']['homeTeam']
        awayteam=datas['props']['pageProps']['game']['awayTeam']

        if(id==teamid):#홈팀의id가 GSW의 teamid와 일치할때==GSW가 홈팀일때
            #print(hometeam['players'])
            player.append(hometeam['players'])
            players_all.append(player)
        else:#GSW가 원정팀일때
            #print(awayteam['players'])
            player.append(awayteam['players'])
            players_all.append(player)    
        
        
        #1번 실행
        
    
    return players_all

          
def dates(date):
    list=date.split('/')
    date=f'{list[2]}-{list[0]}-{list[1]}'
    return date