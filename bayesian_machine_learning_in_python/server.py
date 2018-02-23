'''
Created on 23 Feb 2018

@author: filipe
'''
import numpy as np
from flask import Flask, jsonify, request
from scipy.stats import beta

# create an app
app = Flask(__name__)


# define bandits
# there's no "pull arm" here
# since that's technically now the user/client
class Bandit:
  def __init__(self, name):
    self.name = name

  def sample(self):
    # TODO
    return 1

  # TODO - what else does the Bandit need to do?


# initialize bandits
banditA = Bandit('A')
banditB = Bandit('B')



@app.route('/get_ad')
def get_ad():
  # TODO
  return jsonify({'advertisement_id': 'A'})


@app.route('/click_ad', methods=['POST'])
def click_ad():
  result = 'OK'
  if request.form['advertisement_id'] == 'A':
    # TODO
    pass
  elif request.form['advertisement_id'] == 'B':
    # TODO
    pass
  else:
    result = 'Invalid Input.'

  # nothing to return really
  return jsonify({'result': result})


if __name__ == '__main__':
  app.run(host='127.0.0.1', port='8888')