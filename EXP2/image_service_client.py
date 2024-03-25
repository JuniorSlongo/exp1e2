from zeep import Client

# URL do WSDL do serviço
wsdl = "http://localhost:8000/?wsdl"

# Criando o cliente SOAP
client = Client(wsdl)

# Chamando o método do serviço para obter o MDC
mdc = client.service.calculate_mdc(1920, 1080)

# Calculando o Aspect Ratio
aspect_ratio_width = 1920 / mdc
aspect_ratio_height = 1080 / mdc

print("Aspect Ratio: {} : {}".format(aspect_ratio_width, aspect_ratio_height))
