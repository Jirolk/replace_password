#!/bin/bash

log_file="log_busqueda.txt"
directory="/mnt/d/+-Documentos-CDS---/Factury/Python/"

# Buscar archivos .env en el directorio especificado
count=$(find "$directory" -iname "*.env" | wc -l)

if [ "$count" -gt 0 ]; then
  echo "Se encontraron $count archivos .env en el directorio: $directory" >> "$log_file"
else
  echo "No se encontraron archivos .env en el directorio: $directory" >> "$log_file"
fi
