from db_connection import DB_connection

my_conn = DB_connection()
my_conn_etablished = my_conn.get_connection()


class AgentDB:
    def create_agents(self, data: dict):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def get_all_agents(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def get_agent_by_id(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def update_agent(self, id: int, data: dict):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def deactivate_agent(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def increment_completed(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def increment_failed(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def get_agent_performance(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()

    def count_active_agents(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = ""
        cur.execute(sql_command1)
        conn.commit()

        cur.close()
        conn.close()
