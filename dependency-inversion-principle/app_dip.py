from abc import ABC, abstractmethod


class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"


"""
Nesta reformulação de suas classes, adicionamos uma classe DataSource como uma abstração que fornece a interface 
necessária, ou o método .get_data(). Observe como FrontEnd agora depende da interface fornecida por DataSource, que é 
uma abstração.

Depois definimos a classe Database, que é uma implementação concreta para aqueles casos em que desejamos recuperar os 
dados do seu banco de dados. Esta classe depende da abstração de DataSource por herança. Finalmente, definimos a classe 
API para suportar a recuperação dos dados da API REST. Esta classe também depende da abstração de DataSource. 
"""
