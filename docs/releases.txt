*********************
Publicando Pacotes
*********************

Por que publicar pacotes
=========================



Preparar publicação
=====================

Considerando que os passos descritos em :doc:`ambiente` foram realizados, você
deve estar pronto para fazer releases(publicar) pacotes.

Como checklist, valide se você está pronto para publicação nos 3 ambientes mais
utilizados na empresa:

Extranet
--------

Repositório interno para release de pacotes, a sua utilização é restrita aos
colaboradores da Simples Consultoria.

Você deve ter uma conta na `Simplesnet <https://simplesnet.com.br/>`_ e fazer
parte do grupo de desenvolvedores. Caso não tenha, entre em contato com a
equipe de administração de sistemas.

PyPI
----

O repositório central de pacotes de projetos Python. Todos os pacotes públicos
desenvolvidos pela Simples Consultoria devem ser publicados aqui.

É necessária a criação de uma conta de acesso ao site, conforme documentado em
:ref:`PyPI <conta_pypi>`

Plone.org
---------

Repositório de pacotes para Plone. Apesar de ter certa redundância ao PyPI, a
política da Simples Consultoria é de utilizar, também, este repositório para a
publicação de pacotes que sejam para Plone.

É necessária a criação de uma conta de acesso ao site, conforme documentado em
:ref:`Plone.Org <conta_ploneorg>`

Validar a documentação
=======================

A documentação de pacotes Python é essencial para sua manutenção e sua divulgação.

Sendo assim recomendamos **sempre** uma análise dos seguintes itens antes da
sua publicação:


* Arquivo setup.py

    * Validar se os campos *keywords*, *description*, *author*, *author_email* e
      *classifiers* estão preenchidos com valores corretos

* Arquivo README.txt e <ns>/<ns>/<packagename>/README.txt

    * Estão preenchidos com informações corretas.

    * Créditos estão listados

    * Formatação ReST está correta

* Arquivo docs/HISTORY.txt

    * Está atualizado, com a lista das últimas modificações

    * Possui cabeçalhos com informações corretas sobre os releases

    * Formatação ReST está correta

Após estes passos vamos simular a geração de um arquivo HTML a partir da
documentação do pacote usando o comando **longtest**, instalado junto com o
**zest.releaser**:
::

    longtest

.. note:: Este comando deve ser executado **dentro** da pasta raiz do pacote.

Caso tudo esteja correto, será aberta, no seu navegador padrão, uma renderização
HTML da documentação. Esteja atento para possíveis erros e os corrija antes do
release final do pacote.

Fazer o Release
=================

Com as contas criadas, documentação do pacote validada e todas as alterações já
efetivadas no sistema de controle de versões, o passo seguinte é o release
propriamente dito.

O processo para o release de um pacote aciona um wizard que o guiará pelos
passos necessários:

.. warning:: A versão 3.20 do **zest.releaser** apresenta um bug quando
             utilizada para releases de pacotes a partir de repositórios
             Mercurial. Garanta que a versão seja 3.21 ou superior!

Dentro da pasta raiz do pacote, executamos o comando **fullrelease**:
::

    fullrelease

Após a informação de que estamos iniciando o processo de prerelease, a
primeira pergunta será sobre o número desta versão:
::

    INFO: Starting prerelease.
    Enter version [0.5]:

Informe a versão, ou pressione enter para manter a sugerida -- em nosso exemplo
a versão *0.5* -- e o wizard realizará a alteração do arquivo de histórico e
apresentará a opção de commitar as alterações para você:
::

    INFO: History file ./docs/HISTORY.txt updated.
    INFO: The 'svn diff':

    Index: docs/HISTORY.txt
    ===================================================================
    --- docs/HISTORY.txt	(revision 17763)
    +++ docs/HISTORY.txt	(working copy)
    @@ -2,8 +2,8 @@
     =========


    -0.5 - (Unreleased)
    --------------------
    +0.5 (2011-04-20)
    +----------------

     * Criados passos de Upgrade considerando o ambiente existente [erico_andrei]



    OK to commit this (Y/n)?

Caso aceite, o commit será confirmado e iniciaremos o processo de release
propriamente dito:
::

    INFO: Sending        docs/HISTORY.txt
    Transmitting file data .
    Committed revision 17766.

    INFO: Starting release.

Você será então perguntado sobre a necessidade da criação de uma tag referente
a esta versão do seu pacote:
::

    Tag needed to proceed, you can use the following command:
    svn cp https://simplesnet.com.br/svn/Clientes/FooBar/Foo/produtos/sc.foobar.foo/trunk https://simplesnet.com.br/svn/FooBar/Foo/produtos/sc.foobar.foo/tags/0.5 -m "Tagging 0.5"
    Run this command (Y/n)?

Aceite a realização deste comando e:
::

    Committed revision 17767.

A nova tag será criada.

Para garantir que a tag foi realizada corretamente, o wizard perguntará se deve
fazer o checkout da mesma para ser a base de nosso release. Aceite e o programa
iniciará o checkout (ou pull ou clone) e criará os arquivos para o release:
::

    Check out the tag (for tweaks or pypi/distutils server upload) (Y/n)?
    INFO: Doing a checkout...
    A    ...
    Checked out revision 17767.

    INFO: Tag checkout placed in /private/var/folders/SB/SBfcZTZiFmCshTe3PVg6LE+++TI/-Tmp-/sc.foobar.foo-0.5-cd8lbt
    INFO: Making an egg of a fresh tag checkout.
    running sdist
    running egg_info
    creating sc.foobar.foo.egg-info
    writing requirements to sc.foobar.foo.egg-info/requires.txt
    writing sc.foobar.foo.egg-info/PKG-INFO
    ...
    Writing sc.foobar.foo-0.5/setup.cfg
    creating dist
    tar -cf dist/sc.foobar.foo-0.5.tar sc.foobar.foo-0.5
    gzip -f9 dist/sc.foobar.foo-0.5.tar
    tar -cf dist/sc.foobar.foo-0.5.tar sc.foobar.foo-0.5
    gzip -f9 dist/sc.foobar.foo-0.5.tar
    removing 'sc.foobar.foo-0.5' (and everything under it)

As próximas perguntas são sobre quais repositórios serão alvo deste release.

.. note:: Estas configurações levam em conta o arquivo setup.cfg (do pacote)
          e as configurações existentes no arquivo **.pypirc**

No nosso exemplo, o pacote será publicado tanto no PyPI como na Extranet.
::

    WARNING: This package is NOT registered on PyPI.
    Register and upload to pypi (Y/n)?

Respondendo positivamente registraremos o pacote no PyPI e logo em seguida o
publicaremos:
::

    INFO: Running: //home/<meu_user>/py-paster/bin/python2.6 setup.py register -r pypi sdist  upload -r pypi
    Showing first few lines...
    running register
    running egg_info
    writing requirements to sc.foobar.foo.egg-info/requires.txt
    writing sc.foobar.foo.egg-info/PKG-INFO
    writing namespace_packages to sc.foobar.foo.egg-info/namespace_packages.txt
    ...
    Showing last few lines...
    removing 'sc.foobar.foo-0.5' (and everything under it)
    running upload
    Submitting dist/sc.foobar.foo-0.5.tar.gz to http://pypi.python.org/
    Server response (200): OK

Logo em seguida teremos a mesma pergunta para o ambiente da Extranet:
::

   Register and upload to extranet (Y/n)?

E em caso positivo, o processo se repetirá, até o momento da publicação.

O último passo do wizard é a realização do postrelease, que atualizará o arquivo
de histórico e a versão do produto:
::

    INFO: Starting postrelease.
    Current version is '0.5'
    Enter new development version ('dev' will be appended) [0.6]:

A pergunta é sobre o novo número de versão, manteremos a sugestão de *0.6*:
::

    INFO: New version string is '0.6dev'
    INFO: Changed ./sc/foobar/foo/version.txt to '0.6dev'
    INFO: Injected new section into the history: '0.6 (unreleased)'
    INFO: The 'svn diff':

    Index: sc/foobar/foo/version.txt
    ===================================================================
    --- sc/foobar/foo/version.txt	(revision 17750)
    +++ sc/foobar/foo/version.txt	(working copy)
    @@ -1 +1 @@
    -0.5
    \ No newline at end of file
    +0.6dev
    Index: docs/HISTORY.txt
    ===================================================================
    --- docs/HISTORY.txt	(revision 17766)
    +++ docs/HISTORY.txt	(working copy)
    @@ -2,6 +2,12 @@
     =========


    +0.6 (unreleased)
    +----------------
    +
    +- Nothing changed yet.
    +
    +
     0.5 (2011-04-20)
     ----------------

O wizard valida se queremos commitar estas alterações:
::

    OK to commit this (Y/n)?

E com nossa afirmativa ele efetiva as mudanças.
::

    INFO: Sending        docs/HISTORY.txt
    Sending        sc/foobar/foo/version.txt
    Transmitting file data ..
    Committed revision 17768.

    INFO: Finished full release.
    INFO: Reminder: tag checkout is in /private/var/folders/SB/SBfcZTZiFmCshTe3PVg6LE+++TI/-Tmp-/sc.foobar.foo-0.5-cd8lbt

O processo de release está feito e com isto este pacote estará disponível para
download dentro dos repositórios.
