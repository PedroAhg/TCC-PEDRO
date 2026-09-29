import customtkinter as ctk

FILEIRAS = 10
COLUNAS = 20

app = ctk.CTk()
app.title("Gerenciamento de Cinema")
app.geometry("600X450")

filme = ctk.CTkLabel(app, text="Filme: Regular Show: The Movie")
filme.pack(pady=(20, 5))


tela = ctk.CTkLabel(
    app,
    text="T E L A",
    fg_color="#FFFFFF",

)
tela.pack(fill="x", padx=60, pady=20)

frame_assentos = ctk.CTkFrame(app, fg_color="transparent")

frame_assentos.pack()

for x in range(FILEIRAS):
    letra = chr(65 + x)

    for y in range(1, COLUNAS + 1):
        codigo = f"{letra}{y}"

        btn = ctk.CTkButton(
        frame_assentos,
        text=codigo,
        width=45,
        height=40,
        fg_color="#0A7400",
        hover_color="#FF0000"
    )
        btn.grid(row=x, column=y - 1, padx=4, pady=4,)

app.mainloop()
