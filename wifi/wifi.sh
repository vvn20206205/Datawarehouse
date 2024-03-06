#!/bin/bash
echo "Tải offline"

echo "Tải mysql"
# docker pull mysql
# docker save -o wifi/image/mysql_image.tar mysql
docker load -i wifi/image/mysql_image.tar
echo "Xong mysql"

echo "Tải node"
# docker pull node
# docker save -o wifi/image/node_image.tar node
docker load -i wifi/image/node_image.tar
echo "Xong node"

echo "Tải nats"
# docker pull nats
# docker save -o wifi/image/nats_image.tar nats
docker load -i wifi/image/nats_image.tar
echo "Xong nats"

echo "Tải mailhog"
# docker pull  mailhog/mailhog
# docker save -o wifi/image/mailhog_image.tar mailhog/mailhog
docker load -i wifi/image/mailhog_image.tar
echo "Xong mailhog"

echo "Tải phpmyadmin"
# docker pull  phpmyadmin/phpmyadmin
# docker save -o wifi/image/phpmyadmin_image.tar phpmyadmin/phpmyadmin
docker load -i wifi/image/phpmyadmin_image.tar
echo "Xong phpmyadmin"

# echo "Tải postgres:alpine"
# docker pull postgres:alpine
# docker save -o wifi/image/postgres_image.tar postgres:alpine
# docker load -i wifi/image/postgres_image.tar
# echo "Xong postgres"

# echo "Tải pgadmin4"
# docker pull dpage/pgadmin4
# docker save -o wifi/image/pgadmin4_image.tar dpage/pgadmin4
# docker load -i wifi/image/pgadmin4_image.tar
# echo "Xong pgadmin4"

# echo "Tải latex"
# docker pull         blang/latex:latest
# docker save -o wifi/image/latex_image.tar  blang/latex:latest
# docker load -i wifi/image/latex_image.tar
# echo "Xong latex"

echo "Tải jenkins"
# docker pull jenkins/jenkins:lts
# docker save -o wifi/image/jenkins_image.tar jenkins/jenkins:lts
docker load -i wifi/image/jenkins_image.tar
echo "Xong jenkins"
