import json

with open('imobiliaria.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

imoveis = dados['imoveis']

print('IMÓVEIS:')
for i in range(len(imoveis)):
    print(i+1, '-', imoveis[i]['descricao'])

escolha = int(input('----------------------------\nDigite o número do imóvel: '))

imovel = imoveis[escolha - 1]

print('-------------- Características --------------')
caracteristicas = imovel['caracteristicas']
print('Descrição:', imovel['descricao'])
print('Tamanho:', caracteristicas['tamanho'])
print('Quartos:', caracteristicas['numQuartos'])
print('Banheiros:', caracteristicas['numBanheiros'])
print('Valor:', imovel['valor'])

print('-------------- Proprietário --------------')
proprietario = imovel['proprietario']
print('Nome:', proprietario['nome'])

if proprietario['email'] != None:
    print('Email:', proprietario['email'])
else:
    print('Email: Não informado')

if len(proprietario['telefones']) > 0:
    print('Telefones:', ', '.join(proprietario['telefones']))
else:
    print('Telefones: Não informado')

print('-------------- Endereço --------------')
endereco = imovel['endereco']
print('Rua:', endereco['rua'])
print('Bairro:', endereco['bairro'])
print('Cidade:', endereco['cidade'])

if endereco['numero'] != None:
    print('Número:', endereco['numero'])
else:
    print('Número: S/N')