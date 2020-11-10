from infrastructure.infrastructure import app
import uvicorn


if __name__ == '__main__':
    app = application = uvicorn.run(app, host='0.0.0.0', port=8000)