FROM ubuntu:xenial

RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-php

RUN echo "<?php phpinfo(); ?>" > /var/www/html/index.php

EXPOSE 80
#ENTRYPOINT ["apache2ctl"]
CMD ["apache2ctl", "-D", "FOREGROUND"]