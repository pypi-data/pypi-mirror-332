from subprocess import run
def create_user(username:str,password:str):
    """
    新建用户

    username:用户名
    password:密码 留空则不设置

    需要提升权限
    """
    cmd='net user '+username+' "'+password+'" /add'
    run(cmd,shell=True)

def delete_user(username:str):
    """
    删除用户

    username:用户名

    需要提升权限
    """
    cmd='net user '+username+' /del'
    run(cmd,shell=True)
