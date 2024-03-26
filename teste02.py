nome = input('Qual o seu nome? ')
genero = input('Qual o seu gênero? ')

if genero.lower() in ['menina', 'garota', 'feminino', 'mulher']:
    print(f'Bem vinda, {nome}, você é muito querida!')
elif genero.lower() in ['menino', 'garoto', 'homem', 'masculino']:
    print(f'Bem vindo {nome} fracassado!')
else:
    novonome = input('Quem você pensa que é? ')
    print(f'{novonome} você é um transformer!')
