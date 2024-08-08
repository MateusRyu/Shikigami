---
title: SSH
tags:
  - v1
aliases:
  - SSH
created_at: 2024-07-26T13:21:33-03:00
updated_at: 2024-08-07T17:50:17-03:00
---
# SSH
---
O [protocolo](../../../../ideias/2024/07/06/Protocolo.md) Secure Shell (SSH) é um método para se conectar com segurança a um computador em uma rede não segura para poder executar comandos ou transferir arquivos. O SSH usa [Criptografia](../../06/30/Criptografia.md) para autenticar e criptografar conexões entre dispositivos por meio de uma chave.

## Verificar chaves existentes
```shell
ls -al ~/.ssh
```

## Criar chave SSH
```shell
ssh-keygen -t rsa -b 4096 -C your@email.com
```
## Adicionar chave ssh ao ssh-agent
O [ssh-agent](../../../../ideias/2024/07/08/ssh_agent.md) é um programa que registra e armazenas as [chaves privada](../../../../ideias/2024/07/12/Chaves_privada.md).

1. Verifique se ele está em execução:
	- No [Linux](../08/2024-06-30-Linux.md) ou [Mac](../../../../ideias/2024/07/12/Mac.md): 
	```shell
	eval "$(ssh-agent -s)" # for Mac and Linux`
	```
	-  No [Windows](../../06/30/Windows.md):
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
