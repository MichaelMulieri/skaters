from mysqlconnection import connectToMySQL

class Skater:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.company = data['company']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def display_all(cls):
        query = "SELECT * FROM Skaters;"
        results = connectToMySQL('skaters').query_db(query)
        skaters = []
        for s in results:
            skaters.append(cls(s))
        return skaters

    @classmethod
    def add_skater(cls, data):
        query = "INSERT INTO Skaters (first_name, last_name, company) VALUES (%(first_name)s, %(last_name)s, %(company)s);"
        results = connectToMySQL('skaters').query_db(query, data)
        return results 