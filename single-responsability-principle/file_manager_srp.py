from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


"""
O conceito de responsabilidade neste contexto pode ser bastante subjetivo. Ter uma única responsabilidade não significa
necessariamente ter um único método. A responsabilidade não está diretamente ligada ao número de métodos, mas à tarefa
principal pela qual sua classe é responsável, dependendo da ideia do que a classe representa em seu código.
"""
