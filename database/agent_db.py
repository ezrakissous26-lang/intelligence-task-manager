from db_connection import DB_connection

my_conn = DB_connection()
my_conn_etablished = my_conn.get_connection()


class AgentDB:
    def create_agents(self, data: dict):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command = """INSERT INTO agents (`name`, speciality, is_active, completed_missions, failed_missions, agent_rank)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        values = list(data.values())

        cur.execute(sql_command, values)
        conn.commit()

        result = cur.lastrowid

        cur.close()
        conn.close()

        return result

    def get_all_agents(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "SELECT * FROM agents"
        cur.execute(sql_command1)

        result = cur.fetchall()

        cur.close()
        conn.close()

        return result

    def get_agent_by_id(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "SELECT * FROM agents WHERE id = %s"
        cur.execute(sql_command1, (id,))

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result

    def update_agent(self, id: int, data: dict):
        conn = my_conn_etablished
        cur = conn.cursor()

        set_parts = [f"{key} = %s" for key in data.keys()]
        set_clause = ", ".join(set_parts)

        sql_command1 = f"UPDATE agents SET {set_clause} WHERE id = %s"
        values = list(data.values()) + [id]

        cur.execute(sql_command1, values)
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

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


        '''set_parts = [f"{key} = %s" for key in data.keys()]
        set_clause = ", ".join(set_parts)

        sql_command1 = f"UPDATE agents SET {set_clause} WHERE id = %s"
        values = list(data.values()) + [id]

        cur.execute(sql_command1, values)'''


my_data = {
    "name": "Ezra",
    "speciality": "dev",
    "is_active": 1,
    "completed_missions": 5,
    "failed_missions": 2,
    "agent_rank": "junior"
}
a = AgentDB()
a.create_agents(my_data)
