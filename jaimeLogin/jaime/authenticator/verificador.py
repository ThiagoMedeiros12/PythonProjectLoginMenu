
#def login(inputLogin):
    #verificar inputLogin no db e retornar True
    #se nao retornar false

#def senha(inputSenha):
    #verificar se senha é == a senha do login selecionado se True retornar True
    #se nao retornar false


def autenticar(login,senha):
    checkSenha = False
    checkLogin = False

    if login == True:
        if login == True and senha == True:
            return True
        else:
            checkSenha = False
            return False, checkSenha
    else:
        checkLogin = False
        return False, checkLogin



       