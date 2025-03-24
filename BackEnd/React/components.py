from os import link
from django.shortcuts import redirect
from BackEnd.React.views import loginIndex
from reactpy import component, html

@component
def Login():
    componente = html.div(
        {
            "style": {
                "align_items": "center",
                "text_align": "center",
                "margin": "auto",
                "width": "50%",
                "padding": "90px",
            }
        },
        html.h2("Digite seu login"),
        html.input(),
        html.h2("Digite sua senha"),
        html.input(),
        html.p(),
        button()
    )
    return componente

@component
def HelloWorld():
    pagina = html.div(
        {
            "style": {
                "align_items": "center",
                "text_align": "center",
                "margin": "auto",
                "width": "50%",
                "padding": "90px",
                "line-height": "0.6",
            }
        },
        html.h1("Bem vindo!"),
        html.p("Esse e o meu primeiro projeto"),
        Login(),
    )
    return pagina

@component
def loginSucess():
    pagina = html.div(
        {
                "style": {
                    "align_items": "center",
                    "text_align": "center",
                    "margin": "auto",
                    "width": "50%",
                    "padding": "90px",
                    "line-height": "0.6",
            },
        },
        html.h1("Parabens voce fez login !!"),
    )
    return pagina






@component
def button(on_click, display_text):
        return html.button({"on_click":lambda event: signin},"Sign")


@component
def signin(event):
        return redirect(loginIndex)
    