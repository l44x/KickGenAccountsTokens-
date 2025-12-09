import os
import json
import time
import random
import re
import subprocess
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

from init_webdrive import init_webdriver_ec 

ruta_actual = os.path.dirname(os.path.abspath(__file__))

def obtener_email_temporal(driver):
    print("📬 Obteniendo correo temporal...")
    driver.get("https://www.eztempmail.com/")

    wait = WebDriverWait(driver, 25)

    email_input = wait.until(ec.presence_of_element_located((By.ID, "mainEmail")))

    def email_valido(_):
        val = email_input.get_attribute("value").strip()
        return (val and "@" in val and "landing" not in val.lower())

    wait.until(email_valido)


    email = email_input.get_attribute("value").strip()

    try:
        driver.execute_script("document.body.style.zoom='0.5'")
        print("🔎 Zoom ajustado al 50% en EZTempMail.")
    except:
        print("⚠️ No se pudo aplicar zoom (ignorado).")

    print(f"✅ Correo obtenido: {email}")

    tempmail_handle = driver.current_window_handle

    return email, tempmail_handle


def get_next_index(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return int(f.read().strip())
    return 1

def save_index(file_path, index):
    with open(file_path, 'w') as f:
        f.write(str(index))

def slow_type(element, text, delay_range=(0.07, 0.2)):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(*delay_range))

def run_bot():
    driver = init_webdriver_ec(headless=False, pos='maximizada', usar_devtools=True)
    wait = WebDriverWait(driver, 30)

    try:
        index_file = os.path.join(ruta_actual, "user_index.txt")
        user_index = get_next_index(index_file)

        email, tempmail_handle = obtener_email_temporal(driver)
        username = f"L44X_TESTED_GEN{str(user_index).zfill(3)}"

        with open("registro_data.json", "w", encoding="utf-8") as f:
            json.dump({"email": email, "username": username}, f, ensure_ascii=False)

        subprocess.run([
            "C:\\{YOUR_PATH}\\AutoHotkey.exe",
            os.path.join(ruta_actual, "ss3.ahk")
        ])

        print("🕒 Esperando que el script AHK llene el formulario... (40 segundos)")
        time.sleep(40)


        print("📩 Buscando código de verificación en tempmail...")

        try:
            driver.switch_to.window(tempmail_handle)
            print("🌐 Pestaña de EZTempMail localizada (handle directo).")

            # Zoom 50%
            driver.execute_script("document.body.style.zoom='0.5'")
            print("🔎 Zoom aplicado (50%)")

            # Scroll abajo
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("📜 Scroll hacia abajo realizado.")

        except Exception as e:
            raise Exception(f"❌ No se pudo acceder a la pestaña de correo temporal: {e}")

        wait.until(ec.visibility_of_element_located((
            By.XPATH, "//div[@id='mailbox']//a[@class='link link-primary']"
        )))

        # Obtener subject
        subject_element = driver.find_element(
            By.XPATH, "//div[@id='mailbox']//a[@class='link link-primary']"
        )
        subject = subject_element.text.strip()
        print(f"📧 Asunto del correo: {subject}")

        match = re.search(r"(\d{6})", subject)
        if not match:
            raise Exception("❌ No se encontró código OTP en el correo.")

        verification_code = match.group(1)
        print(f"✅ Código OTP: {verification_code}")

        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if "kick.com" in driver.current_url.lower():
                break

        otp_input = wait.until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-input-otp='true']")
        ))
        otp_input.clear()
        slow_type(otp_input, verification_code)
        print("🔐 Código OTP ingresado.")

        time.sleep(10)

        scroll_ahk = "register.ahk"
        ruta_scroll_ahk = os.path.join(ruta_actual, scroll_ahk)
        subprocess.Popen(["C:\{YOUR_PATH}\\AutoHotkey.exe", ruta_scroll_ahk])

        time.sleep(30)

        cookies = driver.get_cookies()
        session_token = None
        for cookie in cookies:
            if cookie['name'] == 'session_token':
                session_token = cookie['value']
                break

        if session_token:
            print(f"🔑 session_token: {session_token}")
            with open("session_token.txt", "a") as f:
                f.write(session_token + "\n")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta_guardado = os.path.join("CookiesSession", f"kick_{timestamp}.json")
        os.makedirs("CookiesSession", exist_ok=True)
        with open(ruta_guardado, "w", encoding="utf-8") as f:
            json.dump(cookies, f, ensure_ascii=False, indent=2)

        print(f"💾 Cookies guardadas en: {ruta_guardado}")

        user_index += 1
        save_index(index_file, user_index)

    except Exception as e:
        print(f"❌ Error: {e}")
        print("⏳ Esperando 10 minutos para reintentar...")
        time.sleep(600)

    finally:
        driver.quit()
        espera = random.randint(1, 5)
        print(f"🔁 Reiniciando en {espera} segundos...")
        time.sleep(espera)

if __name__ == "__main__":
    while True:
        try:
            run_bot()
        except Exception as e:
            print(f"💥 Error inesperado: {e}")
            time.sleep(600)
