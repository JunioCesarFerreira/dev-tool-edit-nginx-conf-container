from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

nginx_conf_path = '/etc/nginx/nginx.conf'
container_name = ''


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit', methods=['POST'])
def edit():
    container_name = request.form['container_name']
    
    # Recupera o conteúdo atual do arquivo no container
    result = subprocess.run(['docker', 'exec', container_name, 'cat', nginx_conf_path], capture_output=True, text=True)
    current_content = result.stdout

    return render_template('edit.html', file_path=nginx_conf_path, current_content=current_content)

@app.route('/save', methods=['POST'])
def save():
    content = request.form['content']

    # Registra o conteúdo no arquivo no sistema de arquivos local
    with open('nginx.conf', 'w') as f:
        f.write(content)

    # Copia o arquivo para o container
    subprocess.run(['docker', 'cp', 'nginx.conf', f'{container_name}:{nginx_conf_path}'])

    # Reinicia o container
    subprocess.run(['docker', 'restart', container_name])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
    # Apaga o arquivo temporário após a execução do Flask
    temp_file_path = 'nginx.conf'
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)
