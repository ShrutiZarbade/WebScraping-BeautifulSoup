from config.db_connection import con


class Query:

    def __init__(self):
        self.mydb = con

    # query for inserting data into table
    def insert(self, data, table_name):

        column = []
        rows_values = []
        val = []
        for key, values in data:
            column.append(key)
            rows_values.append("%s")
            val.append(values)
        column = ','.join(column)
        val_ = ','.join(['%s'] * len(val))
        query = f''' Insert into %s (%s) values (%s)''' % (table_name, column, val_)
        self.mydb.query_execute(query, value=val)

    # query for inserting multiple rows at a time
    def insert_many(self, data, table_name):
        sql = f"insert into {table_name} (title,link,para) values (%s , %s, %s)"
        val = data
        self.mydb.query_execute_many(query=sql, value=val)

    # query for reading data from database
    def read(self, table_name, column_name, column_val):
        val = (column_val,)
        if column_val is None and column_name is None:
            query = f"SELECT * FROM {table_name}"
            result = self.mydb.run_query(query)
        else:
            query = f"SELECT * FROM {table_name} WHERE {column_name}= %s"
            result = self.mydb.run_query(query, value=val)
        return result

    # query for updating data into the database
    def update(self, data, table_name):
        column = []
        rows_values = []
        val = []
        id = 0
        print(data, '---->data')
        for key, values in data.items():
            if key != 'id':
                column.append(key)
                val.append(values)
            if key == 'id':
                id = values

        val.append(id)
        set_tokens = ','.join([f'{x}=%s' for x in column])
        query = f"UPDATE {table_name} SET {set_tokens} WHERE id = %s"
        self.mydb.query_execute(query, value=val)

    # query for deleting data from the database
    def delete(self, table_name, del_id):

        query = f"DELETE FROM {table_name} WHERE id={del_id}"
        self.mydb.query_execute(query, value=None)
