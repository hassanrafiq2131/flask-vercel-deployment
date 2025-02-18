from app.main import app

if __name__ == "__main__":
    import os
    from werkzeug.serving import run_simple

    port = int(os.environ.get("PORT", 8000))
    run_simple("0.0.0.0", port, app)
