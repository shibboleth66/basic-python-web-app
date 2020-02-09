import os
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1

threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}
