all: java/apache-maven-3.6.1 java/wildfly-16.0.0.Final java/jdk-11.0.4+11 github/cws/accessories/release/bin/wildfly.sh

downloads:
        mkdir -p downloads

downloads/OpenJDK11U-jdk_x64_linux_hotspot_11.0.4_11.tar.gz: downloads
        cd downloads && wget -nc https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.4%2B11/OpenJDK11U-jdk_x64_linux_hotspot_11.0.4_11.tar.gz

downloads/wildfly-16.0.0.Final.tar.gz: downloads
        cd downloads && wget -nc https://download.jboss.org/wildfly/16.0.0.Final/wildfly-16.0.0.Final.tar.gz

downloads/apache-maven-3.6.1-bin.tar.gz: downloads
        cd downloads && wget -nc https://www-us.apache.org/dist/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz

java:
        mkdir -p java

java/apache-maven-3.6.1: java downloads/apache-maven-3.6.1-bin.tar.gz
        cd java && tar xzf ../downloads/apache-maven-3.6.1-bin.tar.gz

java/jdk-11.0.4+11: java downloads/OpenJDK11U-jdk_x64_linux_hotspot_11.0.4_11.tar.gz
        cd java && tar xzf ../downloads/OpenJDK11U-jdk_x64_linux_hotspot_11.0.4_11.tar.gz
        cd java && ln -s jdk-11.0.4+11 jdk11

java/wildfly-16.0.0.Final: java downloads/wildfly-16.0.0.Final.tar.gz
        cd java && tar xzf ../downloads/wildfly-16.0.0.Final.tar.gz
        touch java/wildfly-16.0.0.Final

github/cws: 
        git clone https://github.com/JavaDogs/cws.git github/cws

github/cws/accessories/release/bin/wildfly.sh: SHELL:=/bin/bash
github/cws/accessories/release/bin/wildfly.sh: github/cws
        source env.sh && cd github/cws && mvn clean install -Dmaven.javadoc.skip=true
        touch github/cws/accessories/release/bin/wildfly.sh