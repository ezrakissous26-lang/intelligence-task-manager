import mysql.connector


class DB_connection:
    def get_connection(self):
        conn = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="1234",
            database="Intelligence_db",

        )
        return conn

    def create_database(self):
        conn = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="1234"
        )
        cur = conn.cursor()

        sql_command = "CREATE DATABASE IF NOT EXISTS Intelligence_db;"
        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()

        print("Database created successfully or exists.")

    def create_tables(self):
        conn = self.get_connection()
        cur = conn.cursor()

        sql_command1 = """CREATE TABLE IF NOT EXISTS `agents`(
        `id` int NOT NULL AUTO_INCREMENT,
        `name` varchar(255) DEFAULT NULL,
        `speciality` varchar(255) DEFAULT NULL,
        `is_active` tinyint DEFAULT '1',
        `completed_missions` int DEFAULT '0',
        `failed_missions` int DEFAULT '0',
        `agent_rank` enum(
            'Junior',
            'Senior',
            'Commander'
        ) DEFAULT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci"""

        sql_command2 = """CREATE TABLE IF NOT EXISTS `missions` (
        `id` int NOT NULL AUTO_INCREMENT,
        `title` varchar(255) DEFAULT NULL,
        `description` text,
        `location` varchar(255) DEFAULT NULL,
        `difficulty` int DEFAULT NULL,
        `importance` int DEFAULT NULL,
        `status` varchar(255) DEFAULT 'NEW',
        `risk_level` varchar(255) DEFAULT NULL,
        `assigned_agent_id` int DEFAULT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci"""
        cur.execute(sql_command1)
        cur.execute(sql_command2)
        conn.commit()

        cur.close()
        conn.close()

        print("Tables created successfully or exists.")


db = DB_connection()
db.create_database()
db.create_tables()
