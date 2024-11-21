import requests
import hashlib
import sys


#Conexion con la api: -------------------------------
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error: {res.status_code}, revisa la configuracion de api e intenta nuevamente.')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

#Lectura de respuesta: -------------------------------
#def read_res(response):
 #   print(response.text)

#Codificacion de la contraseña: en sha1 --- NUCLEO DEL PROGRAMA -------------------------------

def pwned_api_check(password):
    #Codificacion y convertit a mayusculas:
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #Guardar los primeros 5 digitos en first5_char y el resto en tail:
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Tu contraseña {password} fue encontrada {count} veces, por favor cámbiala para estar a salvo!')
        else:
            print(f'Tu contraseña {password} no fue encontrada, eso quiere decir que estás a salvo!')
    return 'Listo!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

