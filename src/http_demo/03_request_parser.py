def read_paths():
    paths = {
        'GET': [],
        'POST': [],
    }
    while True:
        input_line = input()
        if input_line == 'END':
            break
        path = input_line[:input_line.rindex('/')]
        method = input_line[input_line.rindex('/')+1:]
        paths[method.upper()].append(path)
    return paths


def read_request():
    method, path, *_ = input().split()
    return {
        'method': method,
        'path': path,
    }


def make_request(paths, request):
    valid_paths_for_method = paths[request['method']]

    if request['path'] in valid_paths_for_method:
        return '''
HTTP/1.1 200 OK
Content-Length: 2
Content-Type: text/plain

OK
        '''
    else:
        return '''
HTTP/1.1 404 Not Found
Content-Length: 9
Content-Type: text/plain

Not Found
        '''


def solve():
    paths = read_paths()
    request = read_request()
    result = make_request(paths, request)
    print(result)

solve()