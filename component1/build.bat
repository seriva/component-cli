set /p C_NAME=<name
set /p C_VERSION=<version
docker build -t luukvv/%C_NAME%:%C_VERSION% -f Dockerfile . --build-arg C_NAME=%C_NAME% --build-arg C_VERSION=%C_VERSION%