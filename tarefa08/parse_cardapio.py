from xml.dom.minidom import parse

dom = parse('cardapio.xml')

cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName('prato')
print("Pratos disponíveis:")
for prato in pratos:
    id = prato.getAttribute('id')
    elemento_nome = prato.getElementsByTagName('nome')[0]
    nome = elemento_nome.firstChild.nodeValue
    print(f"{id} - {nome}")
escolha = input('--------------------------------------------------\nDigite o ID do prato para mais informações: ')

for prato in pratos:
    id = prato.getAttribute('id')

    elemento_nome = prato.getElementsByTagName('nome')[0]
    nome = elemento_nome.firstChild.nodeValue

    elemento_descricao = prato.getElementsByTagName('descricao')[0]
    descricao = elemento_descricao.firstChild.nodeValue

    elemento_preco = prato.getElementsByTagName('preco')[0]
    preco = elemento_preco.firstChild.nodeValue

    ingredientes = prato.getElementsByTagName('ingrediente')
    ingrediente = [ingrediente.firstChild.nodeValue for ingrediente in ingredientes]

    elemento_calorias = prato.getElementsByTagName('calorias')[0]
    calorias = elemento_calorias.firstChild.nodeValue

    elemento_tempoPreparo = prato.getElementsByTagName('tempoPreparo')[0]
    tempoPreparo = elemento_tempoPreparo.firstChild.nodeValue

    if escolha == id:
        print('--------------------------------------------------')
        print(f'Prato: {nome}')
        print(f'Descrição: {descricao}')
        print(f'Preço: R${preco}')
        print(f'Ingredientes: {", ".join(ingrediente)}')
        print(f'Calorias: {calorias} kcal')
        print(f'Tempo de Preparo: {tempoPreparo} minutos')
        break
else:
    print('Prato não encontrado.')


    

