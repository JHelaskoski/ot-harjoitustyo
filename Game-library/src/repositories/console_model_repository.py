class ConsoleModelRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_console_model(self, console_id, name):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into console_models (console_id, name) values (?, ?)",
            (console_id, name)
        )
        self._connection.commit()

    def get_console_models_by_console_id(self, console_id):
        # Hakee kaikki konsolimallit tietyn konsolin id:n perusteella.
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from console_models where console_id = ?",
            (console_id,)
        )
        return cursor.fetchall()

    def get_all_console_models(self):
        # Hakee kaikki konsolimallit.
        cursor = self._connection.cursor()
        cursor.execute("select * from console_models")
        rows = cursor.fetchall()
        return rows

    def get_console_model_by_id(self, model_id):
        # Hakee konsolimallin id:n perusteella.
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from console_models where id = ?",
            (model_id,)
        )
        return cursor.fetchone()

    def get_console_model_by_name(self, name):
        # Hakee konsolimallin nimen perusteella.
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from console_models where name = ?",
            (name,)
        )
        return cursor.fetchone()
