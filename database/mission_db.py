from db_connection import DB_connection

my_conn = DB_connection()
my_conn_etablished = my_conn.get_connection()


class MissionDB:
    def create_mission(self, data: dict):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def get_all_missions(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def get_mission_by_id(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()


    def assign_mission(self, m_id: int, a_id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def update_mission_status(self, id: int, status):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

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
