import cx_Oracle

tenant_name = "tenant_name"
db_host='localhost'
db_service_id = 'db_service_id'
db_port='9999'
db_pswd = 'db_pswd'
db_username = 'db_username'

for i in range(27,28):
    print(10 * '=')

    # get username/password for tenant schema open connection
    db_str = 'db_username' + '/' + db_pswd + '@' +db_host+':' + db_port + '/' + db_service_id;
    print(db_str)
    con = cx_Oracle.connect(db_str)
    print(con.version)


    # get tenant user name and password
    cur = con.cursor()


    sql_str = "select XXX"

    print(sql_str)
    cur.execute(sql_str)
    username = ''
    password = ''
    for result in cur:
        print(result)
        print(result[1])
        print(result[3])
        username = result[1]
        password = result[3]
    con.close

    # get count for tenant schema
    connStr = username + "/" + password + "@" + db_host + ":" + db_port + "/" + 'tenant_id';
    print(connStr)
    conn = cx_Oracle.connect(connStr)
    print(conn.version)

    cur = conn.cursor()
    # cur.execute("select TENANT_ID from EMAIL_TEMPLATE")
    # for result in cur:
    #     print(result)

    cur.execute("select count(*) from EMAIL_TEMPLATE")
    for result in cur:
        print(result[0])

    cur.execute('select count(*) from EMAIL_TEMPLATE_S')
    for result in cur:
        print(result)

    conn.close()