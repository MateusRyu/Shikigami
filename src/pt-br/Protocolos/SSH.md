O protocolo Secure Shell (SSH) é um método para se conectar com segurança a um computador em uma rede não segura para poder executar comandos ou transferir arquivos. O SSH usa [Criptografia](Criptografia.md) para autenticar e criptografar conexões entre dispositivos por meio de uma chave.

## Verificar chaves existentes
```shell
ls -al ~/.ssh
```

## Criar chave SSH
```shell
ssh-keygen -t rsa -b 4096 -C your@email.com
```
## Adicionar chave ssh ao ssh-agent
O [ssh-agent](ssh-agent) é um programa que registra e armazenas as [Chaves privada](Chaves%20privada).

1. Verifique se ele está em execução:
	- No [Linux](Linux.md) ou [Mac](Mac):
	```shell
eval "$(ssh-agent -s)" # for Mac and Linux
```
	-  No [Windows](Windows.md):
	```shell
eval `ssh-agent -s`
ssh-agent -s # for Windows
```
2. Adiciona a chave com:
```shell
ssh-add ~/.ssh/id_rsa
```
## Copiar chave pública
Para Linux ou Mac:
```shell
cat ~/.ssh/id_rsa.pub
```

Para Windows:
```shell
clip < ~/.ssh/id_rsa.pub #
```
