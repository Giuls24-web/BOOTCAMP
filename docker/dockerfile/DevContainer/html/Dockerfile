#Usa una imagen base de Ubuntu
FROM mcr.microsoft.com/devcontainer/base:jammy

#Instala NGINX
RUN apt-get update && apt-get install -y nginx && apt-get clean

#Expone el puerto 80 para NGINX
EXPOSE 80

#Comando para iniciar NGINX en primer plano
CMD ["nginx", "-g", "daemon off;"]