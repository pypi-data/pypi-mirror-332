import sys,os,ctypes
import platform
from subprocess import run

def get_program_name() -> str:
    """
    获取当前程序名称
    系统要求:Windows Linux

    返回类型:str
    """

    return sys.argv[0]
    
def get_arg(id:int) -> str:
    """
    获取当前程序传入的参数
    系统要求:Windows Linux

    返回类型:str

    Args:
        id:
            类型:int
            解释:第id个参数
    """

    if(id<=0):
        ValueError("argument:id Error\n请将ID置为大于0的数字")
        exit()
    else:
        return sys.argv[id]
    
def get_run_type_win() -> bool:
    """
    测试当前程序是否使用了管理员身份运行
    系统要求: Windows

    返回类型:bool
    返回值解释:
        True:使用了管理员身份运行
        False:没有使用任何权限
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def get_run_type_other() -> str:
    """
    测试当前程序是否使用了管理员身份运行
    系统要求: Linux/MacOS

    返回类型:bool
    返回值解释:
        True:使用了管理员身份运行
        False:没有使用任何权限
    """
    return os.access("/etc/passwd", os.W_OK)
    
def cmdline(line:str,use_admin:bool=False):
    """
    运行命令
    系统要求: Windows

    返回类型:NULL
    
    Args:
        line:
            类型:str
            解释:欲运行的命令
        use_admin:
            类型:bool
            默认值:False
            解释:是否需要管理员权限
    """
    if use_admin==False:
        run(line,shell=False)
    else:
        runas_admin=get_run_type_win()
        if runas_admin==False:
            SyntaxError("需要提升特权才可以继续")
            exit()
        else:
            run("runas /user:admin "+line,shell=True,check=True)

def get_system_type() -> int:
    """
    检测系统类型
    系统要求:ALL

    返回类型:int
    返回值解释:
        1:Windows
        2.Linux
        3.other
    """
    system_type=platform.system()
    if system_type=="Windows" : return 1
    elif system_type=="Linux" : return 2
    else : return 3 

def run_file(fileName:str):
    """
        从文件运行命令
        系统要求:ALL

        返回类型:null
        详细解释:
            fileName:文件名
            警告，输入'verbose'程序将会读取为'verbose.pycmd'
    """
    with open(f"{fileName}.pycmd","r") as RunFile:
        ConTent=RunFile.read()
        run(ConTent,shell=False)
