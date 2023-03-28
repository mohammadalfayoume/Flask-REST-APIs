from db import db

class StoreModel(db.Model):
    __tablename__= "stores"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True,nullable=False)
    items= db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    # cascade="all, delete" it means when you delete store, delete all items related to this store also
    # tags= db.relationship("TagModel", back_populates="store", lazy="dynamic")
    