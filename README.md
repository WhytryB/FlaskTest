# FlaskTest

Some steps to run:
1) CHeck Flask,  flask_sqlalchemy and flask_migrate
2) Export Global Env for Database with data
export POSTGRES_URL
POSTGRES_USER
POSTGRES_PW   Its not important field, if you have trust seccurity for postgres
POSTGRES_DB
POSTGRES_PORT
and finally  export FLASK_APP=app.py
3) migrate
flask db init
flask db migrate -m "Event"
flask db upgrade

