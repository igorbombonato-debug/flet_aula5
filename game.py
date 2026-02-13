import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha a opção correta!", color="#e02e16", size=35)
   
    resposta_correta = "Granada"
    page.bgcolor="#a5a852"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "PARABÉNS💣💣💥💥💥"
        else:
            mensagem.value = "Resposta errada👀👀"
            page.update()    
        # page.add(ft.Text(e.control.content))

    page.title = "Game: Adivinhe a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe a imagem",
                    size=24,
                    weight="bold"
                ),
                ft.Image(
                    src="images/silueta granada.webp",
                    height=200,
                    border_radius=100
                

                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="Granada",
                            on_click=verificar_resposta,
                             color="#d7de18",
                            bgcolor="#0a0a09"
                        ),
                        ft.Button(
                            content="Mina-Terrestre",
                            on_click=verificar_resposta,
                            color="#d7de18",
                            bgcolor="#0a0a09"
                        ),
                        ft.Button(
                            content="Canhão",
                            on_click=verificar_resposta,
                             color="#d7de18",
                            bgcolor="#0a0a09"
                        ),
                    ],
                    alignment = ft.MainAxisAlignment.CENTER
                ),
                mensagem
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)