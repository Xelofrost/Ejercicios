FROM ubuntu:latest

RUN apt-get update && apt-get install -y openssh-server sudo

RUN mkdir /var/run/sshd

RUN useradd -m -s  /bin/bash user1 && echo "user1:iloveyou" | chpasswd && usermod -aG sudo user1
RUN useradd  -m -s  /bin/bash user2 && echo "user2:ilovesummer" | chpasswd
RUN useradd  -m -s  /bin/bash JokerPersona && echo "JokerPersona:PhantomThieve18" | chpasswd
RUN useradd  -m -s  /bin/bash SaiyaMexicano && echo "SaiyaMexicano:KrillinFireworks" | chpasswd
RUN useradd  -m -s  /bin/bash Hackerman && echo "Hackerman:HackingTime" | chpasswd
RUN useradd  -m -s  /bin/bash KarateMaster && echo "KarateMaster:Torremonlimos" | chpasswd
RUN useradd  -m -s  /bin/bash Xanathar && echo "Xanathar:ilovemyfish" | chpasswd

# Permitir la autenticación por contraseña
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

#docker build -t sshlab .
#docker run -d -p 2222:22 sshlab