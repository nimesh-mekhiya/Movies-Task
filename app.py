"""This file must be contain Get all the Movies detail in the API"""

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="movies"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM moviesTable")
myresult = cursor.fetchall()

app = Flask(__name__)
api = Api(app)

# Fetch all the movies detail


class UserManager(Resource):
    @staticmethod
    def get():
        try:
            id = request.args['id']
        except Exception as _:
            id = None

        if not id:
            users = myresult
            return jsonify(users)
        user = myresult.query.get(id)
        return jsonify(user)


api.add_resource(UserManager, '/api/users')

if __name__ == '__main__':
    app.run(debug=True)
