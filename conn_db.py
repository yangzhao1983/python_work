import cx_Oracle

def exe_sql(db_host, db_service_id, sql_str, cols, db_pswd='db_pswd',db_username = 'db_username',db_port='1521'):
    db_str = db_username + '/' + db_pswd + '@' +db_host+':' + db_port + '/' + db_service_id;
    print('connection string is ' + db_str)
    print('sql string is ' + sql_str)
    con = cx_Oracle.connect(db_str)
    cur = con.cursor()
    cur.execute(sql_str)
    rel = []
    for result in cur:
        row = []
        for col in cols:
            row.append(result[col])
        rel.append(row)
    con.close()
    return rel