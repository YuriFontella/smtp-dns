import asyncio
import falcon

from src.storage.limiter import limiter

from scripts.deliver import deliver
from scripts.main import emails

@limiter.limit()
class SMTPResources:
    async def on_get_email(self, req, resp):
        email = req.get_param('email', True)
        status, message = await deliver(email)

        resp.media = {
            'status': status,
            'message': message
        }

    async def on_post_emails(self, req, resp):
        try:
            media = await req.media
            if 'emails' not in media:
                raise falcon.HTTPBadRequest(description='The email field was not provided')

            data = media['emails']
            task = asyncio.create_task(emails(data))

            def callback(x):
                x.cancel()

            task.add_done_callback(callback)

        except falcon.MediaNotFoundError:
            raise falcon.HTTPBadRequest(description='Provide an email list')

        else:
            resp.media = True