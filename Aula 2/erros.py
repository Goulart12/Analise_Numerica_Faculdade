#Determinação de erros

QE = float(input("Entre com o valor exato: "));

QAPROX = float(input("Entre com o valor aproximado: "));

EA = abs(QE-QAPROX);
print('Erro Absoluto:' , EA);

ER = (abs(QE-QAPROX) / QE);
print('Erro Relativo:', ER);

EP = (abs(QE-QAPROX) / QE) * 100
print('Erro Percentual:' , EP, '%')