FROM e:0.0.1

ARG C_NAME
ARG C_VERSION

ENV C_NAME $C_NAME
ENV C_VERSION $C_VERSION
ENV TERRAFORM_VERSION 0.12.28
ENV ANSIBLE_VERSION 2.8.6
ENV AZURECLI_VERSION 2.8.0

# Copy component sources
COPY /src/ /component
WORKDIR /component

# Install Terraform
RUN sudo wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && sudo unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && sudo mv terraform /usr/local/bin/ \
    && sudo terraform --version

# Install Ansible, AzureCLI, Boto
RUN sudo pip --disable-pip-version-check --no-cache-dir install ansible==${ANSIBLE_VERSION} azure-cli==${AZURECLI_VERSION} boto3 --default-timeout=100

# Install some other packages needed for common code. Should be moved later
RUN pip --disable-pip-version-check --no-cache-dir install python-json-logger --default-timeout=100

ENTRYPOINT ["python", "main.py"]