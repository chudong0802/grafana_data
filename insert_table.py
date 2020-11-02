import csv
import pymysql
import pandas as pd
import datetime,time


def deal_csv(path):
    csv_file = open(path,encoding='utf-8')    #打开csv文件
    csv_reader_lines = csv.reader(csv_file)   #逐行读取csv文件
    data = []    #创建列表准备接收csv各行数据
    # linenum = 0
    for one_line in csv_reader_lines:
        data.append(one_line)    #将读取的csv分行数据按行存入列表‘date’中
        # linenum = linenum + 1    
    print(data)
    return data

    # need_data = []
    # for i in range(linenum):
    #     table_data = data[i][0].split('\t')
    #     for j in range(len(table_data)):
    #         for char in table_data:
    #             if char == '':
    #                 table_data.remove(char)
    #     need_data.append(table_data)
    # # print(need_data)
    # return need_data
def to_sql(need_data,timestring):
    # 写入数据库
    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest', port=3306,
                            db='chart_demo')
    cursor = conn.cursor()
    
    #插入task_issue
    for k in range(1,3): 
        sql2 = "insert into chart_demo.`%s` (team,open,progess,close,time) values('%s','%d','%d','%d','%s')"\
                %(need_data[k][0],need_data[k][1],int(need_data[k][2]),int(need_data[k][3]),int(need_data[k][4]),timestring)
        print(sql2)
        try:
            cursor.execute(sql2)
        except:
            conn.rollback()
            print('*******')
        else:
            print(sql2)
            conn.commit()

    #插入 team_issues
    for m in range(3,15):
        sql3 = "insert into chart_demo.`%s` (team,issues,fix,time) values('%s','%d','%d','%s')"\
                %(need_data[m][0],need_data[m][1],int(need_data[m][2]),int(need_data[m][3]),timestring)
        try:
            cursor.execute(sql3)
        except:
            conn.rollback()
            print('*******')
        else:
            print(sql3)
            conn.commit()

    #插入verify_bug
    sql4 = "insert into chart_demo.`%s` (time,EE,IOV,DEV,TS,DRE) values('%s','%s','%d','%d','%d','%d')"\
            %(need_data[15][0],timestring,int(need_data[15][2]),int(need_data[15][3]),int(need_data[15][4]),int(need_data[15][5]),int(need_data[15][6]))

    #插入overdue_total_bug，overdue_total_task，unmark_total_task，unmark_total_bug
    for n in range(16,20):
        sql5 = "insert into chart_demo.`%s` (time,TS,MX,Cerence,HMI,Voice,MW,yf,iov_tester,DRE,Intergration,`iov infrastructure`)\
               values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d')"%(need_data[n][0],timestring,int(need_data[n][2]),int(need_data[n][3]),\
                int(need_data[n][4]),int(need_data[n][5]),int(need_data[n][6]),int(need_data[n][7]),int(need_data[n][8]),\
                int(need_data[n][9]),int(need_data[n][10]),int(need_data[n][11]),int(need_data[n][12]))
        try:
            cursor.execute(sql5)
        except:
            conn.rollback()
            print('*******')
        else:
            print(sql5)
            conn.commit()
    #插入Bug_trend
    sql7 = "insert into chart_demo.`%s` (time,added,fix) values('%s','%d','%d')"\
           %(need_data[21][0],timestring,int(need_data[21][2]),int(need_data[21][3]))

    #插入work_of_tester_group
    sql8 = "insert into chart_demo.`%s` (time,IOV,EE,DRE,DEV,TS,other) values('%s','%d','%d','%d','%d','%d','%d')"\
           %(need_data[22][0],timestring,int(need_data[22][2]),int(need_data[22][3]),int(need_data[22][4]),int(need_data[22][5]),int(need_data[22][6]),int(need_data[22][7]))

    try:    
        cursor.execute(sql4)
        cursor.execute(sql7)
        cursor.execute(sql8)    
    except Exception as e:
        conn.rollback()
        print('*********')
    else:
        print(sql4)
        print(sql7)
        print(sql8)
        conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    today = datetime.date.today()
    #间隔天数
    # oneday = datetime.timedelta(days=0)
    needed_time = str(today)+ ' 00:00:00' 
    to_sql(deal_csv('J.csv'),needed_time)




