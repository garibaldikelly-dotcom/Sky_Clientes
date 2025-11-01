# Navega al directorio del proyecto
cd /home/ec2-user/Sky_Clientes

# Ejecuta el script de Python. 
# Usamos 'exec' para que python3 tome el PID del script shell.
# Systemd se encarga de manejar los logs y la ejecución en segundo plano, 
# por lo que no necesitamos 'nohup' ni '&'.

# Si necesitas un entorno virtual (venv), descomenta y ajusta la siguiente línea:
# source /home/ec2-user/Microservicios_Clientes_AWS/venv/bin/activate 

exec python3 sky_app.py
