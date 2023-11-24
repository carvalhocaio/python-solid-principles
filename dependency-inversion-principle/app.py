class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)


class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"


"""
Neste exemplo, a classe FrontEnd depende da classe BackEnd e de sua implementação concreta. Podemos dizer que ambas as 
classes estão fortemente acopladas. Esse acoplamento pode levar a problemas de escabilidade. Por exemplo, digamos que a
aplicação esteja crescendo rapidamente e gostaríamos que ela seja capaz de ler dados de uma API REST.

Poderíamos adicionar um novo método a BackEnd para recuperar os dados da API REST. No entanto, isso também exigirá que 
FrontEnd seja modificado, que deve ser fechado para modificação, de acordo com o princípio aberto-fechado.

Para corrigir o problema, podemos aplicar o princípio de inversão de dependência e fazer com que suas classes dependam
de abstrações em vez de implementações concretas como BackEnd. Neste exemplo, podemos introduzir uma classe DataSource 
que fornece a interface para usar em suas classes concretas.
"""
