import connect

def update_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update ='''
    UPDATE clientes
    SET nombre_Cliente = 'Manel'
    WHERE nombre_Cliente = 'Josep Oriol'
    '''
    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update succesfully"}