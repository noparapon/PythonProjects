class Application:
    def __init__(self, roots: dict, f_controllers: list):
        self.roots = roots
        self.front_controllers = f_controllers

    def parse_input_data(self, data: str):
        res = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                res[k] = v
        return res

    def parse_wsgi_input_data(self, data: bytes):
        res = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            res = self.parse_input_data(data_str)
        return res

    def get_wsgi_input_data(self, env) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        # Полезный функционал
        if path[-1] != '/':
            path += '/'

        method = environ['REQUEST_METHOD']
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)

        query_str = environ['QUERY_STRING']
        request_params = self.parse_input_data(query_str)

        if path in self.roots:
            view = self.roots[path]
            request = {}
            request['method'] = method
            request['data'] = data
            request['params'] = request_params

            for controller in self.front_controllers:
                controller(request)
                # вызываем view, получаем результат
            code, text = view(request)
            # возвращаем заголовки
            start_response(code, [('Content-Type', 'text/html')])
            # возвращаем тело ответа
            return [text.encode('utf-8')]
        else:
            # Если url нет в roots - то страница не найдена
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]
