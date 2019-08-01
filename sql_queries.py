# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (
    songplay_id int,
    start_time int,
    user_id int,
    level varchar,
    song_id varchar(18),
    artist_id varchar(18),
    session_id int,
    location varchar,
    user_agent varchar
)
""")

user_table_create = ("""
CREATE TABLE users (
    user_id int,
    first_name varchar,
    last_name varchar,
    gender char(1),
    level varchar,
    PRIMARY KEY (user_id)
)
""")

song_table_create = ("""
CREATE TABLE songs (
    song_id varchar(18),
    title varchar,
    artist_id varchar(18),
    year int,
    duration float,
    PRIMARY KEY (song_id)
)
""")

artist_table_create = ("""
CREATE TABLE artists (
    artist_id varchar(18),
    name varchar NOT NULL,
    location varchar,
    latitude varchar,
    longitude varchar,
    PRIMARY KEY (artist_id)
)
""")

time_table_create = ("""
CREATE TABLE time (
    start_time int NOT NULL,
    hour int NOT NULL,
    day int NOT NULL,
    week int NOT NULL,
    month int NOT NULL,
    year int NOT NULL,
    weekday int NOT NULL
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
    (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users
    (user_id, first_name, last_name, gender, level)
VALUES
    (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs
    (song_id, title, artist_id, year, duration)
VALUES
    (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists
    (artist_id, name, location, latitude, longitude)
VALUES
    (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
VALUES
    (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop
]
