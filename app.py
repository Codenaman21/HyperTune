from flask import Flask, render_template
from flask_cors import CORS
from routes.dataset import dataset_bp
from routes.model import model_bp
from routes.evaluation import evaluation_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(dataset_bp, url_prefix="/dataset")
app.register_blueprint(model_bp, url_prefix="/model")
app.register_blueprint(evaluation_bp, url_prefix="/evaluation")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
