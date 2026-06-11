import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

op = input("1 para Moeda do país\n2 para DDI do país\n3 para Nome do país\n")
country_code = input("Digite o código do país: ")

if op == "1":
    operation = "CountryCurrency"
elif op == "2":
    operation = "CountryIntPhoneCode"
elif op == "3":
    operation = "CountryName"
else:
    print("Número Invalido") 
    exit()



payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{operation} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{country_code}</sCountryISOCode>
					</{operation}>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.status_code == 200:
    if op == "1":
        response = parseString(response.text).documentElement.getElementsByTagName("m:sName")[0].firstChild.nodeValue
    elif op == "2":
        response = parseString(response.text).documentElement.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue
    elif op == "3":
        response = parseString(response.text).documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue
    print (response)

