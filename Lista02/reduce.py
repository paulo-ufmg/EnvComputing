
# reduce function
# Calculo de salário sendo comissao(2%) sobre vendas + um fixo
from functools import reduce
fixo = 1412.00
vendas = [1200.89, 2325.00, 199.00, 3599.00,1440.34]
#===========================================
def calculo_comissao(v1,v2):
    """
    Retorna a comissão de 2% sobre o valor da venda (v1 é o somatório)
    """
    return v1 + v2*0.02 
#-------------------------------------------
salario = reduce(calculo_comissao,vendas, fixo)

print(f"Salário fixo + comissões: {'{:.2f}'.format(salario)}") 






