from db_connection import DB_connection
from agent_db import AgentDB

my_conn = DB_connection()
my_conn_etablished = my_conn.get_connection()


class MissionDB:

    valid_status = ["NEW", "ASSIGNED", "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELLED"]

    def set_risk_level(self, difficulty: int, importance: int):
        risk_level = difficulty * 2 + importance

        if risk_level <= 9:
            return "LOW"
        elif risk_level <= 17:
            return "MEDIUM"
        elif risk_level <= 24:
            return "HIGH"
        else:
            return "CRITICAL"

    def create_mission(self, data: dict):
        diff = data.get("difficulty")
        imp = data.get("importance")
        if not (1 <= diff <= 10) or not (1 <= imp <= 10):
            raise ValueError("Error ! Difficulty and importance need to be betwenn 1 and 10.")

        risk_level = self.set_risk_level(diff, imp)

        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command = """INSERT INTO missions (title, description, location, difficulty, importance, status, risk_level, assigned_agent_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (
            data["title"],
            data.get("description"),
            data.get("location"),
            diff,
            imp,
            "NEW",
            risk_level,
            None
        )

        cur.execute(sql_command, values)
        conn.commit()

        result = cur.lastrowid

        cur.close()
        conn.close()

        return self.get_mission_by_id(result)

    def get_all_missions(self):
        conn = my_conn_etablished
        cur = conn.cursor(dictionary=True)

        sql_command1 = "SELECT * FROM missions"
        cur.execute(sql_command1)

        result = cur.fetchall()

        cur.close()
        conn.close()

        return result

    def get_mission_by_id(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor(dictionary=True)

        sql_command1 = "SELECT * FROM agents WHERE id = %s"
        cur.execute(sql_command1, (id,))
        conn.commit()

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result

    def assign_mission(self, m_id: int, a_id: int):

        my_mission = self.get_mission_by_id(m_id)
        my_agent = AgentDB().get_agent_by_id(a_id)

        if my_mission is None:
            raise ValueError("Mission not found.")  # maybe return false is better ?
        if my_agent is None:
            raise ValueError("Agent not found.")
        if my_agent["is_active"] is False:
            raise ValueError("This agent is not active, sorry.")
        if my_mission["status"] != "NEW":
            raise ValueError("The mission need be in status NEW for assign to agent.")
        if my_mission['risk_level'] == "CRITICAL" and my_agent["agent_ranks"] != "Commander":
            raise ValueError("Only Commander can take mission CRITICAL")

        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "UPDATE missions SET assigned_agent_id = %s, status = 'ASSIGNED' WHERE id = %s"
        cur.execute(sql_command1, (a_id, m_id))
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def update_mission_status(self, id: int, status):  # a revoir je me suis embrouille 
        my_mission = self.get_mission_by_id(id)
        actual_status = my_mission["status"]

        if status not in self.valid_status:
            raise ValueError(f"Error ! Invalid status. Use only this {self.valid_status}")
        if my_mission is None:
            raise ValueError("Mission not found.")

        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "UPDATE missions SET status = %s WHERE id = %s"
        values = status, id

        cur.execute(sql_command1, values)
        conn.commit()

        check = cur.rowcount > 0

        cur.close()
        conn.close()

        return check

    def get_open_missions_by_agent(self, id: int):
        conn = my_conn_etablished
        cur = conn.cursor(dictionary=True)

        sql_command1 = "SELECT COUNT(*) FROM missions WHERE assigned_agent_id = %s AND status IN ('ASSIGNED', 'IN_PROGRESS')"
        cur.execute(sql_command1, (id,))

        result = cur.fetchall()

        cur.close()
        conn.close()

        return result

    def count_all_missions(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "SELECT COUNT(*) FROM missions"
        cur.execute(sql_command1)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0]

    def count_by_status(self, status):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "SELECT COUNT(*) FROM missions WHERE status = %s"
        cur.execute(sql_command1, (status,))

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0]

    def count_open_missions(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "SELECT COUNT(*) FROM missions WHERE status IN ('NEW', 'ASSIGNED', 'IN_PROCESS')"
        cur.execute(sql_command1)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0]

    def count_critical_missions(self):
        conn = my_conn_etablished
        cur = conn.cursor()

        sql_command1 = "SELECT COUNT(*) FROM missions WHERE risk_level = 'CRITICAL"
        cur.execute(sql_command1)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0]

    def get_top_agent(self):
        conn = my_conn_etablished
        cur = conn.cursor(dictionary=True)

        sql_command1 = "SELECT * FROM agents ORDER BY completed_missions DESC LIMIT 1"
        cur.execute(sql_command1)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result
