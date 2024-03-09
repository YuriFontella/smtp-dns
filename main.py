import falcon.asgi

from os import path, getcwd

from config.db import Database

from src.storage.limiter import Limiter
from src.storage.error import StorageError

from src.resources.smtp import SMTPResources

app = falcon.asgi.App(middleware=[Database(), Limiter()], cors_enable=True)

smtp = SMTPResources()

app.add_route('/smtp/email', smtp, suffix='email')
app.add_route('/smtp/emails', smtp, suffix='emails')

app.add_static_route(
    prefix='/files',
    downloadable=True,
    directory=path.join(getcwd(), 'files')
)

app.add_error_handler(Exception, StorageError.handle)