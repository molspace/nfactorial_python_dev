import json

def app(environ, start_response):
    path = environ.get('PATH_INFO', '')
    method = environ.get('REQUEST_METHOD', '')

    # ping pong
    if path == "/ping" and method == "GET":
        data = b"pong"
        status = "200 OK"
        headers = [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
        start_response(status, headers)
        return iter([data])

    # request info
    elif path == "/info" and method == "GET":
        info = {
            "method": method,
            "url": environ.get('PATH_INFO', ''),
            "protocol": environ.get('SERVER_PROTOCOL', '')
        }
        data = json.dumps(info).encode()
        status = "200 OK"
        headers = [("Content-Type", "application/json"), ("Content-Length", str(len(data)))]
        start_response(status, headers)
        return iter([data])

    # hello world for other requests
    else:
        data = b"Hello, World!\n"
        status = "200 OK"
        headers = [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))]
        start_response(status, headers)
        return iter([data])
