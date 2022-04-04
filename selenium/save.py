import csv
def save_data(datas,team_name,year):
    row=list(datas[0][0])+list(datas[0][1][0])
    row.pop()
    row+=list(datas[0][1][0]['statistics'].keys())
    file=open(f"stat/{team_name}_{year}.csv",mode='w',newline='',encoding="utf-8")
    writer=csv.writer(file)
    writer.writerow(row)
    for data in datas:
        team_stat=list(data[0].values())
        #print(stat_list)
        #print()
        for players in data[1]:
            stat_list=team_stat+list(players.values())
            stat_list.pop()
            stat_list+=players['statistics'].values()
            writer.writerow(stat_list)
            print("saving..."+players["nameI"])
    return