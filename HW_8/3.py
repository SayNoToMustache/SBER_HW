'''Упражнение 3.
Реализуйте модернизированную версию контекст менеджера File -
теперь, при попытке открыть несуществующий файл, менеджер автоматически создаёт 
и открывает этот файл в режиме записи. 
На выходе из менеджера подавляются все исключения, связанные с файлами.
'''
# Было написано мной на паре


class MyCM:
    def __init__(self, file_path, mod="r"):
        self.file_path = file_path
        self.mod = mod

    def __enter__(self):
        try:
            self.fd = open(self.file_path, self.mod)
        except IOError as io:
            print(io)
            self.fd = open(self.file_path, "w")
        finally:
            return self.fd

    def __exit__(self, exp_type, exp_value, exp_tr):
        if exp_type is IOError:
            self.fd.close()
            return True
        self.fd.close()


with MyCM("HW_8/dads.txt") as pd:
    print(pd.readline())
