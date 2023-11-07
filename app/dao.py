from app.models import Category, Product

def get_Category():
    return Category.query.all()

def get_Produce(kw):
    produce = Product.query

    if(kw):
        produce = produce.filter(Product.name.contains(kw))

    return produce.all()