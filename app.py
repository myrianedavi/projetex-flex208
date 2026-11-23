from flask import Flask, render_template
import aluno_service
import curso_service

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", titulo="Minha primeira aplicação Flask")






@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/ola/<nome>")
def ola(nome):
    return render_template("ola.html", nome=nome)





@app.route("/idade/<int:idade>")
def idade(idade):
    return render_template("idade.html", idade=idade)


@app.route("/disciplinas")
def disciplinas():
    lista = ["Progamação Web", "Banco de Dados",
             "Redes", "Inglês Técnico"]
    return render_template("disciplinas.html", disciplinas=lista)


@app.route("/tabuada/<int:n>")
def tabuada(n):
    return render_template("tabuada.html", n=n)

@app.route("/tabuadas")
def tabuadas():
    return render_template("tabuadas.html")



@app.route("/aluno/")
def listar_alunos():
    alunos = aluno_service.listar()
    return render_template("aluno/listar.html", alunos=alunos)




@app.route("/curso/")
def listar_curso():
    curso = curso_service.listar()
    return render_template("curso/lista.html", curso=curso)








if __name__ == "__main__":
    # host=0.0.0.0 permite o encaminhamento da porta no Codespaces.
    app.run(host="0.0.0.0", port=5000, debug=True)

