from os import getenv
from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import datetime

import psycopg2
dbname="msbfyodw"
user="msbfyodw"
password="LEYW7uXgDeh2BASjqFR4aqXCvnZImj5h"
host="lallah.db.elephantsql.com"

def db_conect():
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
    return pg_conn
pg_conn = db_conect() #
def  exec_query(pg_conn,query):
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    results=pg_curs.fetchall()
    pg_curs.close()
    return results
# users class model try 


router = APIRouter()


@router.get('/salty/{comment_id}')
async def salty(comment_id: int):
    """
    ### Shows comment table with saltiness score 
    Takes /salty/{comment_id} - starting comment id

    ### Response
    - `id`: integer

    - `created_at`: datetime
    
    - `comment`: string
    
    - `story_title`: string
    
    - `saltiness`:float

    - `user_id`: int
    
    - `user_name`:string

    LIMITS 20 per response

    """
    print(comment_id)
    QUERY = """
               SELECT * FROM comments,users WHERE comments.user_id = users.id 
               AND comments.id > {} ORDER BY created_at DESC LIMIT 20
               """.format(comment_id)
    pg_conn=db_conect()
    results = exec_query(pg_conn,QUERY)
    
    commlist = []

    for result in results:
        comm = {}
        comm['id'] = result[0]
        comm['created_at'] = result[1]
        comm['comment_text'] = result[2]
        comm['story_title'] = result[3]
        comm['saltiness'] = result[4]
        comm['user_id'] = result[5]
        comm['username'] = result[7]
        commlist.append(comm)

    print(commlist)
    #print(QUERY)
    #print(result)
    return commlist