import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22780413"))
    API_HASH = os.environ.get("API_HASH", "45a244f065e9d889bb2cb9c80abcf0af)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6837252503:AAH8AXWm80lSdNG6CTV1KSgqf2ccnUHUflg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQFbmf0AnROihIWZlSwGFSD2Es-p0omUEpiwbFsA4Wpx7bbre0GSlfy4_j2wf94xKJJK3W_okWammbaVvvE1BSil7HM54o9YNvVYaRIMwI4bzWF4iR6bz080IN_Ib4utKdO1cH38A_MMHCPmnTSTXUhJts2hdToTwzYdtXxS6zjtb-6i9WA5OYiahLY7V_CtkDMd6nyXLhiIgyL5p7o8uySKn2yY6ktYzNjn5gG2FiLjlMmjZDSR7ZDDrzeZfIgr5iYt3JG7iWquKdfKzDYRRxZdKTUZ_3lRtjTOPEeXEo8x0pbO1TBnOxsz9fNvOZPPgGSKVY1ao_dPtVycGsejrnPMvSSYFgAAAAGStXFJAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "PallaviMusix_Bot")
    SUPPORT = os.environ.get("SUPPORT", "Heaven_vibezz") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Heaven_vibezz") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/9198a61a611fe557105eb.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/d6c5f269027327a7ae5b1.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6756331849")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
