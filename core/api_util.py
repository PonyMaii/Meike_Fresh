from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_mobile_belong(self, **kwargs):
        return self.get("/shouji/query", **kwargs)

    def post_data(self, **kwargs):
        return self.post("/posts", **kwargs)

    # 以下项目实战的方法
    def get_code(self, **kwargs):
        return self.post("/code/", **kwargs)

    def register_mobile(self, **kwargs):
        return self.post("/users/", **kwargs)

    def user_login(self, **kwargs):
        return self.post("/login/", **kwargs)

    # goods_api
    #加入购物车
    def shopping_add(self, **kwargs):
        return self.post("/shopcarts/", **kwargs)

    def shopcarts_get(self, **kwargs):
        return  self.get("/shopcarts/", **kwargs)

    def banner(self, **kwargs):
        return self.get("/banners/", **kwargs)

    # 获取收获地址
    def address_get(self, **kwargs):
        return self.get('/address/', **kwargs)

    # 添加收获地址
    def address_add(self, **kwargs):
        return self.post('/address/', **kwargs)

    # 删除收货地址
    def address_del(self, address_id, **kwargs):
        return self.delete(f'/address/{address_id}', **kwargs)

    # 下单接口
    def orders_add(self, **kwargs):
        return self.post("/orders/", **kwargs)


api_util = Api()
