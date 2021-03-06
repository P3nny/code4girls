from random import randint
from random import choice

from app import app
from flask import render_template
 
@app.route('/')
def lucky_static():
    lucky_num = randint(1, 100)
    return render_template('simple.html', lucky_num=lucky_num)
    
#@app.route('/<max>/')
#def lucky_max(max):
 #   lucky_num = randint(1, int(max))
  #  return render_template('simple.html', lucky_num=lucky_num)

@app.route('/<name>/')
def name_length(name):
	length = len(name)
	return render_template('name.html', name=name.capitalize(), length=length)

@app.route('/horoskop/')
def get_horoskop():
	a = ['In deinen Sternen steht, dass ', 'Auf dem Grunde der Kaffeetasse ist zu lesen, dass ', 'Das Orakel sagt, dass ']
	b = ['Du bald ', 'Du für immer und ewig ', 'Du in deinem Leben ']
	c = ['glücklich wirst.', 'Liebe findest.', 'reich und berühmt wirst.']
	horoskop = choice(a)+choice(b)+choice(c)
	lucky_num = randint(1, 100)
	return render_template('horoskop.html', horoskop=horoskop, lucky_num=lucky_num)
