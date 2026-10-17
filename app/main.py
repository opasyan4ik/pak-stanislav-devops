"""Small DevOps laboratory application with a health endpoint."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os


DEFAULTS = {
    "STUDENT_NAME": "Stanislav",
    "STUDENT_SURNAME": "Pak",
    "STUDENT_GROUP": "IT2-2314",
    "STUDENT_ID": "37845",
}
APP_VERSION = "1.0"


def student_details():
    """Return values from the environment with project defaults."""
    return {key: os.getenv(key, default) for key, default in DEFAULTS.items()}


def student_message(details=None):
    """Format the same student data for the console and web page."""
    values = details if details is not None else student_details()
    return (
        "================================\n"
        "DevOps Student Application\n"
        "================================\n\n"
        f"Name: {values['STUDENT_NAME']}\n"
        f"Surname: {values['STUDENT_SURNAME']}\n"
        f"Group: {values['STUDENT_GROUP']}\n"
        f"Student ID: {values['STUDENT_ID']}\n\n"
        "Application is running successfully!\n"
    )


def version_message():
    return f"pak-stanislav-devops {APP_VERSION}\n"


class StudentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b"OK\n"
            status = 200
        elif self.path == "/version":
            body = version_message().encode("utf-8")
            status = 200
        elif self.path == "/":
            body = student_message().encode("utf-8")
            status = 200
        else:
            body = b"Not found\n"
            status = 404

        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    port = int(os.getenv("APP_PORT", "8080"))
    print(student_message(), flush=True)
    print(f"Listening on port {port}", flush=True)
    server = ThreadingHTTPServer(("0.0.0.0", port), StudentHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
