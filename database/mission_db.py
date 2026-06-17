from db_connection import DB_connection

my_conn = DB_connection()
my_conn_etablished = my_conn.get_connection()


class MissionDB:
    def create_mission(data):
        pass

    def get_all_missions(self):
        pass

    def get_mission_by_id(self, id: int):
        pass

    def assign_mission(self, m_id: int, a_id: int):
        pass

    def update_mission_status(self, id: int, status):
        pass

    def get_open_missions_by_agent(self, id: int):
        pass

    def count_all_missions(self):
        pass

    def count_by_status(self, status):
        pass

    def count_open_missions(self):
        pass

    def count_critical_missions(self):
        pass

    def get_top_agent(self):
        pass
