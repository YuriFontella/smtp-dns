from tortoise.models import Model
from tortoise.fields import *

class Files(Model):
    name = CharField(max_length=255, null=True, index=True)
    finish=BooleanField(default=False)
    date=DatetimeField(auto_now_add=True)