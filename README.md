# Dev Tool Edit Nginx Configuration in Docker Container

## Descrição
Este projeto é uma ferramenta de desenvolvimento para editar arquivos de configuração do Nginx em containers Docker. Permite aos usuários especificar o nome do container e editar o arquivo `nginx.conf` diretamente através de uma interface web.

---

## Instalação
Siga estas etapas para instalar o projeto:

## Pré-requisitos

Certifique-se de ter o Python e o Docker instalados no seu sistema.

```bash
pip install Flask
```

## Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o aplicativo Flask:

```bash
python app.py
```

O aplicativo estará disponível em http://localhost:5000/.

## Uso

1. Acesse http://localhost:5000/ no seu navegador.
2. Clique em "Editar".
3. Insira o caminho do arquivo (por exemplo, `/etc/nginx/nginx.conf`).
4. Modifique o conteúdo do arquivo conforme necessário.
5. Clique em "Registrar" para salvar as alterações no arquivo e reiniciar o container.

---

## Notas Importantes

- Este projeto é destinado apenas para fins de desenvolvimento local.
- Modificar diretamente arquivos em um container em execução em ambientes de produção é uma prática arriscada.

---

## License

This project is licensed under the MIT License - see file [LICENSE](LICENSE) for details.

---