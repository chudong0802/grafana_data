import csv
import pymysql
import pandas as pd
import datetime,time


def deal_csv(path):
    csv_file = open(path,encoding='utf-8')    #打开csv文件
    csv_reader_lines = csv.reader(csv_file)   #逐行读取csv文件
    data = []    #创建列表准备接收csv各行数据
    for one_line in csv_reader_lines:
        data.append(one_line)    #将读取的csv分行数据按行存入列表‘data’中
    print(data)
    return data

    
def to_sql(need_data,timestring):
    # 写入数据库
    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest', port=3306,
                            db='chart_demo')
    cursor = conn.cursor()
    #更新Bug_total_trend
    sql1 = "update chart_demo.`%s` set real_bug='%d' where time='%s'" \
            % (need_data[0][0], int(need_data[0][2]),timestring)
    print(sql1)
    # #更新ABbug_trend
    sql6 = "update chart_demo.`%s` set ABreal='%d' where time='%s'"\
           %(need_data[20][0],int(need_data[20][2]),timestring)
    print(sql6)
    try:
        cursor.execute(sql1)
        cursor.execute(sql6)
    
    except Exception as e:
        conn.rollback()
        print('=====================')
    else:
        print(sql1)
        print(sql6)
        conn.commit()
    cursor.close()
    conn.close()
   

if __name__ == '__main__':
    # deal_csv('tttask.csv')
    today = datetime.date.today()
    #间隔天数
    # oneday = datetime.timedelta(days=0)
    needed_time = str(today) + ' 00:00:00' 
    print(needed_time)
    to_sql(deal_csv('J.csv'),needed_time)




