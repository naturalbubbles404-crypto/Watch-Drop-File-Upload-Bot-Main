import os

# Telegram API credentials
API_ID = int(os.environ.get("API_ID", "21404189"))
API_HASH = os.environ.get("API_HASH", "bd7028cc6f1bad77cd8e53023bf895b6")

# Bot token
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8262822749:AAFMahrFssdA31D3052hMXD1YJpBKVZSD-c")

# Workers
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Database channel
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002973651102"))

# Owner info
OWNER = os.environ.get("OWNER", "Magic_Mall_GameShop")   # Without @
OWNER_ID = int(os.environ.get("OWNER_ID", "1849257766"))

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Flame:HtunHlaAung-007047@watch-drop.cmn22zb.mongodb.net/?retryWrites=true&w=majority&appName=WATCH-DROP")
DB_NAME = os.environ.get("DB_NAME", "Zaws-File-Share")

# Support group link
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/MagicMallCustomerSupportBot")

# Optional branding images
START_PIC = os.environ.get("START_PIC", "")
FORCE_PIC = os.environ.get("FORCE_PIC", "")

# Custom caption footer
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "• ʙʏ @WatchDrop")

# File protect
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False").lower() == "true"

# Fsub expiry
FSUB_LINK_EXPIRY = int(os.environ.get("FSUB_LINK_EXPIRY", "10"))

# Text templates
START_MSG = """
👋 Welcome to **Watch Drop**!

I can store files in my database and share them with permanent links.  
Just send me any media and I’ll save it for you.

Use me in your groups too — I can auto-reply with files.

⚙️ Use /help to see available commands.
"""

HELP_MSG = """
📖 **Watch Drop Help**

• Send me any file — I’ll save it and give you a permanent shareable link.  
• Add me to your groups — I’ll respond to file requests automatically.

🔒 Admin commands (for bot owner):
/commands — show admin command list
/addchnl /delchnl /listchnl — manage force-sub channels
/ban /unban /banlist — manage bans
/broadcast — send message to all users

❓ Need help? Contact support: @MagicMallCustomerSupportBot
"""

ABOUT_MSG = f"""
**🤖 Bot:** Watch Drop FileStore  
**👨‍💻 Owner:** @{OWNER}  
**📢 Updates:** @watch_drop_movies_and_series  
**💬 Support:** @MagicMallCustomerSupportBot
"""
