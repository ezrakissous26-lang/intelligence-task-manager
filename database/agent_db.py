from db_connection import DB_connection

my_conn = DB_connection()
my_conn_etablished = my_conn.get_connection()


class AgentDB:

    valid_ranks = ["Junior", "Senior", "Commander"]

    def create_agents(self, data: dict):

        if data["agent_rank"] not in self.valid_ranks:
            raise ValueError(f"Error ! Accepted values only : {self.valid_ranks}")
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command = """INSERT INTO agents (`name`, speciality, is_active, completed_missions, failed_missions, agent_rank)
        VALUES (%s, %s, %s, %s, %s, %s)"""
        values = list(data.values())

        cur.execute(sql_command, values)
        conn.commit()

        last_id = cur.lastrowid

        cur.close()
        conn.close()

        return self.get_agent_by_id(last_id)

    def get_all_agents(self):
        conn = my_conn_etablished
        cur = conn.cursor(dictionary=True)

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
        if 'agent_rank' in data and data['agent_rank'] not in self.valid_ranks:
            raise ValueError(f"Error ! Accepted values only : {self.valid_ranks}")
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

        sql_command1 = "UPDATE agents SET is_active = FALSE WHERE id = %s"
        cur.execute(sql_command1, (id,))
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def increment_completed(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = """UPDATE agents SET completed_missions = completed_missions + 1 WHERE id = %s"""
        cur.execute(sql_command1, (id,))
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def increment_failed(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = """UPDATE agents SET failed_missions = failed_missions - 1 WHERE id = %s"""
        cur.execute(sql_command1, (id,))
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def get_agent_performance(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor(dictionary=True)

        sql_command1 = "SELECT completed_missions, failed_missions FROM agents WHERE id = %s"
        cur.execute(sql_command1, (id,))
        conn.commit()

        row = cur.fetchone()

        cur.close()
        conn.close()

        if row is None:
            return None
        
        completed = row["completed_missions"]
        failed = row["failed_missions"]
        total = completed + failed

        success_rate = (completed / total * 100) if total > 0 else 0

        return {
            "completed": completed,
            "failed": failed,
            "total": total,
            "success_rate": f"{success_rate} %"
        }

    def count_active_agents(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "SELECT COUNT(*) FROM agents WHERE is_active = TRUE"
        cur.execute(sql_command1)
        conn.commit()

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result

# supprimer ca avnt de push a la fin
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
