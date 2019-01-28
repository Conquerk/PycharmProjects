#只处理与users相关的业务

from . import users

@users.route('/01-user')
def user1():
    return "这是user下面的首页"