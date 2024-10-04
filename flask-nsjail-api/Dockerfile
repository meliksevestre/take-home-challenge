# Written by Mélik Sevestre

FROM debian:bullseye

# Dependencies installation
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    protobuf-compiler \
    git \
    libprotobuf-dev \
    libnl-3-dev \
    libnl-route-3-dev \
    libcap-dev \
    libseccomp-dev \
    pkg-config \
    linux-headers-amd64 \
    libz-dev \
    flex \
    bison \
    curl \
    python3 \
    python3-pip

# Flask and python dependencies
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Nsjail cloning and compilation
WORKDIR /tmp
RUN git clone https://github.com/google/nsjail.git && cd nsjail && make

# Nsjail copy
RUN cp /tmp/nsjail/nsjail /usr/local/bin/nsjail

# Nsjail conf copy
COPY nsjail.cfg /etc/nsjail/nsjail.cfg

# Flask app's code copy
COPY . /app

# Expose port 8080
EXPOSE 8080

# Flask repo
WORKDIR /app

# Nsjail exec for secure Flask app
CMD ["nsjail", "--config", "/etc/nsjail/nsjail.cfg", "--", "python3", "/app/app.py"]

