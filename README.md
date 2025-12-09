# KickGenAccountsTokens 2025 - DICIEMBRE (2026)

Automatización completa para crear cuentas nuevas en **Kick.com** utilizando:

- undetected-chromedriver (WebDriver indetectable)
- Selenium
- EZTempMail (correo temporal)
- AutoHotkey (AHK)
- Sistema automático de OTP, cookies, sesión y usernames secuenciales

**Nota importante:**  
Este bot solo funciona correctamente en pantallas con resolución **1920x1080**, ya que los scripts AutoHotkey dependen de posiciones fijas en pantalla.

---

## Características

- Uso de `undetected-chromedriver` para evitar detección.
- Obtención automática de correos temporales desde EZTempMail.
- Lectura automática del correo de Kick.
- Extracción automática del código OTP (6 dígitos).
- Llenado del formulario de registro mediante `ss3.ahk`.
- Aceptación automática de términos con `register.ahk`.
- Guardado de:
  - session_token
  - cookies en formato JSON
  - email y username utilizados
- Generación automática de usernames secuenciales.
- Manejo de errores con reinicios automáticos.

## Requisitos

### Python
- Python 3.8 o superior  
- Instalar dependencias:

```bash
pip install selenium undetected-chromedriver
```

## ⚠️ Advertencia Legal

Este proyecto es únicamente para fines educativos.  
El uso de automatizaciones para crear cuentas o interactuar con plataformas como **Kick.com** puede violar sus Términos de Servicio.  
El autor no se hace responsable del uso indebido, abusivo o ilegal de este software.  
Usa esta herramienta bajo tu propio riesgo.


## Autor
**Desarrollado por:**  
Discord: **0encrypt3d**
