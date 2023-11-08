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

    def __str__(self):
        return self.name

class Product(db.Model):
    __tablename__ ='product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(500))
    category_id =Column(Integer, ForeignKey(Category.id),nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Mobie')
        # c2 = Category(name='Laptop')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        # db.create_all()
        p1 = Product(name = 'Iphone13', price = 20000, category_id =1,image ="https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy")
        p2 = Product(name = 'Iphone14', price = 20000, category_id =2,image ="https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy")
        p3 = Product(name = 'Iphone15', price = 20000, category_id =1,image ="https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy")
        p4 = Product(name = 'Iphone16', price = 20000, category_id =2,image ="https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy")
        p5 = Product(name = 'Iphone17', price = 20000, category_id =1,image ="https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy")

        db.session.add_all([p1,p2,p3,p4,p5])
        db.session.commit()
