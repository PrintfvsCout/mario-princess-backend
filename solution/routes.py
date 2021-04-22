from flask import Flask, request, jsonify
from solution import app, db

from solution.models import RequestModel
from solution.schemas import RequestSchema
from datetime import datetime

from solution.algorithms.constants import *
from solution.algorithms.utils import *
from solution.algorithms.algorithms import *

import ast
import numpy as np
import json

request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)

@app.route('/sendinput', methods=['POST'])
def send_grid():
  n = request.json['n']
  grid = request.json['grid']

  if validate_grid(n,grid):

    grid_list = ast.literal_eval(grid)

    matric = to_matrix(grid_list)

    start_pos = find_marion_position(matric)

    pp = find_princess(matric,n,start_pos[0],start_pos[1])

    path_string = ','.join(pp)

    solved_path= RequestModel(n,grid,datetime.now(),path_string)
    
    if len(pp) > 0:
      db.session.add(solved_path)
      db.session.commit()
      
    return jsonify({'error_flag': False, 'paths': pp})
  else:
    return jsonify({'error_flag': True})


@app.route('/getresults', methods=['GET'])
def get_grid_paths():
  all_results = RequestModel.query.all()
  result = requests_schema.dump(all_results)
  return jsonify(result)

@app.route('/getresults/<id>', methods=['DELETE'])
def delete_row(id):
  row = RequestModel.query.get(id)

  if row is None:
    return jsonify({'error_flag': True, '404':"Request with that id not found"})
  else:
      db.session.delete(row)
      db.session.commit()
    
  return jsonify({'error_flag': False})
