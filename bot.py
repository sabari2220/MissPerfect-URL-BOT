#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
from config import Config
from pyrogram import Client as LazyDeveloper
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = LazyDeveloper("@Sabari023",
    bot_token=Config."5753542938:AAFQ_23zAEwxGTPRAEMCItqm1Vz6BjEfjXU",
    api_id=Config."29161994",
    api_hash=Config."6de0c3c108577f72d5a50097108e9486",
    plugins=plugins)
    Warrior.run()
