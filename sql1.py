import sqlite3
import datetime
import json
con = sqlite3.connect("/headless/gpt/gpt_messages.db", check_same_thread=False)
#con = sqlite3.connect("gpt_messages.db", check_same_thread=False)
cur = con.cursor()

def all_data():
    res = cur.execute(
    '''
    SELECT * FROM message_table
    ''')
    return res.fetchall()
def create_msg(msg0, msg1):
    id=len(all_data())
    today = datetime.datetime.now()
    cur.execute(
    '''
    INSERT INTO message_table (id, msg0, msg1, date)
    VALUES (?,?,?,?)
    ''', [id, msg0, msg1, today])
    con.commit()

def data_from_id(id):
    res = cur.execute(
    '''
    SELECT * FROM message_table WHERE id=?
    ''', [id])
    return res.fetchall()
def last_msg():
    id=len(all_data())
    return data_from_id(id-1)[0]
def total_msgs():
    return len(all_data())
def update_last_msg(msg1):
    id=total_msgs()-1
    cur.execute(
    '''
    UPDATE message_table SET msg1=? WHERE id=?
    ''', [msg1, id]
    )
    con.commit()
def get_messages():
    mydict={
        "id":[],
        "question":[],
        "answer":[],
        "date":[]
    }
    id_list=[]
    question_list=[]
    answer_list=[]
    date_list=[]
    for i in all_data():
        id_list.append(i[0])
        question_list.append(i[1])
        answer_list.append(i[2])
        date_list.append(i[3])
    mydict["id"]=id_list
    mydict["question"]=question_list
    mydict["answer"]=answer_list
    mydict["date"]=date_list
    data=json.dumps(mydict, ensure_ascii=False)
    return data
#cur.execute("DROP TABLE message_table")
#cur.execute("CREATE TABLE message_table (id, msg0, msg1, date)")
#create_msg("hi", "!gpt")
#print(data_from_id(0))
#print(all_data())
#print(get_messages())
#print(total_msgs())
#print(last_msg())
con.commit()