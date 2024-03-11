def soma(num1, num2):
    resultado = num1 + num2
    return resultado

def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado

def dividir(a,b):
    return a/b

def multiplicar (a,b):
    c=a*b
    return c


print("Operações\n[1]Soma\n[2]Subtração\n[3]Divisão\n[4]Mutiplicação")

op = int(input("Digite a operação desejada"))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


if op==1:
    print(soma(num1,num2))

elif op==2:
   print(subtracao(num1,num2))

elif op==3:
    print(dividir(num1,num2))

elif op==4:
    print(multiplicar(num1,num2))

else:
    print("Valor Inválido")

