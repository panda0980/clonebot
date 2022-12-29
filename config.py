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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCyFxgAIfecVy9WKjKG_6YuJ2e7ew5XhMDzyVDWS8o4qoYEhqgsQoMgbRtvycpDsHKTtoempjnDHOmex2sfr1YC730n0bK7sF0-pTGvmR3YjFQT-sVq1yYhLZWE-OPb1QVEG2sTlsKvyLyEbAPMV0pMoN5-dsF2Vnt-zKixaaIV_vinDKy1jUM4XnyOz-kz5lXaw7b0ei8SDm67-BM6bLjP66ASLG0U3KrilNipsNhKxs_vGLrAqkFCl0FAADMF7-Rdex7uC5Zp9M0sg0kxqOUtw1i2lJTT71epChlP4PMPh8n6QtZ-Fy0LQBRYNCz8ip_ejE7V5gvtHAp5GUI3A0J7EbFIqQAAAAB2OkRWAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://rraexkat:WoJSlT-mN0vR5OokJXmpr3omKR2kx4wY@berry.db.elephantsql.com/rraexkat")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
