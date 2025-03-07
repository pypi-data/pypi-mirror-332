https://github.com/ALERTua/script.git


git submodule set-branch --branch main script


cd .github\workflows
gsudo mklink /h docker-image.yml ..\..\script\docker-image.yml
