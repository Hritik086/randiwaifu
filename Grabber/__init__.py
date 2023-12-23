import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = 6379841493
sudo_users = ["6053689459", "5316914263"]
GROUP_ID = -1001999912328
TOKEN = "6811173408:AAG82qRQnhMLWbvpjf2ylRvhwoBce0p4OsE"
mongo_url = "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://telegra.ph/file/da13bb5af3dff2a227446.jpg", "https://telegra.ph/file/0adf1124349534495e422.jpg"]
SUPPORT_CHAT = "XTM_CHATS"
UPDATE_CHAT = "XTM_CHATS"
BOT_USERNAME = "XTM_waifus_bot"
CHARA_CHANNEL_ID = -1001980576874
api_id = 23961967
api_hash = "f8112d39264d893bb661b227316f092e"


application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']



