from xml.dom.minidom import parse
import json

dom = parse('imobiliaria.xml')
imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName('imovel')

lista_imoveis = []

for imovel in imoveis:
    elemento_descricao = imovel.getElementsByTagName('descricao')[0]
    descricao = elemento_descricao.firstChild.nodeValue

    proprietario = imovel.getElementsByTagName('proprietario')[0]
    elemento_nome = proprietario.getElementsByTagName('nome')[0]
    nome = elemento_nome.firstChild.nodeValue
    
    elemento_email = proprietario.getElementsByTagName('email')
    if elemento_email and elemento_email[0].firstChild is not None:
        emails = elemento_email[0]
        email = elemento_email[0].firstChild.nodeValue
    else:
        email = None
    
    elemento_telefone = proprietario.getElementsByTagName('telefone')
    telefones = [telefone.firstChild.nodeValue for telefone in elemento_telefone]

    proprietario_dict = {
        "nome": nome,
        "email": email,
        "telefones": telefones
    }

    endereco = imovel.getElementsByTagName('endereco')[0]
    elemento_rua = endereco.getElementsByTagName('rua')[0]
    rua = elemento_rua.firstChild.nodeValue
    elemento_bairro = endereco.getElementsByTagName('bairro')[0]
    bairro = elemento_bairro.firstChild.nodeValue
    elemento_cidade = endereco.getElementsByTagName('cidade')[0]
    cidade = elemento_cidade.firstChild.nodeValue
    elementos_numero = endereco.getElementsByTagName('numero')
    if elementos_numero and elementos_numero[0].firstChild is not None:
        numero = elementos_numero[0].firstChild.nodeValue
    else:
        numero = None

    endereco_dict = {
        "rua": rua,
        "bairro": bairro,
        "cidade": cidade,
        "numero": numero
    }

    caracteristicas = imovel.getElementsByTagName('caracteristicas')[0]
    elemento_tamanho = caracteristicas.getElementsByTagName('tamanho')[0]
    tamanho = elemento_tamanho.firstChild.nodeValue
    elemento_numQuartos = caracteristicas.getElementsByTagName('numQuartos')[0]
    quartos = elemento_numQuartos.firstChild.nodeValue
    elemento_numBanheiros = caracteristicas.getElementsByTagName('numBanheiros')[0]
    banheiros = elemento_numBanheiros.firstChild.nodeValue

    caracteristicas_dict = {
        "tamanho": tamanho,
        "numQuartos": quartos,
        "numBanheiros": banheiros
    }

    elemento_valor = imovel.getElementsByTagName('valor')[0]
    valor = elemento_valor.firstChild.nodeValue

    imovel_dict = {
        "descricao": descricao,
        "proprietario": proprietario_dict,
        "endereco": endereco_dict,
        "caracteristicas": caracteristicas_dict,
        "valor": valor
    }

    lista_imoveis.append(imovel_dict)

dados = {
    "imoveis": lista_imoveis
}

with open('imobiliaria.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)

print('Dados convertidos para JSON e salvos em imobiliaria.json')
