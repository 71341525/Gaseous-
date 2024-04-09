from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 19645327))
API_HASH = getenv("API_HASH", "92de937beb2f87db08df95bcca0ac2d6")

BOT_TOKEN = getenv("BOT_TOKEN", "6437907769:AAEgVIwRLzPPcoWZvTn8cFgkR1stTrMVJBM")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mohammadtaleb2012t:hamoda7@cluster0.xwc4uff.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 1260465030))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Tws_Tepthon")
