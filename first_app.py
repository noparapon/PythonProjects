from test_fw import Application
from test_fw import render
import datetime


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


# Front controllers
def secret_front(request):
    request['secret_key'] = 'some secret'


def date_front(request):
    request['date'] = datetime.datetime.today()


roots = {
    '/': index_view,
    '/about/': about_view
}

front_controllers = [secret_front, date_front]

application = Application(roots, front_controllers)

# gunicorn first_app:application
