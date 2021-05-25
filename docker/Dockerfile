###############################################################################
# main
###############################################################################

FROM continuumio/miniconda3:4.8.3 AS main

RUN apt-get -y update && \
    apt-get -y install build-essential
RUN conda update -n base -c defaults conda

RUN conda install pip
# chown changes owner from root owner (1000) to the first user (100)
COPY --chown=1000:100 . /var/app
# install requirements and source
RUN pip install -r /var/app/requirements.txt
RUN pip install -e /var/app --no-deps
WORKDIR /var/dev

# ###############################################################################
# # test
# ###############################################################################

# FROM main AS test
# WORKDIR /var/app
# RUN pytest
