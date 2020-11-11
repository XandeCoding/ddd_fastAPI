from infrastructure import framework
import uvicorn


if __name__ == '__main__':
    app = application = uvicorn.run(framework.app, host='0.0.0.0', port=8000)