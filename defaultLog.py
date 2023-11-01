import logging
from logging import DEBUG, StreamHandler, FileHandler, Formatter

fileh = FileHandler("Afk-Logs.txt","a") #for every project this needs to be changed.
streamh = StreamHandler()

file_format = Formatter('%(asctime)s ... %(levelname)s -- %(message)s -- %(filename)s', datefmt='%d/%m/%Y %H:%M')
stream_format = Formatter('[%(levelname)s] -- %(message)s')

fileh.setFormatter(file_format)
streamh.setFormatter(stream_format)

logging.basicConfig(encoding='UTF-8', datefmt = '%d/%m/%Y %H:%M',
                    handlers=[fileh, streamh], level=DEBUG
                    )

logging.debug("Default Logger by Atila: Imported and Started...")