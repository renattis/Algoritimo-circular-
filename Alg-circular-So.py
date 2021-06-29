def circular(fila_de_processos, quantum, troca_de_contexto):
    turn_around = [0] * len(fila_de_processos)  
    tempo_atual = 0  

    
                else:
                    tempo_atual += quantum
                    fila_de_processos[i] -= quantum

                    print(f"\nP{i} executa")
                    print(f"Termino em T-{tempo_atual}")
                    print("TROCA DE CONTEXTO")
                    tempo_atual += troca_de_contexto
                    turn_around[i] = tempo_atual
            print("-" * 30)

    print(f"tempo onde Terminou cada processo: {turn_around}")
    return turn_around


def tempo_atual_medio_turnaround(lista_de_processos, lista_de_tempos):
    resultado = sum(lista_de_tempos) / (len(lista_de_processos))
    print(f"Tempo Médio de Turnaround = {resultado:.2f}")


if __name__ == '__main__':
    fila_de_processos = [10, 7, 8]

    quantum = 3

    troca_de_contexto = 1

    turnAround = circular(fila_de_processos, quantum, troca_de_contexto)

    tempo_atual_medio_turnaround(fila_de_processos, turnAround)
