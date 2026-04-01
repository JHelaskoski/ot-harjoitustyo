from database_connection import get_database_connection

def drop_tables(connection):
    # Poistetaan tietokantataulut.
    cursor = connection.cursor()

    cursor.execute("drop table if exists game_genres;")
    cursor.execute("drop table if exists games;")
    cursor.execute("drop table if exists console_models;")
    cursor.execute("drop table if exists consoles;")
    cursor.execute("drop table if exists genres;")


    connection.commit()


def create_tables(connection):
    # Luodaan tietokantataulut.
    cursor = connection.cursor()

    #Erotetaan genret omaksi, jotta peleille voidaan määritellä useampi genre.
    cursor.execute("""
        create table genres (
            id integer primary key,
            name text not null unique
        );
    """)


    #Konsolien yläotsikot
    cursor.execute("""
        create table consoles (
            id integer primary key,
            name text not null
        );
    """)

    #Konsolien ala-otsikot
    cursor.execute("""
        create table console_models (
            id integer primary key,
            console_id integer not null,
            name text not null,
            foreign key (console_id) references consoles(id)
        );
    """)

    # Luodaan itse pelitietokanta, laitetaan viittaukset konsoliin ja genreihin.
    # Arvostelut pelaaja lisää, kun peli merkataan pelatuksi.
    cursor.execute("""
        create table games (
            id integer primary key,
            name text not null,
            console_model_id integer,
            release_year integer,
            status text not null,

            story_rating integer,
            graphics_rating integer,
            gameplay_rating integer,
            overall_rating integer,

            foreign key (console_model_id) references console_models(id)

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
