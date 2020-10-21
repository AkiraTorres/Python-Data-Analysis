from functions import *


# CONSULTA 02 - Qual foi a nota média de avaliações do usuário X?
def getRatingsAverage(userId):
    soma, reviews = 0, 0
    with open("data/BX-Book-Ratings.csv", 'r') as bookRatingsBX:
        for i in bookRatingsBX:
            actualRating = removeExcesses(i)
            if actualRating[0] == userId[0]:
                soma += int(actualRating[2])
                reviews += 1
    if reviews != 0:
        media = soma/reviews
        return f"a media das notas do usuario eh {media:.2f}"
    else:
        return "Erro, confira o codigo inserido e tente novamente"


# CONSULTA 06 - Mostre a faixa de idade dos usuários que avaliaram um livro X.
def getReviewersAgeAverage(isbn):
    users = getBookReviewers(isbn)
    ageSum, reviewersQuantity = 0, 0
    for i in users:
        user = getUserData(i)
        if user[2] != 'NULL':
            ageSum += int(user[2])
            reviewersQuantity += 1
    if reviewersQuantity != 0:
        return f"A media da idade dos usuarios que avaliaram esse livro eh {ageSum / reviewersQuantity:.2f}"
    else:
        return "Erro, confira o codigo inserido e tente novamente"


# CONSULTA 11 - Mostre a média de avaliação de um livro X numa cidade Y.
def getReviewsOnCity(isbn, selectedCity):
    users = getBookReviewers(isbn)
    soma, reviews = 0, 0
    for i in range(len(users)):
        actualCity = getCity(users[i])
        if actualCity == selectedCity:
            with open("data/BX-Book-Ratings.csv", 'r') as bookRatingsBX:
                for j in bookRatingsBX:
                    actualRating = removeExcesses(j)
                    if users[i] == actualRating[0] and isbn == actualRating[1]:
                        soma += int(actualRating[2])
                        reviews += 1
    if reviews != 0:
        return f"A media do livro na cidade de {selectedCity} eh {soma / reviews:.2f}"
    else:
        return "Este livro nao foi avaliado nessa cidade"


# CONSULTA 18 - Dado um usuário X, mostre a Y editora dos livros que ele avaliou com a nota Z.
def getPublisherByNote(userId, note):
    publishers = []
    with open("data/BX-Book-Ratings.csv", 'r') as bookRatingsBX:
        for i in bookRatingsBX:
            actualRating = removeExcesses(i)
            if userId == actualRating[0] and note == actualRating[2]:
                isbn = actualRating[1]
                actualBook = getBookData(isbn)
                publishers.append(actualBook[4])
        if publishers != []:
            return publishers
        else:
            return "Erro, confira o codigo inserido e tente novamente"
