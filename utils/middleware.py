from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddlewareMixin(MiddlewareMixin):

    def process_request(self, request):
        # 不用登录就可以直接访问处理
        if request.path_info in ['/login/', '/img/code/', '/edit/password/', '/admin/add/']:
            return

        # 获取session信息
        info_dict = request.session.get('info')
        # 未登录
        if not info_dict:
            return redirect("/login/")

        # 已登录
        request.info_dict = info_dict
