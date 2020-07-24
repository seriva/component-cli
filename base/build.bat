set /p E_VERSION=<version
docker build -t luukvv/base:%E_VERSION% -f Dockerfile . --build-arg E_BASE_VERSION=%E_VERSION%