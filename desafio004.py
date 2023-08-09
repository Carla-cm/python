a = input ('Digite algo: \n')
print('O tipo primitivo desse valor é: ', type(a))
    
if a.isalnum():
    print(f'{a} é alfanúmerico. ')
else: 
    print(f'{a} não é alfanúmerioco. ')
    
if a.isalpha():
    print(f'{a} é composto somente por letras. ')
else:
    print(f'{a} não é composto somente por letras. ')
    
if a.isnumeric():
    print(f'{a} é compoto apenas por números. ')
else:
    print(f'{a} não é composto apenas por números. ')
    
if a.isdigit():
    print(f'{a} é um digito. ')
else: 
    print(f'{a} não é um digito. ')    
    
if a.isdecimal():
    print(f'{a} é um número decimal. ')
else: 
    print(f'{a} não é um número decimal. ')
    
if a.isprintable():
    print(f'{a} é um termo imprimivel. ')        
else: 
    print(f'{a} não é um termo imprimivel. ')
        
if a.isspace():    
      print(f'{a} é um espaço vazio. ')  
else: 
    print(f'{a} não é um espaço vazio. ')
        