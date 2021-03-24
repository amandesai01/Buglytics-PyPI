from flask import Flask, request
from buglytics import Buglytics

app = Flask(__name__)

bl_instance = Buglytics(
    server_url="http://localhost:5000",
    connection_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJBQ0NFU1NfUklHSFRTIjoiRVJSX1JFUE9SVHwiLCJQUk9KX0lEIjoiZDJiODdlYTQtMzczZi00ZTc1LWI5NTItNjIwZjZjYmQ2M2NmIiwiT1JHX0lEIjoiMDQwYTBkZjItN2E3NS00YWNhLWE3YzMtMDk3MGY0NmQ1NmVjIn0.v8pN0biMZPCI-tFiR_Lz-sh618uEWtS4bIHvBboGsVM"
)

@app.route('/divide')
def divide():
    try:
        numerator = request.args.get("numerator")
        denominator = request.args.get("denominator")
        result = int(numerator)/int(denominator)
        return "<h3>Result: {}</h3>".format(result)
    except:
        bl_instance.report_error(level=120)
        return "Error"

@app.route('/catch', methods=['POST'])
def catch_error():
    data = request.get_json()
    print("Error Reported!")
    print(data)
    return "OK"

if __name__ == '__main__':
    app.run(port=5155)
    