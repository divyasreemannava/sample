from flask import Flask
from flask_cors import CORS
from configparser import ConfigParser
from services.routes.create_user import user_routes
from services.routes.assistants.getAssistants import assistant_routes
# from services.routes.threadRoutes import thread_routes
from services.routes.threads.create_getResponse import response_route
from services.routes.files.fileUpload import file_routes
from services.routes.threads.deleteThread import delete_route
from services.routes.threads.getAllMessages import all_messages_routes
from services.routes.threads.getAllThreads import all_sessions_routes
from services.routes.login import login_routes
from services.routes.assistants.createassistants import create_assistant_routes
from services.routes.annotations.functionaAnnotations import annotation_routes
from services.routes.single_prompt_assistant.single_prompt_response import copilot_routes

from models import MongoEngine
from consul import Consul
import app_data
# from dotenv import load_dotenv
# import os

app = Flask(__name__)
CORS(app)
config = ConfigParser()
# print(app_data.host)
app.config['MONGODB_SETTINGS'] = {
    'host': f"mongodb://{app_data.username}:{app_data.password}@{app_data.host}/{app_data.database}?authSource=admin&maxIdleTimeMS=60000&retryWrites=true"
}
db = MongoEngine(app)
# configure_app_with_consul(app)
# Register blueprints
app.register_blueprint(user_routes)
app.register_blueprint(assistant_routes)
app.register_blueprint(response_route)
app.register_blueprint(delete_route)
app.register_blueprint(all_messages_routes)
app.register_blueprint(create_assistant_routes)
app.register_blueprint(all_sessions_routes)
app.register_blueprint(file_routes)
app.register_blueprint(annotation_routes)
app.register_blueprint(login_routes)
app.register_blueprint(copilot_routes)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)