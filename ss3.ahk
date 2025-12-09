#SingleInstance Force
SetKeyDelay, 50, 50
SetWorkingDir, %A_ScriptDir%

FileRead, jsonContent, registro_data.json
if (jsonContent = "")
{
    ExitApp  ; 
}

; Extraer email
RegExMatch(jsonContent, """email""\s*:\s*""([^""]+)""", emailMatch)
email := emailMatch1

; Extraer username
RegExMatch(jsonContent, """username""\s*:\s*""([^""]+)""", userMatch)
username := userMatch1

password := "$Super_B5Botijas003"
birth_year := "1998"

; --- Comienza el llenado automático ---

; 1. Click en la barra de URL
MouseClick, left, 290, 17
Sleep, 500

; 2. Click en la caja de texto de URL
MouseClick, left, 433, 62
Sleep, 500
Send, https://kick.com/kick
Sleep, 300
Send, {Enter}
Sleep, 3000

; 3. Click en "Iniciar sesión"
MouseClick, left, 1695, 117
Sleep, 3000

; 4. Click en "Register"
MouseClick, left, 920, 420
Sleep, 3000

; 5. Email
MouseClick, left, 947, 393
Sleep, 500
Send, ^a
Sleep, 100
Send, {Del}
slowType(email)
Sleep, 600

; 6. Año de nacimiento
MouseClick, left, 906, 479
Sleep, 500
Send, ^a
Sleep, 100
Send, {Del}
slowType(birth_year)
Sleep, 600

; 7. Nombre de usuario
MouseClick, left, 935, 569
Sleep, 500
Send, ^a
Sleep, 100
Send, {Del}
slowType(username)
Sleep, 600

; 8. Contraseña
MouseClick, left, 928, 657
Sleep, 500
Send, ^a
Sleep, 100
Send, {Del}
slowType(password)
Sleep, 600

; 9. Click en "Regístrate"
MouseClick, left, 947, 763
Sleep, 3000

ExitApp

slowType(text) {
    Loop, Parse, text
    {
        Send, %A_LoopField%
        Sleep, 60 + Random(0, 40)
    }
}

; Función random
Random(min, max) {
    Random, out, min, max
    return out
}
