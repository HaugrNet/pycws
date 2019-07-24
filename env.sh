# Additional settings for CWS
JAVA_ROOT=${PWD}/java
export CWS_HOME=${PWD}/github/cws
export JAVA_HOME=${JAVA_ROOT}/jdk11
export M2_HOME=${JAVA_ROOT}/apache-maven-3.6.1
export JBOSS_HOME=${JAVA_ROOT}/wildfly-16.0.0.Final
export PATH=${HOME}/bin:${CWS_HOME}/accessories/release/bin:${JAVA_HOME}/bin:${M2_HOME}/bin:${JBOSS_HOME}/bin:${PATH}