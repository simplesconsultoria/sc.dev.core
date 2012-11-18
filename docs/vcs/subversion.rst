Subversion (svn)
=====================

Introduções
----------------------

O Subversion (svn) é um sistema de controle de versões, uma evolução do CVS.

Ele se baseia na existência de um repositório único e centralizado, que mantém
todo o histórico e as versões.

Para manipulação de alguma informação contida no repositório é necessário criar
uma cópia de trabalho localmente.

Ao realizar alterações nas informações da cópia de trabalho ela se distancia da
versão base mantida no repositório e estas alterações só são sincronizadas
mediante a realização de um commit.

Historicamente a Simples Consultoria utilizou o Subversion para a gestão de
seus códigos-fonte, com seu repositório em https://simplesnet.com.br/svn/. A
partir de Abril de 2011 foi definido que os novos projetos utilizarão o
Mercurial, hospedado no provedor Bitbucket, como controle de versão e que os
projetos antigos serão gradualmente migrados para esta nova estrutura.

Pacotes e projetos desenvolvidos pela Simples Consultoria para uso da
comunidade são mantidos no `Github <http://github.com>`_.

.. warning::
    Projetos/Pacotes hospedados em repositórios do Plone ou do Zope, continuam
    sendo mantidos com Subversion. Alguns projetos de clientes usarão Git e a
    comunidade Plone está migrando seus projetos para o GitHub.


Instalando
----------------------

Caminho fácil
--------------

O jeito fácil e rápido de começar a trabalhar com o Subversion é através do uso
de uma ferramenta com interface gráfica.

Em ambientes Windows, a mais famosa delas é o TortoiseSVN. Para sua instalação
acesse http://tortoisesvn.net/downloads.html, baixe a versão mais recente e a
instale.

Para ambientes OSX e Linux existem diversas versões de GUI e inclusive uma
cross-platform: `RapidSVN <http://rapidsvn.tigris.org/>`_ .

Além disto, os gerenciadores de pacotes destes sistemas operacionais sempre
contam com o pacote do Subversion.

OSX
^^^^^^^^^^^^^^^^^^^^^^^

Usando o brew
::

    brew install subversion

Linux - Debian/Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^

Usando o apt:
::

    sudo apt-get install subversion

Linux - RedHat/CentOS/Fedora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Usando o yum:
::

    sudo yum install subversion

Configurações Básicas
----------------------

A configuração do Subversion sempre pode ser realizada através da edição dos
arquivos localizados na pasta **.subversion** na pasta raiz do usuário.

Boa parte das configurações é realizada no arquivo **config**, que é divido em
algumas seções. A primeira seção é a **[auth]** onde é possível configurar como
o Subversion se comportará com relação ao armazenamento de credenciais e senhas.
::

    [auth]
    store-passwords = yes
    # store-auth-creds = no
    #password-stores = windows-cryptoapi #Windows
    #password-stores = gnome-keyring #Linux
    password-stores = keychain #OSX

No exemplo de configuração acima definimos que o Subversion armazenará as senhas
para acesso aos respositórios e que utilizará o Keychain do OSX como mecanismo
de backend.

Caso você utilize Windows, comente a última linha e descomente a linha que
indica windows-cryptoapi como backend.

Para Linux, comente a linha relativa ao OSX e descomente a linha do
gnome-keyring.

.. warning:: Em servidores, quando utilizar o Subversion tenha certeza de que
             a configuração do arquivo config indique que
             **store-auth-creds = no** e **store-passwords = no**.

A próxima seção mais comumente editada é a que define aplicações auxiliares ao
Subversion. A seção **[helpers]** define, por exemplo, qual o editor de texto a
ser utilizado para documentar as ações realizadas.

Abaixo temos um exemplo desta seção já com algumas opções de editores listados.
::

    [helpers]
    editor-cmd = "mate -w"
    #editor-cmd = "vim"
    #editor-cmd = "gvim --nofork"
    #editor-cmd = "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

O editor habilitado, neste exemplo, é o TextMate do OSX. As opções seguintes
configurariam o editor **vim** para ambiente terminal (Linux, OSX),
o **gvim** para ambientes gráficos em Linux e o **Notepad++** para Windows.

Subversion 101
----------------------

A utilização do Subversion é bastante simples e direta. Contando com um
repositório central, sempre é necessário realizar o checkout do código para a
criação de uma cópia local.

Alterações são realizadas na cópia local, é realizada uma atualização da cópia
de trabalho e as alterações locais sãoenviadas para o repositório central.

Lista de comandos
^^^^^^^^^^^^^^^^^^^^^^^

============ ========== ========================================================
Comando       Atalho     Descrição
============ ========== ========================================================
checkout      co         Cria uma cópia de trabalho a partir do repositório
update        up         Atualiza a cópia local com a versão mais atual
                         no repositório
commit        ci         Envia as alterações da cópia de trabalho para o
                         repositório
revert                   Reverte arquivo(s)/diretório(s) ao estado de sua
                         última atualização junto ao repositório.
status        st         Informa qual a situação da cópia de trabalho
add                      Adiciona conteúdo à cópia local -- e após um commit,
                         ao repositório
remove        rm         Remove conteúdo do repositório ou da cópia de trabalho
info                     Exibe informações sobre o repositório, cópia de
                         trabalho ou conteúdo
log                      Exibe histórico sobre conteúdo ou repositório
diff                     Exibe diferenças na cópia de trabalho ou em arquivos
                         listados
============ ========== ========================================================

Ciclo de trabalho
^^^^^^^^^^^^^^^^^^^^^^^

Inicialmente criamos uma cópia de trabalho a partir do repositório.
::

    svn co https://svn.plone.org/svn/collective/sc.dev.core/trunk

Isto criará uma **cópia de trabalho** chamada trunk na pasta atual.
É possível, desejável até, dar um nome arbitrário a cópia de trabalho
::

    svn co https://svn.plone.org/svn/collective/sc.dev.core/trunk sc.dev.core

Após alterar o código do arquivo setup.py dentro da cópia de trabalho é
possível efetivar a alteração no repositório realizando um commit
::

    svn commit setup.py

Com isto **este** arquivo teve suas alterações enviadas para o repositório. No
Subversion é usual que os commits agrupem alterações realizadas em vários
arquivos. Para realizar o commit das alterações de uma pasta, *docs* por exemplo
o comando seria:
::

    svn commit docs/

Efetivando todas as alterações realizadas em arquivos sob esta pasta.

Podemos adicionar novos arquivos ao controle de versão:
::

    svn add MANIFEST.in

E enviá-lo ao repositório:
::

    svn commit MANIFEST.in

Também é possível remover um arquivo ou pasta na cópia de trabalho:
::

    svn remove sc.dev.core.egg-info

Ou diretamente no repositório:
::

    svn remove https://svn.plone.org/svn/collective/sc.dev.core/trunk/sc.dev.core.egg-info

O repositório pode ter sido alterado por outras pessoas, portanto é necessário
sincronizar sua cópia de trabalho com a versão mais recente do servidor:
::

    svn update

Que realizará esta ação para toda a cópia de trabalho, ou se você quiser
sincronizar apenas uma pasta:
::

    svn update docs

As diferenças entre a versão atual do conteúdo e sua última atualização podem
ser exibidas com o comando diff:
::

    svn diff docs

Para reverter as alterações ao estado de sua última
sincronização com o repositório, usamos o comando revert:
::

    svn revert docs

Para resumir, o ciclo é::

     svn co https://svn.plone.org/svn/collective/sc.dev.core/trunk sc.dev.core
     <modificações>
     svn commit
     <modificações>
     svn commit
     <sincronização>
     svn update
     <adiciona um arquivo>
     svn add MANIFEST.in
     svn commit MANIFEST.in


