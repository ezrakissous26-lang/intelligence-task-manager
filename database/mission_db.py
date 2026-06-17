from db_connection import DB_connection

my_conn = DB_connection()
my_conn_etablished = my_conn.get_connection()


class MissionDB:
    def create_mission(self, data: dict):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command = """INSERT INTO missions (title, description, location, difficulty, importance, status, risk_level, assigned_agent_id)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        values = list(data.values())

        cur.execute(sql_command, values)
        conn.commit()

        result = cur.lastrowid

        cur.close()
        conn.close()

        return result

    def get_all_missions(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "SELECT * FROM missions"
        cur.execute(sql_command1)

        result = cur.fetchall()

        cur.close()
        conn.close()

        return result

    def get_mission_by_id(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "SELECT * FROM agents WHERE id = %s"
        cur.execute(sql_command1, (id,))
        conn.commit()

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result

    def assign_mission(self, m_id: int, a_id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def update_mission_status(self, id: int, status, data: dict):  a revoir !!!!
        conn = my_conn_etablished
        cur = conn.cursor()

        set_parts = [f"{key} = %s" for key in data.keys()]
        set_clause = ", ".join(set_parts)

        sql_command1 = f"UPDATE missions SET {set_clause} WHERE id = %s"
        values = list(data.values()) + [id]

        cur.execute(sql_command1, values)
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def get_open_missions_by_agent(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def count_all_missions(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def count_by_status(self, status):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def count_open_missions(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def count_critical_missions(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def get_top_agent(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()
