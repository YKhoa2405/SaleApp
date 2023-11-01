from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app import db, app


# Tao bangcategory
class Category(db.Model):
    __tablename__ = 'category'
    # tao tung column cho bang
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product',backref='category',lazy=True)

class Product(db.Model):
    __tablename__ ='product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    category_id =Column(Integer, ForeignKey(Category.id),nullable=False)

if __name__ == '__main__':
    with app.app_context():
        # add data vao bang
        c1 = Category(name='Mobie')
        c2 = Category(name='Laptop')

        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()
        db.create_all()


