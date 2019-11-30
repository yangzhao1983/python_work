from conn_db import exe_sql

db_host='localhost'
db_service_id = 'db_service_id'
db_port='9999'
db_pswd = 'db_pswd'
db_user = 'db_user'
tenant_name = 'tenant_name'

sql_str = "select XXX"

rel = exe_sql(db_host, db_service_id, sql_str, [1,3], db_pswd,db_user,db_port)

for result in rel:
    print(rel)