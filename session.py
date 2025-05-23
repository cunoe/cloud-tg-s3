from pyrogram import Client
import asyncio

from app.core.config import TELEGRAM_API_HASH, TELEGRAM_API_ID

async def stringGenerate():
    api_id = TELEGRAM_API_ID
    api_hash = TELEGRAM_API_HASH
    client = Client("memory", api_id, api_hash)
    await client.connect()
    
    phone_number = input("Insert your phone number: \nIncluding Country code. Example: +5357653423 \n")
    print("Sending code to telegram... \n")
    code = await client.send_code(phone_number)
    
    phone_code_msg = input("Insert registration code: \n")
    
    try:
        print('Login in Telegram...')
        await client.sign_in(phone_number, code.phone_code_hash, phone_code_msg)
    except:
        password = input('Insert your double factor:\n')
        await client.check_password(password=password)
    print("Session String: ")
    string_session = await client.export_session_string()
    
    
    print(f"Session String:\n{string_session}")
    
    
if __name__ == "__main__":
    asyncio.run(stringGenerate())