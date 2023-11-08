from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    kw = request.args.get('kw')

    cates = dao.get_Category()
    prods = dao.get_Produce(kw)
    # tạo biến để lấy database, import thư mục chứa data
    return render_template('index.html', categories=cates, products=prods)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
