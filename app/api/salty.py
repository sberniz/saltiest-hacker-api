from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import datetime
from os import getenv
import mysql.connector

import psycopg2
HEROKU_POSTGRESQL_WHITE_URL = "postgres://ujtntgfamtnxpe:2faf019e88a07f89ab3b61c82aafc17e3e6d369986184d5f81d2caa8b4411435@ec2-54-235-192-146.compute-1.amazonaws.com:5432/d2fmg0vctqrcnh"

DATABASE_URL = getenv('DATABASE_URL')
def db_conect():
    pg_conn = psycopg2.connect(HEROKU_POSTGRESQL_WHITE_URL)
    return pg_conn
pg_conn = db_conect() 
def  exec_query(pg_conn,query):
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    results=pg_curs.fetchall()
    pg_curs.close()
    return results

router = APIRouter()

@router.get('/top_salty')
async def top_salty():
    """
    ### Returns top 10 saltiest user
    - Takes `/top_salty`

    ### Response

    `id` - userid
    `username` - username
    `saltiness` - saltiness
    `salty_description` = salty description

    """

    QUERY = "SELECT * FROM users ORDER BY saltiness limit 10"
    pg_conn=db_conect()
    results = exec_query(pg_conn,QUERY)
    pg_conn.close()
    print(results)
    userlist = []
    for result in results:
        user = {}
        user['id'] = result[0]
        user['username'] = result[1]
        user['saltiness'] = result[2]
        user['salty_description'] = result[3]
        userlist.append(user)



    return userlist

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
    pg_conn.close()
    
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