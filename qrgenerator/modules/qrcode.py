"""
Module to manage QRcodes API calls and file saves.
"""

import os
import requests
import logging


class Qrcode:
    """
    Get and Save QR codes.
    """
    error_count = 0

    def __init__(self, id):
        """
        Initialize with id. Initialise Logging.
        """
        self.id = id
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_qr(self):
        """
        Get and save QR codes based on id.
        """

        # API URL
        url = f"""https://image-charts.com/chart?chs=150x150&cht=qr&chl=
        {self.id}=UTF-8"""

        # Ensure folder exists for qrcodes, if not - mkdir
        os.makedirs('qrcodes', exist_ok=True)

        # Attempt to get a response from API and save qrcode as .png.
        try:
            response = requests.get(url)
            response.raise_for_status()

            with open(f"qrcodes/qr_{self.id}.png", "wb") as file:
                file.write(response.content)

        except requests.RequestException as e:
            Qrcode.error_count += 1
            self.logger.error(f"Failed response: {e}", exc_info=True)

        except IOError as e:
            Qrcode.error_count += 1
            self.logger.error(f"Failed to write file: {e}", exc_info=True)

        except Exception as e:
            Qrcode.error_count += 1
            self.logger.error(f"An unexpected error occurred: {
                              e}", exc_info=True)

        if Qrcode.error_count >= 10:
            logging.error("Reached 10 errors. Stopping process.")
            return
