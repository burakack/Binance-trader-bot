import time

import Logger
from tabulate import tabulate
import Tradefuncs
from Tradefuncs import al,sat
from Indicators import MACD, RSI ,MA ,BOLLINGER
import Information
import os
from binance.client import Client
import Envmanager
from datetime import datetime

# pip install pandas
# pip install python-binance
Envmanager.takevars()
while True:
    Logger.printdate()
    Logger.printinfo()
    time.sleep(2)



