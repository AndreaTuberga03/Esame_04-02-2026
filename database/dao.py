from database.DB_connect import DBConnect
from model.authorship import Authorship

class DAO:

    @staticmethod
    def get_all_authorship():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM authorship"""
        cursor.execute(query)

        for row in cursor:
            result.append(Authorship(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_role():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT role
                    FROM authorship"""
        cursor.execute(query)

        for row in cursor:
            result.append(row["role"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_artist(role):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT a.artist_id, a.name, COUNT(object_id) AS n
                    FROM artist a, authorship au
                WHERE a.artist_id = au.artist_id
                AND role = %s
                GROUP BY a.artist_id, a.name"""
        cursor.execute(query, (role,))

        for row in cursor:
            result.append((row["artist_id"], row["name"], row["n"]))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def get_all_categories():
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM authorship"

        cursor.execute(query)

        for row in cursor:
            results.append(Authorship(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_all_weighted_neigh(year, shape):
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT LEAST(n.state1, n.state2)    AS st1,
                           GREATEST(n.state1, n.state2) AS st2,
                           COUNT(*)                     as N
                    FROM artist a,authorship au, object
                    WHERE year (s.s_datetime) = %s
                      AND s.shape = %s
                      AND (s.state = n.state1 
                       OR s.state = n.state2)
                    GROUP BY st1, st2 """
        cursor.execute(query, (year, shape))
        for row in cursor:
            result.append((row['st1'], row['st2'], row["N"]))
        cursor.close()
        conn.close()
        return result
