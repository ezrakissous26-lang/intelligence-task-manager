from database.db_connection import DB_connection
from database.agent_db import AgentDB


class MissionDB:

    valid_status = ["NEW", "ASSIGNED", "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELLED"]

    def connecting(self):
        return DB_connection().get_connection()

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

        conn = self.connecting()
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
        conn = self.connecting()
        cur = conn.cursor(dictionary=True)

        sql_command1 = "SELECT * FROM missions"
        cur.execute(sql_command1)

        result = cur.fetchall()

        cur.close()
        conn.close()

        return result

    def get_mission_by_id(self, id: int):
        conn = self.connecting()
        cur = conn.cursor(dictionary=True)

        sql_command1 = "SELECT * FROM missions WHERE id = %s"
        cur.execute(sql_command1, (id,))
        conn.commit()

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result

    def assign_mission(self, m_id: int, a_id: int):

        my_mission = self.get_mission_by_id(m_id)
        my_agent = AgentDB().get_agent_by_id(a_id)
        mission_open = self.get_open_missions_by_agent(a_id)

        if my_mission is None:
            raise ValueError("Mission not found.")  # maybe return false is better ?
        if my_agent is None:
            raise ValueError("Agent not found.")
        if my_agent["is_active"] is False:
            raise ValueError("This agent is not active, sorry.")
        if my_mission["status"] != "NEW":
            raise ValueError("The mission need be in status NEW for assign to agent.")
        if my_mission['risk_level'] == "CRITICAL" and my_agent["agent_rank"] != "Commander":
            raise ValueError("Only Commander can take mission CRITICAL")
        if len(mission_open) >= 3:
            raise ValueError("Agent can't have more than 3 missions.")

        conn = self.connecting()
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
        if status == "IN_PROGRESS" and actual_status != "ASSIGNED":
            raise ValueError("The mission need be ASSIGNED before be IN_PROGRESS")
        if status in ["COMPLETED", "FAILED"] and actual_status != "IN_PROGRESS":
            raise ValueError("Before be finish the mission need be IN_PROGRESS")
        if status == "CANCELED" and actual_status not in ["NEW", "ASSIGNED"]:
            raise ValueError("You can cancel mission only if she in status NEW or ASSIGNED")

        conn = self.connecting()
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
        conn = self.connecting()
        cur = conn.cursor(dictionary=True)

        sql_command1 = "SELECT * FROM missions WHERE assigned_agent_id = %s AND status IN ('ASSIGNED', 'IN_PROGRESS')"
        cur.execute(sql_command1, (id,))

        result = cur.fetchall()

        cur.close()
        conn.close()

        return result

    def count_all_missions(self):
        conn = self.connecting()
        cur = conn.cursor()

        sql_command1 = "SELECT COUNT(*) FROM missions"
        cur.execute(sql_command1)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0]

    def count_by_status(self, status):
        conn = self.connecting()
        cur = conn.cursor()

        sql_command1 = "SELECT COUNT(*) FROM missions WHERE status = %s"
        cur.execute(sql_command1, (status,))

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0]

    def count_open_missions(self):
        conn = self.connecting()
        cur = conn.cursor()

        sql_command1 = "SELECT COUNT(*) FROM missions WHERE status IN ('NEW', 'ASSIGNED', 'IN_PROGRESS')"
        cur.execute(sql_command1)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0]

    def count_critical_missions(self):
        conn = self.connecting()
        cur = conn.cursor()

        sql_command1 = "SELECT COUNT(*) FROM missions WHERE risk_level = 'CRITICAL'"
        cur.execute(sql_command1)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0]

    def get_top_agent(self):
        conn = self.connecting()
        cur = conn.cursor(dictionary=True)

        sql_command1 = "SELECT * FROM agents ORDER BY completed_missions DESC LIMIT 1"
        cur.execute(sql_command1)

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result
