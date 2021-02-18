import quopri

from test_fw import render


def index_view(request):
    secret = request.get('secret_key', None)
    date = request.get('date', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', secret=secret, date=date)


def about_view(request):
    secret = request.get('secret_key', None)
    date = request.get('date', None)
    # Используем шаблонизатор
    return '200 OK', render('about.html', secret=secret, date=date)


def contact_post(request):
    secret = request.get('secret_key', None)
    date = request.get('date', None)
    if request['method'] == 'POST':
        data = request['data']
        title = decode_value(data['title'])
        text = decode_value(data['text'])
        email = decode_value(data['email'])
        print(f'Пришло сообщение от {email} с темой {title} и текстом {text}')
        return '200 OK', render('contact_post.html', secret=secret, date=date)
    else:
        return '200 OK', render('contact_post.html', secret=secret, date=date)


def contact_get(request):
    secret = request.get('secret_key', None)
    date = request.get('date', None)
    if request['method'] == 'GET' and request['params']:
        params = request['params']
        title = decode_value(params['title'])
        text = decode_value(params['text'])
        email = decode_value(params['email'])
        print(f'Пришло сообщение от {email} с темой {title} и текстом {text}')
        return '200 OK', render('contact_get.html', secret=secret, date=date)
        # Используем шаблонизатор
    else:
        return '200 OK', render('contact_get.html', secret=secret, date=date)


def decode_value(val):
    val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
    val_decode_str = quopri.decodestring(val_b)
    return val_decode_str.decode('UTF-8')
