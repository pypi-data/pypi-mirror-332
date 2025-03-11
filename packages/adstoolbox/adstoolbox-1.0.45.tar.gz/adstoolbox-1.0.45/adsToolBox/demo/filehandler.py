from adsToolBox.logger import Logger
from adsToolBox.global_config import set_timer
from adsToolBox.file_handler import FileHandler
import os
import mimetypes

source_dir = r"C:\Users\mvann\Desktop\ADS\Projects\adsGenericFunctions\adsToolBox\demo\data"
dest_dir = r"C:\Users\mvann\Desktop\ADS\Projects\adsGenericFunctions\adsToolBox\demo\data\copies"

files = ["clients_ads.xml", "data.D365_CustomersV3.csv", "dosia.gif", "FRA77570963700034_EXRM_R_20250204_07.zip", "haddad.png",
         "lorem-ipsum.pdf", "script.py", "special_characters_file.txt", "special_characters_file_clean.txt", "tank.jpg"]

os.makedirs(dest_dir, exist_ok=True)

logger = Logger(Logger.DEBUG, "AdsLogger")
set_timer(True)
file_handler = FileHandler(logger)

special_characters_text = """
Voici quelques caractères spéciaux supplémentaires :
- Accents : é, è, ê, ë, à, â, ä, î, ï, ô, ö, ù, ü, ñ, ç, œ
- Caractères non-latins : привет, 你好, こんにちは, здравствуйте, مرحبا
- Symboles : @, €, #, &, %, ©, ™, →, ±, ∆, ∑, ∞, ≠, √, ∫, ≈, £, ¥
- Emojis : 😊, 😂, 🥺, ❤️, 👍, 👑, 🌍, 🍕, 🏀
- Caractères arabes : العربية, ١٢٣٤٥, أ
- Caractères cyrilliques : А, Б, В, Г, Д, Ж, З, И, Й, К
- Divers : ¿, ¡, ©, ®, ‰, ∅, ¶, ′, ″, ⅛, ⅓, ⅔, ⅘, ≡, ⊗
"""

file_path = r"C:\Users\mvann\Desktop\ADS\Projects\adsGenericFunctions\adsToolBox\demo\data\special_characters_file.txt"

file_handler.write_file(file_path, special_characters_text, "w", False)

file_path = file_path[:-4] + "_clean.txt"
file_handler.write_file(file_path, special_characters_text, "wb", True)

for filename in files:
    source_file = os.path.join(source_dir, filename)
    dest_file = os.path.join(dest_dir, filename)
    if os.path.isfile(source_file):
        mime_type, _ = mimetypes.guess_type(source_file)
        is_text = mime_type and mime_type.startswith("text")
        try:
            if is_text:
                file, extension = filename.split('.')
                filename_clean = file + '_clean.' + extension
                file_content = file_handler.read_file(source_file, mode="rb")
                file_handler.write_file(os.path.join(dest_dir, filename_clean), file_content, mode="wb", clean=True)
            file_content = file_handler.read_file(source_file, mode="rb")
            file_handler.write_file(dest_file, file_content, mode="wb", clean=False)
            logger.debug(f"Copie réussie: {filename}")
        except Exception as e:
            print(f"Erreur lors de la copie de {filename}")