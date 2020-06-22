from flask import Flask 
from blog.core.controllers import core 

app = Flask(__name__)
app.register_blueprint(core)
