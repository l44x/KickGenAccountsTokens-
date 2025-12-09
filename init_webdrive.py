from pathlib import Path
import undetected_chromedriver as uc
import sys

def init_webdriver_ec(headless=False, pos="maximizada", usar_devtools=True):
    options = uc.ChromeOptions()

    user_profile = Path(r"C:{YOUR_PATH}")  # OPTIONAL
    if not user_profile.exists():
        sys.exit(f"❌ Error: El perfil de Chrome no existe → {user_profile.resolve()}")

    options.add_argument(f"--user-data-dir={user_profile.resolve()}")

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--allow-outdated-plugins")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "intl.accept_languages": "es-ES,es"
        }
    )

    driver = uc.Chrome(
        options=options,
        headless=headless,
        log_level=3,
        enable_cdp_events=usar_devtools
    )

    if not headless:
        driver.maximize_window()
        if pos != "maximizada":
            ancho, alto = driver.get_window_size().values()
            if pos == "izquierda":
                driver.set_window_rect(x=0, y=0, width=ancho // 2, height=alto)
            elif pos == "derecha":
                driver.set_window_rect(x=ancho // 2, y=0, width=ancho // 2, height=alto)

    print("✅ Chrome iniciado usando perfil real con todas las extensiones cargadas.")
    return driver
