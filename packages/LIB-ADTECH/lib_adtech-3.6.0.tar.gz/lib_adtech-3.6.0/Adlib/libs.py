import os
import os.path

# Selenium
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

import os
import shutil
import datetime
from time import sleep
from Adlib.funcoes import *
from Adlib.logins import loginVirtaus
from Adlib.utils import meses
from Adlib.api import EnumBanco, EnumProcesso, putStatusRobo, EnumStatus

# Adlib
import Adlib
from Adlib.logins import *
from Adlib.funcoes import getCredenciais, esperarElemento, dataEscolha, clickCoordenada, mensagemTelegram, selectOption, putStatusRobo, aguardarDownload
from Adlib.integracao import integracaoVirtaus


# Explicitação de itens que serão exportados ao importar `libs`
__all__ = [
    "os", "sleep",
    "selenium", "webdriver", "Service", "WebDriverWait", "Keys", "ChromeDriverManager",
    "Adlib", "integracaoVirtaus", "EnumBanco", 'Chrome', 'esperarElemento', 'getCredenciais', 'dataEscolha', 'clickCoordenada', 
    'mensagemTelegram', 'selectOption', 'putStatusRobo', 'aguardarDownload', 'EnumStatus', 'EnumProcesso', 'shutil', 'datetime', 'meses', 'loginVirtaus']
