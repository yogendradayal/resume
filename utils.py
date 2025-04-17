# utils.py

import logging
import os
from config import LOG_FILE

def setup_logging():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

def mask_email(email):
    return email[0] + "***" + email[email.find("@"):]
