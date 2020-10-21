# remove as aspas duplas, o '\n' de uma linha e a retorna como um array, dividindo pelo ponto-e-vírgula
def removeExcesses(actualLine):
    actualLine = actualLine.replace('"', '')
    actualLine = actualLine.replace('\n', '')
    return actualLine.split(";")


# usando o id do usuário, retorna os dados do usuário
def getUserData(selectedId):
    # selectedId = input("Digite um id: ")
    with open("data/BX-Users.csv", 'r') as usersBX:
        for i in usersBX:
            actualUser = removeExcesses(i)
            if(actualUser[0] == (selectedId)):
                return actualUser


# retorna um array com os dados do livro
def getBookData(isbn):
    # isbn = input("Digite o titulo de um livro ou um ISBN: ")
    with open("data/BX-Books.csv", 'r') as booksBX:
        for i in booksBX:
            actualBook = removeExcesses(i)
            if actualBook[0] == isbn:
                return actualBook


# usando como parametro o isbn, retorna os ids dos usuários que avaliaram esse livro
def getBookReviewers(isbn):
    # isbn = input("Digite o titulo de um livro ou um ISBN: ")
    users = []
    with open("data/BX-Book-Ratings.csv", 'r') as bookRatingsBX:
        for i in bookRatingsBX:
            actualRating = removeExcesses(i)
            if actualRating[1] == isbn:
                users.append(actualRating[0])
        return users


# usando como parametro o id de um usuario, retorna a cidade dele
def getCity(userId):
    actualUser = getUserData(userId)
    actualLocation = actualUser[1].split(',')
    return actualLocation[0]
