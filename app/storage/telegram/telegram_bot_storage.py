from app.core.config import CID, TOKEN
from app.storage import Storage
from app.storage.telegram.bot import bot
import io


class TelegramBotStorage(Storage):
    async def put_file(self, file: bytes, filename: str) -> str:
        result = await bot.send_document(CID, file, filename=filename)
        return str(result.document.file_id)

    async def get_file(self, file_id: str):
        file = await bot.get_file(file_id)
        file_bytes = await file.download_as_bytearray()
        return io.BytesIO(file_bytes)
