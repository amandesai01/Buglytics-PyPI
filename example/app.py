from flask import Flask, request
from buglytics import Buglytics

app = Flask(__name__)

bl_instance = Buglytics(
    server_url="http://localhost:5000",
    connection_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJBQ0NFU1NfUklHSFRTIjoiRVJSX1JFUE9SVCIsIlBST0pfSUQiOiJkMmI4N2VhNC0zNzNmLTRlNzUtYjk1Mi02MjBmNmNiZDYzY2YiLCJPUkdfSUQiOiIwNDBhMGRmMi03YTc1LTRhY2EtYTdjMy0wOTcwZjQ2ZDU2ZWMiLCJleHAiOjE2MTYzMTE2Mjh9.juuc7uVJbhk0PkJav6wrYIfoVRG7hC7gL8E0lGO7mjU"
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

if __name__ == '__main__':
    app.run(port=5155)
    