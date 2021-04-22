from solution import db, ma

class RequestModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  n = db.Column(db.Integer, nullable = False)
  grid = db.Column(db.String, nullable = False)
  req_date = db.Column(db.DateTime)
  path = db.Column(db.String, nullable = False)

  
  def __init__(self, n, grid, req_date, path):
    self.n = n 
    self.grid = grid
    self.req_date = req_date
    self.path = path
  


