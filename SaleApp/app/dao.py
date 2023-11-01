def get_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },
    {
        'id': 2,
        'name': 'Tablet'
    }
    ]

def get_products(kw):
    products = [{
        'id':1,
        'name':'iPhone 13',
        'price':'20000000',
        'image': "https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy"
    },
        {
            'id': 2,
            'name': 'iPhone 18',
            'price': '20000000',
            'image': "https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy"

        },
        {
            'id': 3,
            'name': 'iPhone 14',
            'price': '20000000',
            'image': "https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy"

        },{
            'id': 4,
            'name': 'iPhone 14 Pro',
            'price': '20000000',
            'image': "https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy"

        },{
            'id': 5,
            'name': 'iPhone 15',
            'price': '20000000',
            'image': "https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy"

        },{
            'id': 6,
            'name': 'iPhone 15 Pro',
            'price':'20000000',
            'image': "https://images.macrumors.com/t/9r84bU_ZTOTrUixxwhjHUFsAvD4=/800x0/smart/article-new/2017/09/iphonexdesign.jpg?lossy"

        }
    ]

    if kw:
        products = [p for p in products if p['name'].find(kw)>=0 ]

    return products