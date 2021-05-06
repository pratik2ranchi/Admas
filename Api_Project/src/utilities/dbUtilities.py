import pymysql
import logging as logger


class DBUtilities(object):
    def __init__(self):
        pass

    def create_connection(self):
        connections = pymysql.connect(
            host='localhost',
            user='root',
            password="root",
            db='local',
            port=10005
        )
        return connections

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            logger.debug(f"Executing: {sql}")
            cur=conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict=cur.fetchall()
            cur.close()
        except Exception as e:
            raise  Exception(f"filed running sql: {sql} \n  Error:{str(e)}")

        finally:
            conn.close()

        return rs_dict
