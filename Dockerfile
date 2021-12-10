# Docker file for the group project
# Group 4 Dongxiao Li, Dec, 2021
# Publish to Dockerhub

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# install R packages
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  && install2.r --error \
    --deps TRUE \
    docopt \
    readr \
    ggplot2 \
    dplyr \
    knitr \
    caret \
    gridExtra 
    

# install the kableExtra package using install.packages
RUN Rscript -e "install.packages('kableExtra')"

# install libxt6
RUN apt-get install -y --no-install-recommends libxt6

# install the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

# put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"


# RUN pip install "jupyter-book==0.12.*" 

# install python 3 packages
RUN pip install \
    "numpy==1.21.*" \
    "pandas" \
    "docopt==0.6.*" \
    "scikit-learn==1.0.*" \
    "scipy==1.7.*" \
    "pandas-profiling==1.4.*" \
    "requests==2.24.*" \
    "ipykernel==6.5.*" \
    "ipython>=7.15" \
    "matplotlib==3.5.*" 

# install pandoc in conda
RUN conda install -c conda-forge pandoc

# install jupyter-book
RUN pip install "jupyter-book==0.12.*"
