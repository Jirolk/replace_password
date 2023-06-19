import os
import glob
import logging
from datetime import datetime

'''Script para reemplazar la contraseña vieja del mailjet
autor: Sandro Castillo 
Versión= 1.2'''

def replace_password(root_dir, new_password):
    logging.basicConfig(filename='log_replace_pass.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger()
    logger.info("__Inicio del Cambio__")

    root_dir = os.path.abspath(os.path.expanduser(root_dir))
    print(f"Buscando en el directorio raíz: {root_dir}...")
    env_files = glob.glob(os.path.join(root_dir, '**', '.env'), recursive=True)

    if env_files:
        print("###" * 10)
        print("Archivos .env encontrados:")

        count=0 # Para registrar la cantidad de los archivos .env 

        for env_file in env_files:
            env_file_path = os.path.join(root_dir, env_file)
            print("Ruta: ", os.path.abspath(env_file_path))
            logger.info(f"Ruta: {os.path.abspath(env_file_path)}")

            with open(env_file_path, 'r') as file:
                lines = file.readlines()

            modified = False  # Variable para indicar si se realizó alguna modificación en el archivo
            mailjet = False

            for i in range(len(lines)):
                if lines[i].startswith('EMAIL_HOST='):
                    mailHost = lines[i].strip().split('=')[1]
                    print("valor Email_host: ",mailHost)
                    if mailHost == 'in-v3.mailjet.com':
                        mailjet = True
                    else:
                        print("No se Realizó cambios- posee otro HOST ")
                        log_message=f'PARA EL EMAIL_HOST : {mailHost}, NO APLICA , no se realizaron cambios\n'
                        logger.info(log_message)
                        break                                       
                        
            if mailjet:
                for x in range(len(lines)):
                    if lines[x].startswith('EMAIL_HOST_PASSWORD='):
                        previous_value = lines[x].strip().split('=')[1]  # Obtener el valor anterior
                        lines[x] = f'EMAIL_HOST_PASSWORD={new_password}\n'
                        modified = True
                        break
        
            if modified:
                if previous_value == new_password:
                    print("No se Realizó cambios")
                    logger.info("No se Realizarón cambios.\n")
                else:
                    with open(env_file_path, 'w') as file:
                        file.writelines(lines)
                    print(f"Se ha reemplazado el valor de EMAIL_HOST_PASSWORD en el archivo {env_file}.")
                    # Guardar en el log el valor anterior, la ruta y la hora

                    log_message = f"Se ha reemplazado el valor de EMAIL_HOST_PASSWORD en el archivo {env_file}.\n Valor anterior: {previous_value}, Nuevo valor: {new_password}\n"
                    logger.info(log_message)
            else:
                print("No se encontró la variable EMAIL_HOST_PASSWORD en el archivo.")
                logger.info("No se encontró la variable EMAIL_HOST_PASSWORD en el archivo.")

            count+=1

    else:
        print("###" * 10)
        print("Archivos .env NO encontrados:")
        print("###" * 10)
        
        logger.info("####### Archivos .env NO encontrados ###" )
        
    msj =f'===Total de archivos: {count} ========================\n'
    logger.info(msj)


#root_directory = "/mnt/d/+-Documentos-CDS---/Factury/Python/" #para linux
root_directory = "D:\+-Documentos-CDS---\Factury\Python\envdeprueba" #para windows
new_password = "96f23c14c3063ea0876afc1e8e1c2f39"

replace_password(root_directory, new_password)
