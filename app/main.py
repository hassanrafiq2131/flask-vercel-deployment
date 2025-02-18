from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App Successfully Deployed on Vercel with GitHub Actions!"


if __name__ == "__main__":
    app.run(debug=True)
