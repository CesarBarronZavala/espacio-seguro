#!/usr/bin/env python3
import http.server, socketserver, os, webbrowser, threading

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        if len(args) > 1 and args[1] not in ('200', '304'):
            super().log_message(format, *args)

def abrir():
    import time; time.sleep(1.2)
    webbrowser.open('http://localhost:' + str(PORT))

print('=' * 55)
print('  Espacio Seguro - Servidor Local')
print('=' * 55)
print('  Abre tu navegador en: http://localhost:' + str(PORT))
print('  Para detener: Ctrl + C')
print('=' * 55)

t = threading.Thread(target=abrir, daemon=True); t.start()
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    try: httpd.serve_forever()
    except KeyboardInterrupt: print('Servidor detenido.')
