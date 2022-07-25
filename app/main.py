import uvicorn
import multiprocessing
from api import app

workers = multiprocessing.cpu_count() * 2 + 1


if __name__ == '__main__':
    uvicorn.run('api:app', host='0.0.0.0', port=8000, log_level='trace', reload=True, workers=workers)

