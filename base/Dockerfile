FROM python:3.7-slim

ARG E_BASE_VERSION
ARG USERNAME=epiuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV E_OUTPUT_DIR=/output

RUN apt-get update \
    && apt-get -y install curl wget gcc make musl-dev libffi-dev tar unzip openssh-client

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir $E_OUTPUT_DIR \
    ;chown :$USERNAME $E_OUTPUT_DIR \
    && chmod g+w $E_OUTPUT_DIR

USER $USERNAME

ENTRYPOINT ["/bin/bash"]