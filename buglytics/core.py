import requests
import traceback
import sys

from buglytics.exceptions import ConnectionNotEstablishedException, TokenInvalidException, RequestNotReportedException

class Buglytics:
    def __init__(self, server_url=None, connection_token=None, error_levels=[300, 400, 500], silently_report=False):
        instantiated = False
        token_valid = True
        try:
            r = requests.post(server_url + "/auth/verify",
                    json={"token": connection_token},
                    headers={"Content-Type": "application/json"}
                ).json()
            if r.get("STATUS") == "OK":
                self.server_url = server_url
                self.connection_token = connection_token
                self.error_levels = error_levels
                self.silently_report = silently_report
                instantiated = True
                token_valid = True
            else:
                token_valid = False
        except Exception as e:
            print(e)
        if not instantiated:
            if not token_valid:
                raise TokenInvalidException
            else:
                raise ConnectionNotEstablishedException

    def report_error(self, level):
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        exception_details = ''.join(traceback.format_tb(exception_traceback))
        exception_location = filename + " Line No. " + str(line_number)

        self.__send_error_details__(exception_type, level, exception_location, exception_details)

    def __send_error_details__(self, bug_type, bug_level, bug_location, bug_text):
        r = requests.post(self.server_url+"/errors/create", json={
            "buglevel": bug_level,
            "buglocation": bug_location,
            "bugtext": bug_text,
            "bugtype": str(bug_type)
        }, headers={
            "content-type": "application/json",
            "token": self.connection_token
        }).json()
        if r['STATUS'] != "OK":
            if not self.silently_report:
                raise RequestNotReportedException
