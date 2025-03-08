import platform

class CreateCommand:
    def create(QueryFile:str,command:str):
        """
        创建批处理文件
        如果文件没有.bat后缀 程序自动添加

        操作系统:Windows
        """

        
        #检测并且写入
        NewFile=''
        if QueryFile.find('.bat') == -1:
            NewFile=f"{QueryFile}.bat"
        else:
            NewFile=QueryFile
        
        with open(NewFile,"a+") as files:
            files.write(command)
            files.close()

    def __init__() -> bool:
        """
        测试系统是否满足该命令的执行要求
        """

        if platform.system() == "Windows":
            return 1
        else:
            return 0
        
        return 3