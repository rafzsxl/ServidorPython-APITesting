from http.server import HTTPServer, BaseHTTPRequestHandler

class Servidor(BaseHTTPRequestHandler):

    # Método GET (já usado na ultima aula)
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor funcionando com GET")

    # Método POST (novo)
    def do_POST(self):
        # pega o tamanho dos dados enviados na requisição
        tamanho = int(self.headers['Content-Length'])

        # lê os dados enviados
        dados = self.rfile.read(tamanho)

        # mostra os dados recebidos no terminal
        print("Dados recebidos:", dados.decode())

        # envia resposta para o cliente
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST recebido")

HTTPServer(("0.0.0.0", 8000), Servidor).serve_forever()