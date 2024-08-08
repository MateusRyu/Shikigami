---
title: PCIe bus error
tags:
  - v1
aliases:
  - PCIe bus error
created_at: 2024-08-08T10:18:55-03:00
updated_at: 2024-08-08T10:30:08-03:00
---

`PCIe bus error` é uma mensagem de erro de comunicação com algum periférico. A mensagem em si não costuma  ser para problemas graves e significa apenas que ocorreu alguma pequena falha que pode afetar o comportamento esperado. Entretanto, pode ocorrer que a falta de compatibilidade de algum periférico gere uma sobrecarga de `PCIe bus error` que impede que a máquina execute novas tarefas e travando ela em um looping.

---

## Possíveis soluções

Editar o arquivo `/etc/default/grub` (necessário ter privilégio de `super user` ou `root`) e adicionar o param
```text
 GRUB_CMDLINE_LINUX_DEFAULT="quiet splash pci=noaer"
```