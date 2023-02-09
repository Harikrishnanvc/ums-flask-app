from . import user_app
from core.user_app.views import CreateAndListUsers, DeleteView

user_app.add_url_rule('/', view_func=CreateAndListUsers.as_view('create-and-list-users'))
user_app.add_url_rule('/update-or-delete/<pk>', view_func=DeleteView.as_view('delete-user'))

