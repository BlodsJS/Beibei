from io import BytesIO

import discord
from easy_pil import Canvas, Editor


def to_bytesio(image, filename: str) -> discord.File:
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return discord.File(buffer, filename=filename)


def error_image(width=500, height=140):
    bg = Canvas((width, height), color="#131515")
    editor = Editor(bg)

    editor.text((120, 60), "Erro ao gerar imagem", color="white")

    return to_bytesio(editor.image, "error.png")
