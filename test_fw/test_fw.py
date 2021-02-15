class Application:
    def __init__(self, roots: dict, f_controllers: list):
        self.roots = roots
        self.front_controllers = f_controllers

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        # Полезный функционал
        if path[-1] != '/':
            path += '/'

        if path in self.roots:
            view = self.roots[path]
            request = {}
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
