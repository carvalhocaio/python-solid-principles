from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan funcionality not supported")


class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


"""
Essa implementação viola o princípio de segregação de interface porque força a classe OldPrinter a expor uma interface 
que a classe não implementa ou não precisa. Para corrigir esse problema, é preciso separar as interfaces em classes
menores e mais específicas. Então será possível criar classes concretas herdando de múltiplas classes de interface
conforme necessário.
"""
