from flask import Flask
from flask_cors import CORS
from routes.chat import chat_bp
from routes.history import history_bp

def create_app():
    app = Flask(
        __name__,
        template_folder="../frontend/templates",
        static_folder="../frontend/static"
    )

    CORS(app)

    # Register blueprints
    app.register_blueprint(chat_bp, url_prefix="/api/chat")
    app.register_blueprint(history_bp, url_prefix="/api/history")

    # Serve frontend
    from flask import render_template
    @app.route("/")
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
