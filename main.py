print("=== CONVERSOR DE ARMAZENAMENTO")

bytes = float(input("Digite a quantidade de Bytes: "))
kb = float(input("Digite a quantidade de KB"))
mb = float(input("Digite a quantidae de MB: "))

resultado_kb = bytes / 1024
resultado_mb = kb / 1014
resultado_gb = mb / 1024

print("\n=== RESULTADOS ===")

print(f"{bytes} Bytes = {resultado_kb:,2f} KB")
print(f"{bytes} KB = {resultado_mb:,2f} MB")
print(f"{bytes} MB = {resultado_Gb:,2f} GB")


