read E_VERSION < version
docker build -t e:$E_VERSION -f Dockerfile . --build-arg E_BASE_VERSION=$E_VERSION