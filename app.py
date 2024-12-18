from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Use Render's dynamically assigned port
    app.run(host="0.0.0.0", port=port)        # Bind to all interfaces (0.0.0.0)
