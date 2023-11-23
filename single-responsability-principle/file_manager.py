from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __int__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


"""
Neste exemplo, a classe FileManager tem duas responsabilidades diferentes. Ela usa os métodos .read() e .write() para
gerenciar o arquivo. E também lida com arquivos ZIP fornecendo os métodos .compress() e decompress().

Esta classe viola o príncipio de responsabilidade única porque tem duas razões para alterar sua implementação interna.
Para corrigir esse problema e tornar seu design mais robusto, você pode dividir a classe em duas classes menores e mais
focadas, cada uma com sua preocupação específica. (veja em file_manager_srp.py)
"""
