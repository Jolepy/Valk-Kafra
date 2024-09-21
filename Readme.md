<h1 align="center">
📄<br>Valk Kafra - Sistema de Gerenciamento de Inventários para Ragnarok Online
</h1>

***  Índice ***
* [Descrição do Projeto](#descrição-do-projeto)
* [Pré requisitos](#pré-requisitos)
* [Execução](#execução)
* [Bibliotecas](#bibliotecas)

# Descrição do Projeto
> Este repositorio foi criado inicialmente como um trabalho de extensão para a materia de Banco de Dados na Estacio. 

 O Valk Kafra foi desenvolvido para facilitar a gestão de itens em múltiplas contas de jogadores de Ragnarok Online, possibilitando que todos os inventários sejam gerenciados em um único sistema. Com isso, elimina-se a necessidade de abrir cada conta individualmente para verificar os itens, otimizando o tempo e aumentando a eficiência do gerenciamento.
 O codigo e de uso livre, não comercial.

> Pasta Valk Kafra esta o .rar com o executavel e os arquivos necessarios para o aplicativo.

 ## Pré requisitos
 >Para executar diretamento o codigo.
 * Sistema operacional Windows
 *  IDE de python (ambiente de desenvolvimento integrado de python)
 *  Biblioteca Tkinter e SQLite.

>Para somente usar o aplicativo, baixar o Valk Kafra.rar

 *  Winrar e afins (Ou windows 11 que lhe permita extrair arquivos .rar)

## Execução

Ao executar o codigo ou o aplicativo, uma janela e aberta, com botões interativos, os seguintes botões, *Adicionar, *Deletar, *Atualizar e *Procurar.
>Funções detalhadas dos botões.

*<strong>ADICIONAR:</strong> Abre uma janela, para inserção das informações referentes a "Nome do Produto"(referente ao item), Quantidade (referente a quantidade de tal item) e a conta (a qual esse item pertence ou esta no momento).<br>
*<strong>DELETAR:</strong> Abre uma janela para a inserção do nome do item a ser deletado, o item precisa ser escrito por inteiro, da mesma forma que esta no banco de dados, essa função deleta o item de todas as contas ao mesmo tempo.<br>
*<strong>ATUALIZAR:</strong> Abre uma janela para a remoção de uma quantidade a expecifica de um item em uma conta expecifica, e necessario colocar o nome completo e a conta para adicionar ou remover uma quantidade de itens, para remover colocar um valor negativo (exemplo -2), para adicionar não e necessario nenhum acrescimo.<br>
*<strong>PROCURAR:</strong> Abre uma janela para procurar algo no Database do que ja foi inserido, podendo fazer a busca por nome, parte do nome ou por conta.<br>

>setup.py seria para criar um arquivo executavel de forma facil usando cx_freeze.

## Bibliotecas
* <strong>tkinter:</strong> biblioteca de criação de sistemas interativos (janelas)<br>
* <strong>sqlite3:</strong> bibliotecas de banco de dados localmente<br>
* <strong>cx_freeze:</strong> bibliotecas usado para criar um arquivo executavel para o setup.py<br>

