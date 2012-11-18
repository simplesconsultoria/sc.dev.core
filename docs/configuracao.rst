*************************
Configurando o ambiente
*************************

Para garantir maior produtividade e acesso a repositórios externos, existem 
algumas pequenas configurações que devem ser realizadas.

Acesso via proxy
================

Caso seu acesso internet seja feito através de um proxy é necessária a 
configuração do mesmo no sistema operacional para que o Python -- através da 
biblioteca urllib consiga acessar repositórios externos.

Windows
-------

* Clique com o botão direito em 'Meu Computador'

* Clique na aba 'Avançado'

* Clique em 'Variáveis de Ambiente'

* Adicione as seguintes variáveis de ambiente (valores de exemplo entre 
  parênteses)
    
    * http_proxy (http://meuproxy:3128)
    
    * https_proxy (http://meuproxy:3128)
    
    * ftp_proxy (http://meuproxy:3128)

MacOS e Linux
---------------

Na linha de comando digite:
::

    $ export http_proxy="http://meuproxy:3128"
    $ export https_proxy="http://meuproxy:3128"
    $ export ftp_proxy="http://meuproxy:3128"

.. note:: Estes comandos podem ser adicionados aos seus arquivos de
          inicialização (ex:.profile, .bash_profile) para que as configurações
          não sejam perdidas

Subversion
-----------

Diferente de quase todo o resto das soluções utilizas, o Subversion não leva em 
consideração as variáveis de ambiente http_proxy, https_proxy. 

Para configurar o acesso através de um proxy, procure a pasta de configurações 
do Subversion, usualmente **.subversion** e edite o arquivo **servers**
::

    vim ~/.subversion/servers

No final do arquivo, dentro da seção **[global]**, edite as configurações 
relacionadas ao proxy, com as informações passadas pelo administrador de rede.
::

    http-proxy-host = meuproxy
    http-proxy-port = 3128
    # http-proxy-username = defaultusername
    # http-proxy-password = defaultpassword

Como pode ser visto, é possível adicionarmos as informações de usuário e senha 
para o proxy nas variáveis seguintes -- neste exemplo comentadas (iniciando com 
**#**).

Configurações salvas, é só testar o acesso do Subversion com um comando, como:
::
    
    svn co https://svn.plone.org/svn/collective/sc.dev.core/trunk sc.dev.core

Que deve realizar o checkout da versão de desenvolvimento do sc.dev.core.

Repositórios de pacotes
========================

A instalação do pacote **collective.dist** habilita o suporte à utilização de 
múltiplos repositórios de pacotes para interpretadores Python.

.. note:: Este suporte é incluido em versões mais recentes do Python (>=2.6)

Com este suporte é possível publicar -- fazer o release de -- pacotes não 
apenas no repositório *oficial* da comunidade Python, o Pypi 
(http://pypi.python.org), mas também em outros repositórios públicos como o 
existente no site Plone (http://plone.org/products/) ou em repositórios privados 
ou não acessíveis na Internet.

.. note:: O **collective.dist** está incluído como dependência na instalação 
          do **sc.dev.core**

Arquivo .pypirc
-----------------

O suporte aos múltiplos repositórios é configurado no arquivo **.pypirc** 
localizado na raiz da pasta do usuário.

Uma configuração de exemplo contendo informações para o pypi.python.org, o 
repositório de produtos do plone.org e um repositório privado pode ser visto 
abaixo.
::

    [distutils]
    index-servers =
        pypi
        plone.org
        mycompany


    [pypi]
    username:user
    password:password

    [plone.org]
    repository:http://plone.org/products
    username:ploneuser
    password:password

    [mycompany]
    repository:http://my.company/products
    username:user
    password:password

.. note:: Não se esqueça de criar suas contas tanto no Pypi quanto no site do 
          Plone. Estas informações são úteis para o release de pacotes e 
          documentação de erros encontrados.

Para outras referências sobre o **collective.dist** acesse
http://pypi.python.org/python/collective.dist .

Penduricalhos no Python
========================

É possível configurar o comportamento padrão do interpretador Python em seu 
computador.

Estas configurações ficam armazenadas no arquivo **.pythonrc.py** na raiz da 
pasta de seu usuário.

Um exemplo de configuração é a inclusão do auto-complete, que pode ser realizada 
editando o arquivo **.pythonrc.py** para conter o código abaixo:
::
    
    import rlcompleter, readline
    readline.parse_and_bind('tab: complete')

Configurações para Buildout
===========================

Como boa parte de nosso trabalho é realizado com buildouts, é sugerida a 
criação de configurações padrão para o seu ambiente.

Na raiz de sua pasta de usuário, crie uma nova pasta com o nome de 
**.buildout**:
::

    mkdir ~/.buildout

Dentro desta pasta adicione um arquivo **default.cfg** com as configurações de 
cache para downloads:
::
    
    [buildout]
    zope-directory= /home/<meu_user>/cache/zope 
    download-cache= /home/<meu_user>/cache/download 
    eggs-directory= /home/<meu_user>/cache/eggs
    extends-cache = /home/<meu_user>/cache/extends

.. warning:: Substitua <meu_user> pelo nome de seu usuário [Linux, Mac]

Antes de rodar um novo buildout você deve criar as pastas para a realização 
do cache:
::

    mkdir -p /home/<meu_user>/cache/{zope,download,eggs,extends}

A próxima vez que um buildout for executado nesta máquina, os arquivos serão 
baixados nas pastas de cache -- evitando assim duplicidades.

.. note:: Caso deseje, é possível não usar estas configurações, ao passar a 
          opção **-U**

