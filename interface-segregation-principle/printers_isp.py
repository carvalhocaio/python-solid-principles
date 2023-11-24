from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


"""
Agora Printer, Fax e Scanner são classes base que fornecem interfaces específicas com uma única responsabilidade cada. 
Para criar OldPrinter, apenas a interface Printer é herdada. Dessa forma, a classe não terá métodos não utilizados. Para
criar a classe ModernPrinter, todas as interfaces precisam ser herdadas. Resumindo, a interface Printer foi segregada.

Este design de classe permite criar diferentes máquinas com diferentes conjuntos de funcionalidades, tornando seu design
mais flexível e extensível.
"""
