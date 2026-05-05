def calcular_corrida():
    print("Calculadora de Corrida Uber\n")

    try:
        distancia = float(input("Distância da corrida (km): "))
        tempo = float(input("Tempo da corrida (minutos): "))
        consumo_medio = float(input("Consumo médio do carro (km/l): "))
        preco_litro = float(input("Preço do litro do combustível (R$): "))
        valor_bandeirada = float(input("Valor da bandeirada (R$): "))
        valor_km = float(input("Valor por km rodado (R$): "))
        valor_minuto = float(input("Valor por minuto rodado (R$): "))
    except ValueError:
        print("Entrada inválida! Por favor, digite números válidos.")
        return

    # Calcular combustível gasto
    combustivel_gasto = distancia / consumo_medio
    custo_combustivel = combustivel_gasto * preco_litro

    # Calcular valor da corrida
    valor_corrida = valor_bandeirada + (valor_km * distancia) + (valor_minuto * tempo)

    # Estimar lucro do motorista
    lucro = valor_corrida - custo_combustivel

    print("\nResumo da Corrida:")
    print(f"Distância: {distancia:.2f} km")
    print(f"Tempo: {tempo:.2f} minutos")
    print(f"Combustível gasto: {combustivel_gasto:.2f} litros")
    print(f"Custo do combustível: R$ {custo_combustivel:.2f}")
    print(f"Valor total da corrida: R$ {valor_corrida:.2f}")
    print(f"Lucro estimado do motorista: R$ {lucro:.2f}")

if __name__ == "__main__":
    calcular_corrida()

