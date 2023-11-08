from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product
from app import  app, db
from flask_admin import Admin

admin = Admin(app, name="Quan ly ban hang",
template_mode="bootstrap4")

class MyProduceView(ModelView):
    can_export = True
    can_edit = True
    column_list = ['id', 'name', 'price']
    # tim kiem san pham theo ten
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    # cho phep chinh sua truc tiep
    column_editable_list = ['name', 'price']
    edit_modal = True

class MyCategoryView(ModelView):
    column_list = ['name', 'products']

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProduceView(Product, db.session))