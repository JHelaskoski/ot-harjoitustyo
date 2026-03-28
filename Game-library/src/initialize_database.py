from database_connection import get_database_connection

def drop_tables(connection):
    # Poistetaan tietokantataulut.
    cursor = connection.cursor()

    cursor.execute("drop table if exists game_genres;")
    cursor.execute("drop table if exists genres;")
    cursor.execute("drop table if exists games;")

    connection.commit()


def create_tables(connection):
    # Luodaan tietokantataulut.
    cursor = connection.cursor()

    cursor.execute("""
        create table games (
            id integer primary key,
            name text not null,
            status text not null
        );
    """)

    cursor.execute("""
        create table genres (
            id integer primary key,
            name text not null unique
        );
    """)

    cursor.execute("""
        create table game_genres (
            game_id integer,
            genre_id integer,
            foreign key (game_id) references games(id),
            foreign key (genre_id) references genres(id)
        );
    """)

    connection.commit()


def initialize_database():
    # Haetaan tietokantayhteys.
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
