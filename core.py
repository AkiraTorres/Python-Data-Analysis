# importações das principais funções
from consults import getRatingsAverage, getReviewersAgeAverage, getReviewsOnCity, getPublisherByNote


condition = True
while condition:
    print("Consultas disponiveis: 02, 06, 11, 18. Digite 00 para sair do codigo")
    consult = input(
        "Bem vindo, digite qual consulta voce deseja realizar: ")

    if consult == "02":
        print("CONSULTA 02 - Qual foi a nota média de avaliações do usuário X?")
        userId = input(
            "Digite o ID do usuario que deseja tirar a media das notas: ")
        averageRating = getRatingsAverage(userId)
        print(averageRating)
    elif consult == "06":
        print(
            "CONSULTA 06 - Mostre a faixa de idade dos usuários que avaliaram um livro X.")
        book = input(
            "Digite o ISBN de um livro para ver a media dos usuarios que o avaliaram: ")
        reviewersAge = getReviewersAgeAverage(book)
        print(reviewersAge)
    elif consult == "11":
        print("CONSULTA 11 - Mostre a média de avaliação de um livro X numa cidade Y.")
        city = input("Digite o nome de uma cidade: ")
        book = input(
            f"Digite o ISBN de um livro para ver a media de avaliacao nele na cidade {city}: ")
        average = getReviewsOnCity(book, city)
        print(average)
    elif consult == "18":
        print("CONSULTA 18 - Dado um usuário X, mostre a Y editora dos livros que ele avaliou com a nota Z.")
        userId = input(
            "Digite o ID do usuario: ")
        note = input("Digite a nota ")
        publishers = getPublisherByNote(userId, note)
        if type(publishers) == str:
            print(publishers)
        else:
            print(
                f"Essas foram as editoras avaliadas pelo usuario {userId} com a nota {note}")
            for i in range(len(publishers)):
                print(publishers[i])
    elif consult == "00":
        condition = False
    else:
        print("Voce digitou uma consulta inexistente, tente novamente")
