
# Pwned Password Checker

Este proyecto es una herramienta de línea de comandos que verifica si una contraseña ha sido comprometida en alguna violación de datos conocida. Utiliza la API de [Have I Been Pwned](https://haveibeenpwned.com/) y el método de **k-anonymity** para garantizar la privacidad de las contraseñas.

---

## Características

- Verifica si una contraseña ha sido encontrada en bases de datos comprometidas.
- Utiliza el método seguro de k-anonymity para proteger la contraseña completa.
- Proporciona el número de veces que una contraseña ha sido encontrada en violaciones de datos conocidas.
- Simple de usar desde la terminal.

---

## Instalación

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/agostinasvenson/checkMyPassword.git
   cd checkMyPassword
   ```

2. **Instala las dependencias necesarias:**
   Este proyecto requiere `requests`. Puedes instalarlo con:
   ```bash
   pip install requests
   ```

3. **Ejecuta el script:**
   ```bash
   python passwordchecker.py [contraseña1] [contraseña2] ...
   ```

---

## Uso

### Comando básico
Ejecuta el script seguido de las contraseñas que deseas verificar:
```bash
python passwordchecker.py 123456 password qwerty
```

### Resultado esperado
Para cada contraseña ingresada, el programa mostrará si ha sido comprometida y cuántas veces:
- **Ejemplo 1 (contraseña comprometida):**
  ```
  Tu contraseña 123456 fue encontrada 5000 veces, por favor cámbiala para estar a salvo!
  ```
- **Ejemplo 2 (contraseña segura):**
  ```
  Tu contraseña qwerty no fue encontrada, eso quiere decir que estás a salvo!
  ```

---

## Cómo funciona

1. **Hash de la contraseña:** La contraseña se convierte en un hash SHA-1.
2. **Consulta a la API:** Se envían los primeros 5 caracteres del hash a la API de Have I Been Pwned.
3. **Búsqueda de coincidencias:** El programa compara el resto del hash con las respuestas de la API para determinar si la contraseña ha sido comprometida.
4. **Privacidad garantizada:** Solo se comparten los primeros 5 caracteres del hash con la API, nunca la contraseña completa.

---

## Requisitos del sistema

- Python 3.6 o superior.
- Módulo `requests`.

---

## Advertencia

- Este proyecto es solo para fines educativos y no debe usarse para verificar contraseñas que no sean propias.
- Nunca almacenes ni compartas contraseñas en texto plano.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, por favor abre un **issue** o envía un **pull request**.

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE). Puedes usarlo, modificarlo y distribuirlo libremente siempre y cuando se incluya la licencia original.

---

## Autor

Creado por **[Agostina Svenson](https://github.com/agostinasvenson)**.

---

## Recursos

- [API Have I Been Pwned](https://haveibeenpwned.com/API/v3)
- [Documentación sobre k-anonymity](https://en.wikipedia.org/wiki/K-anonymity)

---

¡Listo para subir a GitHub! 🎉
