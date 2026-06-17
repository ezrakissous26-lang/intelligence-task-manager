from db_connection import DB_connection

my_conn = DB_connection()
my_conn_etablished = my_conn.get_connection()


class AgentDB:
    def create_agents(self, data: dict):
        pass

    def get_all_agents(self):
        pass

    def get_agent_by_id(self, id: int):
        pass

    def update_agent(self, id: int, data: dict):
        pass

    def deactivate_agent(self, id: int):
        pass

    def increment_completed(self, id: int):
        pass

    def increment_failed(self, id: int):
        pass

    def get_agent_performance(self, id: int):
        pass

    def count_active_agents(self):
        pass
