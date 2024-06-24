import os

# Dicionário para armazenar alunos: {RA: [Nome, Nota B1, Nota B2]}
alunos = {}

def menu():
    # Exibe o menu de opções
    print("\nMenu:")
    print("1 - Adicionar aluno\n2 - Listar alunos\n3 - Remover aluno\n4 - Procurar aluno")
    print("5 - Listar aprovados\n6 - Listar reprovados\n7 - Procurar pelo nome do aluno")
    print("8 - Média da turma B1\n9 - Média da turma B2\n10 - Média da turma geral")
    print("11 - Diário da turma\n0 - Sair")

def obter_nota(mensagem):
    # Função auxiliar para obter e validar uma nota
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! Deve ser um número entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

def adicionar_aluno():
    # Adiciona um novo aluno ao dicionário
    while True:
        ra = input("Digite o RA (5 caracteres): ").strip()
        if len(ra) == 5 and ra.isdigit() and ra not in alunos:
            break
        print("RA inválido ou já existente! Tente outro.")
    
    nome = input("Digite o nome (até 27 caracteres): ").strip()[:27]
    nota_b1 = obter_nota("Digite a nota B1 (0-10): ")
    nota_b2 = obter_nota("Digite a nota B2 (0-10): ")
    alunos[ra] = [nome, nota_b1, nota_b2]
    print("Aluno adicionado com sucesso!")

def listar_alunos():
    # Lista todos os alunos cadastrados
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("RA    Nome                      Nota B1  Nota B2")
    for ra, info in alunos.items():
        print(f"{ra} {info[0].ljust(27)} {str(info[1]).rjust(6)} {str(info[2]).rjust(6)}")

def remover_aluno():
    # Remove um aluno pelo RA
    ra = input("Digite o RA do aluno a ser removido: ").strip()
    if ra in alunos:
        del alunos[ra]
        print("Aluno removido com sucesso!")
    else:
        print("RA não encontrado.")

def procurar_aluno():
    # Procura e exibe informações de um aluno pelo RA
    ra = input("Digite o RA do aluno: ").strip()
    if ra in alunos:
        info = alunos[ra]
        print(f"RA: {ra}\nNome: {info[0]}\nNota B1: {info[1]}\nNota B2: {info[2]}\nMédia: {(info[1] + info[2]) / 2}")
    else:
        print("RA não encontrado.")

def listar_por_status(aprovados=True):
    # Lista alunos aprovados ou reprovados
    status = "aprovados" if aprovados else "reprovados"
    filtrados = {ra: info for ra, info in alunos.items() if (info[1] + info[2]) / 2 >= 7} if aprovados else \
                {ra: info for ra, info in alunos.items() if (info[1] + info[2]) / 2 < 7}
    if not filtrados:
        print(f"Nenhum aluno {status}.")
        return
    print(f"RA    Nome                      Nota B1  Nota B2 ({status.capitalize()})")
    for ra, info in filtrados.items():
        print(f"{ra} {info[0].ljust(27)} {str(info[1]).rjust(6)} {str(info[2]).rjust(6)}")

def procurar_por_nome():
    # Procura e exibe informações de alunos pelo nome
    nome_procurado = input("Digite o nome do aluno: ").strip().lower()
    encontrados = {ra: info for ra, info in alunos.items() if nome_procurado in info[0].lower()}
    if not encontrados:
        print("Nenhum aluno encontrado com esse nome.")
        return
    print("RA    Nome                      Nota B1  Nota B2")
    for ra, info in encontrados.items():
        print(f"{ra} {info[0].ljust(27)} {str(info[1]).rjust(6)} {str(info[2]).rjust(6)}")

def calcular_media(bimestre):
    # Calcula e exibe a média das notas do bimestre especificado
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media = sum(info[bimestre] for info in alunos.values()) / len(alunos)
    print(f"Média da turma {'B1' if bimestre == 1 else 'B2'}: {media:.2f}")

def media_turma_geral():
    # Calcula e exibe a média geral da turma
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    media_geral = sum((info[1] + info[2]) / 2 for info in alunos.values()) / len(alunos)
    print(f"Média geral da turma: {media_geral:.2f}")

def diario_turma():
    # Exibe o diário da turma com formatação específica
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("-" * 56 + "\nDiário da turma".center(56) + "\n" + "-" * 56)
    print("RA    Nome                      Nota B1  Nota B2   Média")
    print("-" * 56)
    total_b1, total_b2, total_geral = 0, 0, 0
    for ra, info in alunos.items():
        media = (info[1] + info[2]) / 2
        total_b1 += info[1]
        total_b2 += info[2]
        total_geral += media
        print(f"{ra} {info[0].ljust(27)} {str(info[1]).rjust(6)} {str(info[2]).rjust(6)} {str(media).rjust(6)}")
    n = len(alunos)
    print("-" * 56)
    print(f"Médias da Turma {'':<20} {str(total_b1 / n):<6} {str(total_b2 / n):<6} {str(total_geral / n):<6}")
    print("-" * 56)

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            adicionar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            remover_aluno()
        elif opcao == '4':
            procurar_aluno()
        elif opcao == '5':
            listar_por_status(True)
        elif opcao == '6':
            listar_por_status(False)
        elif opcao == '7':
            procurar_por_nome()
        elif opcao == '8':
            calcular_media(1)
        elif opcao == '9':
            calcular_media(2)
        elif opcao == '10':
            media_turma_geral()
        elif opcao == '11':
            diario_turma()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
        input("Pressione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
