# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# Editado por fnixdev

from kannax import Message, kannax


@kannax.on_cmd(
    "id",
    about={
        "header": "Mostra os ids",
        "usage": "Responda {tr}id a uma mensagem, arquivo ou apenas envie esse comando",
    },
)
async def getids(message: Message):
    msg = message.reply_to_message or message
    out_str = f"๐ฅ **ID do chat** : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f"๐ฌ **ID da mensagem** : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f"๐โโ๏ธ **ID do usuรกrio** : `{msg.from_user.id}`\n"
    file_id = None
    if msg.audio:
        type_ = "audio"
        file_id = msg.audio.file_id
    elif msg.animation:
        type_ = "animation"
        file_id = msg.animation.file_id
    elif msg.document:
        type_ = "document"
        file_id = msg.document.file_id
    elif msg.photo:
        type_ = "photo"
        file_id = msg.photo.file_id
    elif msg.sticker:
        type_ = "sticker"
        file_id = msg.sticker.file_id
    elif msg.voice:
        type_ = "voice"
        file_id = msg.voice.file_id
    elif msg.video_note:
        type_ = "video_note"
        file_id = msg.video_note.file_id
    elif msg.video:
        type_ = "video"
        file_id = msg.video.file_id
    if file_id is not None:
        out_str += f"๐ **ID do arquivo** (`{type_}`): `{file_id}`"
    await message.edit(out_str)
