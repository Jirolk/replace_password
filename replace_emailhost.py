import os
import glob
import logging
from datetime import datetime

'''Script para reemplazar la contraseña vieja del mailjet
autor: Sandro Castillo 
Versión= 1.2'''

def replace_password(root_dir, new_password):
    logging.basicConfig(filename='log_replace_email_host.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger()
    logger.info("__Inicio del Cambio__")


    root_dir = os.path.abspath(os.path.expanduser(root_dir))
    print(f"Buscando en el directorio raíz: {root_dir}...")
    env_files = glob.glob(os.path.join(root_dir, '**', '.env'), recursive=True)

    if env_files:
        print("###" * 10)
        print("Archivos .env encontrados:")

        count=0 # conteo de la cantidad de archivos .env
        modi =0 # conteo de archivos modificados. 

        for env_file in env_files:
            env_file_path = os.path.join(root_dir, env_file)
            print("Ruta: ", os.path.abspath(env_file_path))
            logger.info(f"Ruta: {os.path.abspath(env_file_path)}")

            with open(env_file_path, 'r') as file:
                lines = file.readlines()

            modified = False  # Variable para indicar si se realizó alguna modificación en el archivo
            mailjet = False
            vali=0

            for i in range(len(lines)):
                if lines[i].startswith('EMAIL_HOST='):
                    mailHost = lines[i].strip().split('=')[1]
                    print("valor Email_host: ",mailHost)
                    if mailHost != email_host:
                        mailjet = True
                        break
                    # else:
                    #     print("No se Realizó cambios ")
                    #     log_message=f'Ya posee la configuración correcta.\n'
                    #     logger.info(log_message)
                    #     break      
            
            if mailjet:
                for i in range(len(lines)):

                    if lines[i].startswith('EMAIL_HOST='):
                        mailHost = lines[i].strip().split('=')[1]
                        print("valor Email_host: ",mailHost)
                        lines[i] = f'EMAIL_HOST={email_host}\n'
                        vali+=1
                        
                    if lines[i].startswith('EMAIL_HOST_USER='):                   
                        lines[i] = f'EMAIL_HOST_USER={user_token}\n'           
                        vali+=1        

                    if lines[i].startswith('EMAIL_HOST_PASSWORD='):
                        #previous_value = lines[i].strip().split('=')[1]  # Obtener el valor anterior
                        lines[i] = f'EMAIL_HOST_PASSWORD={new_password}\n'
                        vali+=1

                    if vali==3:
                        modified=True

                
            if modified:               
                with open(env_file_path, 'w') as file:
                    file.writelines(lines)
                
                modi+=1

                print(f"Se ha reemplazado los valores nuevos en el archivo {env_file}.")
                # Guardar en el log el valor anterior, la ruta y la hora

                log_message = f"Se ha reemplazado los valores nuevos en el archivo {env_file}.\n"
                logger.info(log_message)
            else:
                if not mailjet:
                    print("Ya posee la configuración correcta.")
                    logger.info("Ya posee la configuración corecta.")
                else:

                    print("No se encontró la variable EMAIL_HOST en el archivo.")
                    logger.info("No se encontró la variable EMAIL_HOST en el archivo.")

            count+=1

    else:
        print("###" * 10)
        print("Archivos .env NO encontrados:")
        print("###" * 10)
        
        logger.info("####### Archivos .env NO encontrados ###" )
        
    msj =f'===Total de archivos: {count} ====== MODIFICADOS: {modi}==================\n'
    logger.info(msj)


#root_directory = "/mnt/d/+-Documentos-CDS---/Factury/Python/" #para linux
root_directory = "D:\+-Documentos-CDS---\Factury\Python\envdeprueba" #para windows

email_host = 'in-v3.mailjet.com'
new_password = "96f23c14c3063ea0876afc1e8e1c2f39"
user_token = '77576d1b9066c3f8b936b6f8a8c64e79'

replace_password(root_directory, new_password)
