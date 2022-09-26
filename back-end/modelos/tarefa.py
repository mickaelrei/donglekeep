from geral.config import *
from modelos.lista_tarefa import *

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.Text, nullable=False)
    concluido = db.Column(db.Boolean, default=False, nullable=False)
    lista_tarefa_id = db.Column(db.Integer, db.ForeignKey(ListaTarefa.id), nullable=False)

    def json(self) -> dict:
        return {
            "conteudo": self.conteudo,
            "concluido": self.concluido
        }