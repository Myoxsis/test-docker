from flask import Flask
from redis import Redis, RedisError
import os
import socket

#Connect to redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
	try:
		visites = redis.incr("compteur")
	except RedisError:
		visites = "<i>erreur de connexion a redis, compteur désactivé</i>"

	html = "<h3> Bonjour {nom}!</h3>" \
			"Hostname : {hostname}<br/>" \
			"Visites : {visites}<br/>"

	return html.format(nom=os.getenv("NOM", "youtube"), hostname=socket.gethostname(), visites=visites)

@app.route("/bye")
def bye():
	try:
		visites = redis.incr("compteur")
	except RedisError:
		visites = "<i>erreur de connexion a redis, compteur désactivé</i>"

	html = "<h3> Bonjour {nom}!</h3>" \
			"BYE<br/>"

	return html.format(nom=os.getenv("NOM", "youtube"), hostname=socket.gethostname(), visites=visites)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)