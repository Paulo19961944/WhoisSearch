import whois

domain = input("Digite um Domínio:")
print(domain)
consulta = whois.whois(domain)
print (consulta.email)
print (consulta.text)