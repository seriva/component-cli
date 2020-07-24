FROM python:3.7-slim

ENV DEBIAN_FRONTEND=noninteractive

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV TERRAFORM_VERSION 0.12.28
ENV ANSIBLE_VERSION 2.8.6
ENV AZURECLI_VERSION 2.8.0

# Install some common packages
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    && apt-get -y install wget git git-lfs procps lsb-release gcc make musl-dev libffi-dev tar unzip vim 

# Install Terraform
RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && mv terraform /usr/local/bin/ \
    && terraform --version

# Install Ansible, AzureCLI, Boto
RUN pip --disable-pip-version-check --no-cache-dir install ansible==${ANSIBLE_VERSION} azure-cli==${AZURECLI_VERSION} boto3 --default-timeout=100

# Install some other packages needed for common code. Should be moved later
RUN pip --disable-pip-version-check --no-cache-dir install python-json-logger --default-timeout=100


# Setup user and access rights for devcontainer
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND=
