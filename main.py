from zeep import Client

# URL do WSDL
wsdl = "http://www.dneonline.com/calculator.asmx?WSDL"

# Criando o cliente SOAP
client = Client(wsdl)

# Chamando os métodos do serviço
print("Add: ", client.service.Add(10, 20))
print("Subtract: ", client.service.Subtract(20, 10))
print("Multiply: ", client.service.Multiply(10, 5))
print("Divide: ", client.service.Divide(20, 5))