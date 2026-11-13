# 3- Em uma cidade do interior, sabe-se que de janeiro a abril de 1976 
# (121 dias) não ocorreu temperatura inferior a 15o C e nem superior a 
# 40o C. Fazer um programa JS que determine: 
# a) A menor temperatura ocorrida 
# b) A maior temperatura ocorrida 
# c) A temperatura média do período  

temperaturas = []
for i in range(121):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    if 15 <= temp <= 40:
        temperaturas.append(temp)
    else:
        print("Temperatura inválida. Por favor, digite uma temperatura entre 15 e 40.")

menor_temp = min(temperaturas)
maior_temp = max(temperaturas)
media_temp = sum(temperaturas) / len(temperaturas)

print(f"a) A menor temperatura ocorrida foi: {menor_temp}")
print(f"b) A maior temperatura ocorrida foi: {maior_temp}")
print(f"c) A temperatura média do período foi: {media_temp}")
