from test_fw import Application, render
import views
import datetime


roots = {
    '/': views.index_view,
    '/about/': views.about_view,
    '/contact_post/': views.contact_post,
    '/contact_get/': views.contact_get
}


# Front controllers
def secret_front(request):
    request['secret_key'] = roots.keys()


def date_front(request):
    request['date'] = datetime.datetime.today()


front_controllers = [secret_front, date_front]

application = Application(roots, front_controllers)

# gunicorn first_app:application
