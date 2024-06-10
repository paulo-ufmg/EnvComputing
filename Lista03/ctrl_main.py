"""Controlador principal do pipeline"""
import os
import sys
import subprocess
processos = ['a','b','c','d','e']
#--------------------------------------
def run_cmd(cmd):
    try:
        # Executa o comando e captura a saída
        resultado = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Exibe a saída do comando
        print(resultado.stdout)
        
        # Exibe erros, se houver
        if resultado.stderr:
            print("Erros do comando:")
            print(resultado.stderr)
        
    except subprocess.CalledProcessError as e:
        print(f"O comando falhou com o código de retorno {e.returncode}")
        print(f"Erro: {e.stderr}")
#========================================

dir_script = os.path.dirname(os.path.realpath(__file__))

#executa o script a.py
print("\033[33ma)===============================run a.py\033[0m")
cmd = r"python " + dir_script + os.sep + "lib"+ os.sep + "a.py -i " + dir_script + os.sep + "genoma.fasta"
#run_cmd(cmd)
print("\n")



#executa o script b.py
print("\033[33mb)===============================run b.py\033[0m")
cmd = r"python " + dir_script + os.sep + "lib"+ os.sep + "b.py -i " + dir_script + os.sep + "genoma.fasta"
#run_cmd(cmd)
print("\n")


#executa o script c.py
print("\033[33mc)===============================run c.py\033[0m")
cmd = r"python " + dir_script + os.sep + "lib"+ os.sep + "c.py -i " + dir_script + os.sep + "genoma.fasta"
#run_cmd(cmd)
print("\n")

#executa o script d.py
print("\033[33md)===============================run d.py\033[0m")
cmd = r"python " + dir_script + os.sep + "lib"+ os.sep + "d.py -i " + dir_script + os.sep + "genoma.fasta"
run_cmd(cmd)
print("\n")

