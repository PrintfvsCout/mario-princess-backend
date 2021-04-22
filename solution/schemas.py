
from solution import db, ma

class RequestSchema(ma.Schema):
  class Meta:
    fields = ('id','n','grid','req_date','path')

