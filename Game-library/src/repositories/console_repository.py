class ConsoleRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_console(self, name):
        # Lisätään uusi konsoliperhe
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into consoles (name) values (?)",
            (name,)
        )
        self._connection.commit()

    def get_all_consoles(self):
        cursor = self._connection.cursor()
        cursor.execute("select id, name from consoles")
        return cursor.fetchall()
