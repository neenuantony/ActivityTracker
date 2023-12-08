import pymysql

class ActivityTrackerMySQL:
    def __init__(self, host, user, password, database):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()
        self._create_table()

    def _create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS activities (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            duration INT NOT NULL
        )
        """
        self.cursor.execute(create_table_query)
        self.db.commit()

    def track_activity(self, activity_name, duration):
        insert_query = "INSERT INTO activities (name, duration) VALUES (%s, %s)"
        values = (activity_name, duration)
        self.cursor.execute(insert_query, values)
        self.db.commit()

    def get_activities(self):
        select_query = "SELECT * FROM activities"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()


# Example Usage:
tracker_mysql = ActivityTrackerMySQL(host="localhost", user="root", password="", database="activity_tracker")

tracker_mysql.track_activity("Running", 30)
tracker_mysql.track_activity("Reading", 60)
tracker_mysql.track_activity("Walking", 60)
tracker_mysql.track_activity("swimming", 45)

activities = tracker_mysql.get_activities()
print(activities)