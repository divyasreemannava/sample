from flask import Flask
from flask_cors import CORS
from configparser import ConfigParser
from services.routes.create_user import user_routes
from services.routes.assistants.getAssistants import assistant_routes
from services.routes.files.fileUpload import file_routes
from services.routes.threads.create_getResponse import response_route
from services.routes.threads.deleteThread import delete_route
from services.routes.threads.getAllMessages import all_messages_routes
from services.routes.threads.getAllThreads import all_sessions_routes
from services.routes.assistants.createassistants import create_assistant_routes
from services.routes.annotations.functionaAnnotations import annotation_routes
from services.routes.login import login_routes
from services.routes.tokens_calculation.token_calculation import token_route
from services.routes.single_prompt_assistant.single_prompt_response import copilot_routes
from models import MongoEngine
app = Flask(__name__)
CORS(app)
config = ConfigParser()
app.config['MONGODB_SETTINGS'] = {    
            # mongo connection
    'host': f"mongodb://mobius:GaianAdmin8086@192.168.28.3:27017/mobiusgptservice?authSource=admin&maxIdleTimeMS=60000&retryWrites=true"
    # 'host': 'mongodb+srv://divyasreemannava:chat@cluster0.9x90s8n.mongodb.net/?retryWrites=true&w=majority'
}
db = MongoEngine(app)
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
app.register_blueprint(token_route)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)