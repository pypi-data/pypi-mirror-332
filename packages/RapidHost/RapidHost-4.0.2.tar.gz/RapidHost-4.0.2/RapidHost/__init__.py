from flask import Flask, render_template, request, jsonify, redirect
import time

app = Flask(__name__)
host_ip = '127.0.0.1'
host_port = 5000
template_path = 'templates'
static_path = 'static'
routes_data = {}

def hostSite(*pages, information):
    app.template_folder = template_path
    app.static_folder = static_path  # Define o caminho da pasta estática

    for page in pages:
        route = '/' + page.split('.')[0] if page != 'index.html' else '/'

        def render_specific_page(page=page):
            return render_template(page, info=information)

        app.add_url_rule(route, endpoint=route, view_func=render_specific_page)

    app.run(host=host_ip, port=host_port, debug=True)

def hostIP(ip):
    global host_ip
    host_ip = ip

def hostPort(port):
    global host_port
    host_port = port

def setTemplatePath(path):
    global template_path
    template_path = path
    app.template_folder = template_path

def setStaticPath(path):
    global static_path
    static_path = path
    app.static_folder = static_path  # Define o diretório de arquivos estáticos

def create_route(route_name, returnMessage):
    def route_function(route_name=route_name, returnMessage=returnMessage):
        if request.method == 'POST':
            data = request.form.to_dict()
            routes_data[route_name] = data
            time.sleep(0.5)

            if returnMessage.startswith("http://") or returnMessage.startswith("https://"):
                return redirect(returnMessage, code=302)

            return returnMessage, 200

        return jsonify(routes_data.get(route_name, {}))

    app.add_url_rule(f'/{route_name}', endpoint=f'route_{route_name}', view_func=route_function, methods=['GET', 'POST'])

def GetfromRoute(route_name, info=""):
    data = routes_data.get(route_name, {})
    return data if info == "" else data.get(info, None)
