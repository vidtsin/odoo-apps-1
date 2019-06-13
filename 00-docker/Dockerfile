FROM odoo:8.0
MAINTAINER Abdou Nasser <abdounasser202@gmail.com>
USER root
RUN set -x; \
        apt-get update \
        && apt-get install -y python-pip libcups2 libcups2-dev ghostscript python-dev \
        && pip install pycups
USER odoo
COPY ./modules /mnt/extra-addons/
