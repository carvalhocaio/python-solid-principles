# Princípio de Segregação de Interface

O princípio de segreação de interface afirma que: "Os clientes não devem ser forçados a depender de métodos que não
utilizam. As interfaces pertencem aos clientes, não às hierarquias."

Neste caso *clientes* são classes e sublclasses, e *interfaces* consistem em métodos e atributos. Em outras palavras, se
uma classe não usa métodos ou atributos específicos, então esses métodos e atributos devem ser segregação em classes
mais específicas.