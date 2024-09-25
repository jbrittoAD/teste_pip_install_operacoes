import numpy as np
from typing import Union

class Operacoes:
    """
    Classe para realizar operações aritméticas básicas e operações com numpy.
    
    Atributos:
        valor (Union[int, float]): O valor inicial para as operações.
    """

    def __init__(self, valor_inicial: Union[int, float] = 0) -> None:
        """
        Inicializa a classe Operacoes com um valor inicial.

        Args:
            valor_inicial (Union[int, float]): Valor inicial para as operações. Padrão é 0.

        Raises:
            TypeError: Se o valor_inicial não for int ou float.
        """
        if not isinstance(valor_inicial, (int, float)):
            raise TypeError(f"O tipo da variável deveria ser int ou float, mas veio {type(valor_inicial).__name__}")
        self.valor: Union[int, float] = valor_inicial

    def set_valor(self, novo_valor: Union[int, float]) -> None:
        """
        Define um novo valor interno para as operações.

        Args:
            novo_valor (Union[int, float]): O novo valor a ser definido.

        Raises:
            TypeError: Se novo_valor não for int ou float.
        """
        if not isinstance(novo_valor, (int, float)):
            raise TypeError(f"O tipo da variável deveria ser int ou float, mas veio {type(novo_valor).__name__}")
        self.valor = novo_valor

    def soma(self, valor: Union[int, float]) -> Union[int, float]:
        """
        Soma o valor interno ao valor passado como parâmetro.

        Args:
            valor (Union[int, float]): Valor a ser somado.

        Returns:
            Union[int, float]: O resultado da soma.

        Raises:
            TypeError: Se o valor não for int ou float.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError(f"O tipo da variável deveria ser int ou float, mas veio {type(valor).__name__}")
        return self.valor + valor

    def subtracao(self, valor: Union[int, float]) -> Union[int, float]:
        """
        Subtrai o valor passado do valor interno.

        Args:
            valor (Union[int, float]): Valor a ser subtraído.

        Returns:
            Union[int, float]: O resultado da subtração.

        Raises:
            TypeError: Se o valor não for int ou float.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError(f"O tipo da variável deveria ser int ou float, mas veio {type(valor).__name__}")
        return self.valor - valor

    def soma_com_numpy(self, valor: Union[int, float]) -> Union[int, float]:
        """
        Soma o valor interno ao valor passado usando numpy.

        Args:
            valor (Union[int, float]): Valor a ser somado.

        Returns:
            Union[int, float]: O resultado da soma.

        Raises:
            TypeError: Se o valor não for int ou float.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError(f"O tipo da variável deveria ser int ou float, mas veio {type(valor).__name__}")
        return np.add(self.valor, valor)
