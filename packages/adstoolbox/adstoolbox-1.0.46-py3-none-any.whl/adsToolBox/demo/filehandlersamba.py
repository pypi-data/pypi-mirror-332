from adsToolBox.logger import Logger
from adsToolBox.global_config import set_timer
from adsToolBox.file_handler import FileHandler
import os
import mimetypes

source_dir = r"C:\Users\mvann\Desktop\ADS\Projects\adsGenericFunctions\adsToolBox\demo\data"

files = ["clients_ads.xml", "data.D365_CustomersV3.csv", "dosia.gif", "FRA77570963700034_EXRM_R_20250204_07.zip", "haddad.png",
         "lorem-ipsum.pdf", "script.py", "special_characters_file.txt", "special_characters_file_clean.txt", "tank.jpg"]

logger = Logger(Logger.DEBUG, "AdsLogger")
set_timer(True)

smb_config = {
    "server": "192.168.10.106",
    "username": "ADS",
    "password": "9180"
}

file_handler = FileHandler(logger, smb_config)

source_dir = r"C:\Users\mvann\Desktop\ADS\Projects\adsGenericFunctions\adsToolBox\demo\data"
smb_path = r"\\192.168.10.106\samba\\"

for filename in os.listdir(source_dir):
    source_file = os.path.join(source_dir, filename)
    dest_file = os.path.join(smb_path, filename)
    if os.path.isfile(source_file):
        mime_type, _ = mimetypes.guess_type(source_file)
        is_text = mime_type and mime_type.startswith("text")
        try:
            if is_text:
                logger.warning(f"{filename} est un fichier texte")
                file, extension = filename.split('.')
                filename_clean = file + '_clean.' + extension
                file_content = file_handler.read_file(source_file, mode='rb')
                file_handler.write_file(os.path.join(smb_path, filename_clean), file_content, mode="wb", clean=True)
            file_content = file_handler.read_file(source_file, mode="rb")
            file_handler.write_file(dest_file, file_content, mode="wb", clean=False)
            logger.debug(f"Copie réussie: {filename}")
        except Exception as e:
            print(f"Erreur lors de la copie de {filename}")