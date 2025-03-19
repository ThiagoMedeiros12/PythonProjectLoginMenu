from asyncio import open_connection
from tkinter import Button
from turtle import onclick
from reactpy import component, html, hooks

 
def verify(evento):   
    print(evento)  
    

@component
def Login():
    
    componente = html.div(

        html.h2("Digite seu login"),
        html.input(),
        html.h2("Digite sua senha"),
        html.input(),
        html.button("Login"),
        )
    
    return componente


@component
def HelloWorld():
    pagina = html.div(
        html.h1("Bem vindo!"),
        html.p("Esse e o meu primeiro projeto"),
        Login(),
        )
    return pagina


@component
def loginSucess():
    pagina = html.div(
        html.h1("Parabens voce fez login !!"),
       )
    return pagina



