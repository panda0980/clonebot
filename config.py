#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5813212548:AAEu0LiCG-f2tW1mD6mdUWNYLpRLWqbTLLg")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "11671320 "))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "8e409e260f1d80f0ead65da912ee07bb")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBtDYfn0sUsI76Bhk6Ez-9Jx-Px-_TP50c4ZdXifWRdwVRcCXSvGSdXQ53X4aqdq0Wp5ptiSA-ql0waGMHDCQ_-NZmGvU4HkAGaMJvbg8FTgB6d9J3iBxFyeWmZ8t8CRe2jSyF7vvQ568FEGJ8cnoa8yreNhVJNxK_C8g3n1MHpt2jX0iwoPnwYByCl6o7zKIUyW3CFd0LP-o3h5tFrq3IDBgpnpUiVyfNdXSJ-q0jdeegbrEq-6ApotTWxS580NpbW1iq3fw21sBYrDvcFFxmhcx3uK5EIkvEJ4MLNoClQt9JSYtmgHNiKDBpIvSgwbIFX9dgBIBtSSbBxNb_e64X5djpEVgA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "sqlite:///sqlalchemy.sqlite")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
