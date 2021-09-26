# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = "CREATE TABLE IF NOT EXISTS songplay (songplay_id int, start_time timestamp, user_id int, level varchar,  song_id int, artist_id int, session_id int, location varchar, user_agent varchar);"

user_table_create = "CREATE TABLE IF NOT EXISTS user_table (user_id int, fist_name varchar, last_name varchar, gender varchar, level varchar);"

song_table_create = "CREATE TABLE IF NOT EXISTS song (song_id int, title varchar, artist_id int, year date, duration timestamp);"

artist_table_create = "CREATE TABLE IF NOT EXISTS artist (artist_id int, name varchar, location varchar, latitude numeric, longitude numeric);"

time_table_create = "CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour timestamp, day date, week date, month date, year date, weekday varchar);"


# INSERT RECORDS

songplay_table_insert = """
"""

user_table_insert = """
"""

song_table_insert = """
"""

artist_table_insert = """
"""


time_table_insert = """
"""

# FIND SONGS

song_select = """
"""

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
