import os
import time
import inspect
from time import sleep
from functools import wraps
from typing import Callable
from Adlib.api import *
from Adlib.funcoes import *
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


token = "7505814396:AAHQvtr0ltePOLKp88awG7WHB6lksKkNaR0"
chatId = "-4095757991"

formatEnumName = lambda x: x.name.replace('_', ' ')


class LoginReturn(Enum):
    ACESSO_SIMULTANEO = "Acesso simultâneo"
    CAPTCHA_INCORRETO = "Captcha incorreto"
    LOGIN_COM_SUCESSO = "Login com sucesso"
    ERRO_AO_LOGAR = "Erro ao logar"
    RESETAR_SENHA = "Resetar senha"


def login_decorator(func):

    def loginFunctionPrototype(driver: Chrome, usuario: str, senha: str):
        pass


    def loginCaptchaFunctionPrototype(driver: Chrome, usuario: str, senha: str, enumProcesso: EnumProcesso) -> tuple[bool, str, str, EnumBanco]:
        pass


    loginFunctionModel = inspect.signature(loginFunctionPrototype)
    loginCaptchFunctionModel = inspect.signature(loginCaptchaFunctionPrototype)

    def validateLoginFunction(func: Callable) -> bool:
        funcSignature = inspect.signature(func)
        if funcSignature not in [loginFunctionModel, loginCaptchFunctionModel]:
            raise TypeError(
                f"A função {func.__name__} não está no formato adequado!\
                \n{loginFunctionModel}\
                \n{loginCaptchFunctionModel}"
            )
        return True

    @wraps(func)
    def wrapper(driver: Chrome, usuario: str, senha: str, *args):
        isValidLoginFunction = validateLoginFunction(func)
        if isValidLoginFunction:
            try:
                func(driver, usuario, senha, *args)
            except Exception as e:
                print(f"Erro ao realizar login: {func.__name__}")
                print(e)
            sleep(10)
    return wrapper


def captcha_decorator(loginFunc: Callable[[Chrome, str, str, EnumProcesso], tuple[LoginReturn, str, str, EnumBanco]]):
    @wraps(loginFunc)
    def wrapper(driver: Chrome, usuario: str, senha: str, enumProcesso: EnumProcesso) -> tuple[LoginReturn, str, str]:
        while True:
            loginReturn, imgPath, captcha, enumBanco = loginFunc(driver, usuario, senha, enumProcesso)
            
            if enumProcesso in [EnumProcesso.IMPORTACAO, EnumProcesso.APROVADORES]:
                global chatId
                chatId = "-1002257326271"
            
            if loginReturn == LoginReturn.LOGIN_COM_SUCESSO:
                timestamp = int(time.time())
                novo_nome = f"{timestamp}_{captcha}.png"
                novo_caminho = os.path.join(os.path.dirname(imgPath), novo_nome)
                
                os.rename(imgPath, novo_caminho)
                
                try:
                    storeCaptcha(novo_caminho, enumBanco, enumProcesso)
                except Exception as e:
                    os.remove(novo_caminho)
                    print(e)

                return loginReturn

            else:
                os.remove(imgPath)
                if loginReturn == LoginReturn.CAPTCHA_INCORRETO:
                    aguardarAlert(driver)
                    driver.refresh()
                    aguardarAlert(driver)

                else:
                    return loginReturn
        
    return wrapper


@login_decorator
def loginItau(driver: Chrome, usuario: str, senha: str):
    
    driver.get('https://portal.icconsig.com.br/')
    sleep(10)

    iframe = esperarElemento(driver, '/html/body/cc-lib-dialog/div/div[1]/div[2]/div/app-auth-dialog/div/iframe', tempo_espera=20)
    driver.switch_to.frame(iframe)

    esperarElemento(driver, '//*[@id="username"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="password"]').send_keys(senha + Keys.ENTER)
    
    sleep(10)

@login_decorator
def loginCrefisaCP(driver: Chrome, usuario: str, senha: str):

    driver.get("https://app1.gerencialcredito.com.br/CREFISA/default.asp")

    esperarElemento(driver, '//*[@id="txtUsuario"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="txtSenha"]').send_keys(senha)

    solveReCaptcha(driver)
    
    esperarElemento(driver, '//*[@id="btnLogin"]').click()

@login_decorator
def loginC6(driver: Chrome, usuario: str, senha: str):

    driver.get("https://c6.c6consig.com.br/WebAutorizador/Login/AC.UI.LOGIN.aspx")

    esperarElemento(driver, "//*[@id='EUsuario_CAMPO']").send_keys(usuario)
    esperarElemento(driver, "//*[@id='ESenha_CAMPO']").send_keys(senha)
    clickarElemento(driver, '//*[@id="lnkEntrar"]').click()
    
    aguardarAlert(driver)
    

@login_decorator
def loginDigio(driver: Chrome, usuario: str, senha: str):

    driver.get("https://funcaoconsig.digio.com.br/FIMENU/Login/AC.UI.LOGIN.aspx")

    esperarElemento(driver, "//*[@id='EUsuario_CAMPO']").send_keys(usuario)
    esperarElemento(driver, "//*[@id='ESenha_CAMPO']").send_keys(senha)
    clickarElemento(driver, '//*[@id="lnkEntrar"]').click()
    
    aguardarAlert(driver)


@login_decorator
def loginBlip(driver: Chrome, usuario: str, senha: str):

    driver.get('https://takegarage-7ah6a.desk.blip.ai/')
    sleep(5)
    shadowPrincipal = driver.find_element('css selector', 'body > bds-theme-provider > bds-grid > bds-grid.form_space.host.direction--undefined.justify_content--center.flex_wrap--undefined.align_items--center.xxs--12.xs--undefined.sm--undefined.md--6.lg--undefined.xg--undefined.gap--undefined.xxsoffset--undefined.xsoffset--undefined.smoffset--undefined.mdoffset--undefined.lgoffset--undefined.xgoffset--undefined.padding--undefined.margin--undefined.hydrated > bds-grid.login-content.host.direction--column.justify_content--undefined.flex_wrap--undefined.align_items--undefined.xxs--10.xs--6.sm--undefined.md--6.lg--undefined.xg--undefined.gap--2.xxsoffset--undefined.xsoffset--undefined.smoffset--undefined.mdoffset--1.lgoffset--undefined.xgoffset--undefined.padding--undefined.margin--undefined.hydrated > bds-grid.host.direction--column.justify_content--undefined.flex_wrap--undefined.align_items--undefined.xxs--undefined.xs--undefined.sm--undefined.md--undefined.lg--undefined.xg--undefined.gap--2.xxsoffset--undefined.xsoffset--undefined.smoffset--undefined.mdoffset--undefined.lgoffset--undefined.xgoffset--undefined.padding--undefined.margin--undefined.hydrated')
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadowPrincipal)

    shadow_host = driver.find_element('css selector', '#email-input')
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    shadow_root.find_element('class name', 'input__container__text').send_keys(usuario)

    # Shadow host Senha
    shadow_host = driver.find_element('css selector', '#password-input')
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
    shadow_root.find_element('css selector', 'div > div.input__container > div > input').send_keys(senha + Keys.ENTER + Keys.ENTER)
    sleep(5)


@login_decorator
def loginFacta(driver: Chrome, usuario: str, senha: str):

    driver.get('https://desenv.facta.com.br/sistemaNovo/login.php')
    
    esperarElemento(driver, '//*[@id="login"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="senha"]').send_keys(senha)

    esperarElemento(driver,'//*[@id="btnLogin"]').click()

    sleep(5)


@login_decorator
def loginMargem(driver: Chrome, usuario: str, senha: str):
    driver.get('https://adpromotora.promobank.com.br/') 

    esperarElemento(driver, '//*[@id="inputUsuario"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="passField"]').send_keys(senha + Keys.ENTER)

def loginBanrisul(driver: Chrome, usuario: str, senha: str, email: str):
    driver.get('https://bemweb.bempromotora.com.br/autenticacao/login')

    esperarElemento(driver, '/html/body/main/div/div/div[2]/div[2]/form/div[1]/div[2]/div/span/input').send_keys(usuario)
    esperarElemento(driver, '/html/body/main/div/div/div[2]/div[2]/form/div[2]/button').click()
    time.sleep(5)

    esperarElemento(driver, '//*[@id="senha"]').send_keys(senha)
    esperarElemento(driver, '//*[@id="btn-login"]').click()
    
    try:
        time.sleep(10)
        pop_up = esperarElemento(driver, '/html/body/section[2]/div/button').click()

        time.sleep(4)         
        print('Pop up fechado')
    except:
        while True:
            pin = coletarEmailEspecifico(email)
            try:
                inputPIN = esperarElemento(driver, '//*[@id="pin"]').send_keys(pin + Keys.ENTER)
                time.sleep(10)
                pop_up = esperarElemento(driver, '/html/body/section[2]/div/button').click()
                time.sleep(4)
                break
            except:
                inputPIN = esperarElemento(driver, '//*[@id="pin"]').clear()
                print('Tente logar novamente')


@login_decorator
def loginCashCard(driver: Chrome, usuario: str, senha: str):
    
    driver.get(f"https://front.meucashcard.com.br/WebAppBPOCartao/Login/ICLogin?ReturnUrl=%2FWebAppBPOCartao%2FPages%2FProposta%2FICPropostaCartao")
     
    esperarElemento(driver, '//*[@id="txtUsuario_CAMPO"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="txtSenha_CAMPO"]').send_keys(senha)

    esperarElemento(driver, '//*[@id="bbConfirmar"]').click()


@login_decorator
def loginVirtaus(driver: Chrome, usuario: str, senha: str):
    driver.get("https://app.fluigidentity.com/ui/login")
    sleep(5)

    esperarElemento(driver, '//*[@id="username"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="password"]').send_keys(senha + Keys.ENTER)


@login_decorator
def loginPaulista(driver: Chrome, usuario: str, senha: str):
    driver.get("https://creditmanager.bancopaulista.com.br/Login.aspx?ReturnUrl=%2fConcessao%2fMonitor.aspx")
    
    esperarElemento(driver, '//*[@id="MainContent_txtUsuario"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="MainContent_txtSenha"]').send_keys(senha)
    loginButton = esperarElemento(driver, '//*[@id="MainContent_Button1"]')
    
    loginButton.click()


@login_decorator
def loginSafra(driver: Chrome, usuario: str, senha: str):
    driver.get("https://epfweb.safra.com.br/")
    
    esperarElemento(driver, '//*[@id="txtUsuario"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="txtSenha"]').send_keys(senha + Keys.ENTER)
    sleep(35)
    try:
        buttonLogin = esperarElemento(driver, '//*[@id="btnEntrar"]')
        buttonLogin.click()
    finally:
        sleep(5)

    
@login_decorator
def loginMaster(driver: Chrome, usuario: str, senha: str):
    
    driver.get('https://autenticacao.bancomaster.com.br/login')

    esperarElemento(driver, '//*[@id="mat-input-0"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="mat-input-1"]').send_keys(senha)
    clickarElemento(driver, '/html/body/app-root/app-login/div/div[2]/mat-card/mat-card-content/form/div[3]/button[2]').click()
    try:
        clickarElemento(driver, '//*[@id="mat-dialog-0"]/app-confirmacao-dialog/div/div[3]/div/app-botao-icon-v2[2]/button').click()
    except:
        pass



@login_decorator
@captcha_decorator
def loginIBConsig(driver: Chrome, usuario: str, senha: str, enumProcesso: EnumProcesso) -> tuple[bool, str, str, EnumBanco]:
    
    enumBanco = EnumBanco.ITAU

    def checkLogin() -> bool:
        return driver.current_url == "https://www.ibconsigweb.com.br/principal/fsconsignataria.jsp" # URL após login bem sucedido
    
    driver.get("https://www.ibconsigweb.com.br/")

    esperarElemento(driver, '/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr/td/form/table/tbody/tr[1]/td[3]/input').send_keys(usuario)
    esperarElemento(driver, '/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/font/strong/input').send_keys(senha)
                                     
    captchaElement = esperarElemento(driver, '/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr/td/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td/iframe')

    imgPath = saveCaptchaImage(captchaElement, enumBanco, enumProcesso)

    captcha = enviarCaptcha(imgPath, enumBanco, enumProcesso)

    try:
        esperarElemento(driver, '/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr/td/form/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/input').send_keys(captcha)

        esperarElemento(driver, '/html/body/table/tbody/tr[2]/td[3]/table/tbody/tr/td/form/table/tbody/tr[4]/td/table/tbody/tr[1]/td[3]/a').click()
        sleep(10)
    except Exception as e:
        print(e)
        
    if loginReturn:=checkLogin():
        mensagemTelegram(token, chatId, f"Entrou! {formatEnumName(enumBanco)} {formatEnumName(enumProcesso)} ✅")

    return loginReturn, imgPath, captcha, enumBanco


@login_decorator
@captcha_decorator
def loginBMG(driver: Chrome, usuario: str, senha: str, enumProcesso: EnumProcesso) -> tuple[bool, str, str, EnumBanco]:
    
    def fecharAbasPopUp():
        substring = "bmgconsig"
        originalTab = driver.current_window_handle

        popups = [handle for handle in driver.window_handles if handle != originalTab]

        for handle in popups:
            driver.switch_to.window(handle)
            if substring in driver.current_url:
                driver.close()

        driver.switch_to.window(originalTab)

    def checkLoginBMG() -> LoginReturn:
        
        if aguardarAlert(driver):
            return LoginReturn.RESETAR_SENHA

        if esperarElemento(driver, '//*[@id="div-error"]/span[contains(text(), "tentativa de acesso simultâneo")]'):
            return LoginReturn.ACESSO_SIMULTANEO
    
        if esperarElemento(driver, '//*[@id="div-error"]/span[contains(text(), "A palavra de verificação está inválida.")]'):
            return LoginReturn.CAPTCHA_INCORRETO
        
        if driver.current_url == "https://www.bmgconsig.com.br/principal/fsconsignataria.jsp":
            return LoginReturn.LOGIN_COM_SUCESSO
        
        return LoginReturn.ERRO_AO_LOGAR
    enumBanco = EnumBanco.BMG
    
    driver.get("https://www.bmgconsig.com.br/Index.do?method=prepare")

    esperarElemento(driver,'//*[@id="usuario"]').send_keys(usuario + Keys.ENTER)
    esperarElemento(driver, '//*[@id="j_password"]').send_keys(senha + Keys.ENTER)

    captchaElement = esperarElemento(driver, '/html/body/section[1]/div/div[1]/div/div/form/div[3]/iframe')

    imgPath = saveCaptchaImage(captchaElement, enumBanco, enumProcesso)

    captcha = enviarCaptcha(imgPath, enumBanco, enumProcesso)
    try:
        esperarElemento(driver, '//*[@id="captcha"]').send_keys(captcha)

        esperarElemento(driver, '//*[@id="bt-login"]').click()
        sleep(10)
    except Exception as e:
        print(e)

    loginReturn = checkLoginBMG()

    if loginReturn == LoginReturn.LOGIN_COM_SUCESSO:
        fecharAbasPopUp()
        mensagemTelegram(token, chatId, f"Entrou! {formatEnumName(enumBanco)} {formatEnumName(enumProcesso)} ✅")

    return loginReturn, imgPath, captcha, enumBanco


@login_decorator
@captcha_decorator
def loginDaycoval(driver: Chrome, usuario: str, senha: str, enumProcesso: EnumProcesso) -> tuple[bool, str, str, EnumBanco]:

    enumBanco = EnumBanco.DAYCOVAL

    def checkLogin():
        return driver.current_url == "https://consignado.daycoval.com.br/Autorizador/" # URL após login bem sucedido
    
    aguardarAlert(driver)

    driver.get('https://consignado.daycoval.com.br/Autorizador/Login/AC.UI.LOGIN.aspx')
    sleep(5)
    
    esperarElemento(driver, '//*[@id="Captcha_lkReGera"]').click()
    sleep(1)
    esperarElemento(driver, '//*[@id="EUsuario_CAMPO"]').send_keys(usuario)
    esperarElemento(driver, '//*[@id="ESenha_CAMPO"]').send_keys(senha)
    
    captchaElement = driver.find_element('xpath', '//*[@id="form1"]/img')#captchaElement = esperarElemento(driver, '//*[@id="form1"]/img')

    imgPath = saveCaptchaImage(captchaElement, enumBanco, enumProcesso)

    captcha = enviarCaptcha(imgPath, enumBanco, enumProcesso)
    
    esperarElemento(driver, '//*[@id="Captcha_txtCaptcha_CAMPO"]').send_keys(captcha)

    esperarElemento(driver, '//*[@id="lnkEntrar"]').click()
    sleep(10)
    aguardarAlert(driver)
    
    if loginReturn:=checkLogin():
        mensagemTelegram(token, chatId, f"Entrou! {formatEnumName(enumBanco)} {formatEnumName(enumProcesso)} ✅")

    return loginReturn, imgPath, captcha, enumBanco


def logoutBMG(bmg: Chrome):
    
    bmg.get("https://www.bmgconsig.com.br/login/logout.jsp")
    try:
        esperarElemento(bmg, '//*[@id="buttonLink"]').click()
        time.sleep(3)
        aguardarAlert(bmg)
    except:
        pass
    time.sleep(5)


if __name__=="__main__":

    driver = setupDriver(r"C:\Users\dannilo.costa\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe")
    #loginBanco, senhaBanco = 
    user, senha = getCredenciais(159)
    
    #loginDaycoval(driver, user, senha, EnumProcesso.IMPORTACAO)
    loginBMG(driver, user, senha, EnumProcesso.INTEGRACAO)

    input("FECHAR????")
    input("FECHAR????")
    input("FECHAR????")
    input("FECHAR????")
    input("FECHAR????")