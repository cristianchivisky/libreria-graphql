from api_config import db

class LineaPedido(db.Model):
    __tablename__ = "linea_pedido"
    id_pedido = db.Column(db.Integer, db.ForeignKey("pedido.id_pedido"), nullable=False, primary_key=True)
    id_ejemplar = db.Column(db.String(13), db.ForeignKey("ejemplar.isbn"), nullable=False, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    pedido = db.relationship("Pedido", backref="lineas_pedido")
    ejemplar = db.relationship("Ejemplar", backref="lineas_pedido")
