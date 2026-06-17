### First day
#

# Intelligence Task Manager

This project aims to build the complete data layer connected to a MySQL database contained within a Docker container. This database allows the ShadowNet intelligence unit to manage agents and their missions. The Python code, using a MySQL-Python connector, will handle the management of the intelligence-mysql database, including the agent and mission tables.

## Stucture folders and files
### First day
````
intelligence-task-manager/
├── database/
│ ├── db_connection.py
│ ├── agent_db.py
│ └── mission_db.py
├── README.md
├── requirements.txt
└── .gitignore
````

## Tables Structure
Intelligence_db
### Agents :

|`Field` | `Type` | `Comments`|
|----|----| ----|
id | INT, AUTO INCREMENT, PRIMARY KEY | UNIQUE
name | VARCHAR | name of agent
speciality | VARCHAR | domain speciality
is_active | BOOLEAN | default = TRUE
completed_missions | INT | default = 0
failed_missions | INT | default = 0
agent_rank | VARCHAR ENUM | only Junior / Senior / Commander

### Missions :

|`Field` | `Type` | `Comments`|
|----|----| ----|

id | INT, AUTO INCREMENT, PRIMARY KEY | UNIQUE
title | VARCHAR | title of mission
description | TEXT | detailling description
location | VARCHAR | location of the mission
difficulty | INT | between 1 and 10 only
importance | INT | between 1 and 10 only
status | VARCHAR | default = new
level_risk | VARCHAR | automatic not from user 
assigned_agent_id | INT | Null until assignement

## Explication functions and classes

### DB_connection:
This class manage the creaction and the connection with databse.

`connection_get()`

Returns an active connection to MySQL

`create_database()`

Creates db_Intelligence if it does not exist.

`tables_create()`

Creates both tables if they do not exist.

### AgentsDB:

This class manage the table agents.

`create_agent(data)`

Creates a new agent and returns the agent object.

`get_all_agents()`

Returns a list of all agents

`get_agent_by_id(id)`

Returns an agent by id or none.

`update_agent(id, data)`

Update all row , can't change the id

`increment_completed(id)`

Updates the number of tasks completed.

`increment_failed(id)`

Updates the number of tasks failed.

`get_agent_performance(id)`

Return a dict with key completed, failed, total, success_rate -> (%)

`count_active_agents()`

Returns the number of active agents

### MissionDB:

This class manage the table missions.

`mission_create(data)`

Create a new mission and return the object.

`get_all_missions()`

Return all the missions.

`get_mission_by_id(id)`

Return one mission or None.

`assign_mission(m_id, a_id)`

Merge one mission to agent.

`update_mission_status(id, status)`

Change the status of the mission.

`get_open_mission_by_agent(id)`

Return all the mission in progress by agent id.

`count_all_mission()`

Count total mission.

`count_by_status(staus)`

Count missions by specific status.

`count_open_mission()`

Count open missions.

`count_critical_mission()`

Count missions with Critical level.

`get_top_agent()`

Return the agent  with the highest number of mission completed.

## System rules

- Rule: Anywhere that needs to return a list if no data is found returns an empty list.

- rank must be Commander / Senior / Junior — any other value throws an error.

- difficulty and importance must be between 1 and 10 — otherwise an error.

- level_risk is calculated automatically when creating a task — the user does not submit it.

- An agent with False=active_is cannot accept tasks.

- An agent cannot have more than 3 open tasks (PROGRESS_IN / ASSIGNED) at the same time.

- If CRITICAL=level_risk — only an agent with the Commander rank can accept the task.

- Only a task with the status NEW can be assigned. After assignment: ASSIGNED=status.

- Only a task with the status ASSIGNED can be started. After: PROGRESS_IN=status.

- Only a task can be completed. PROGRESS_IN and changed to completed or failed status

- Only a task in NEW or ASSIGNED status can be canceled — otherwise an error

## Running instructions

### Docker 

``docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0``

finish at 11:20 :(