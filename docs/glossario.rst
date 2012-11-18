.. _glossario:

Glossário
=========

.. glossary::
   :sorted:

   virtualenv
      Pacote que implementa um ambiente separado de Python, permitindo a
      instalacão de outros pacotes e a realização de configurações sem que estes
      influenciem o Python utilizado pelo sistema.
      Essencial no uso do i18ndude e do ArchGenXML.

   ``>>>``
      Prompt padrão do Python quando acessado interativamente. Usualmente
      encontrado em blocos de documentação e testes de código doctest.

   ``...``
      Prompt padrão do Python quando acessado interativamente para a inserção de
      código indentado ou dentro de delimitadores esquerdo e direito.
      (Aspas, colchetes, parênteses, chaves).

   ZEO
      Zope Enterprise Objects é uma maneira de utilizar o Zope de maneira
      distribuída. Com o ZEO é possível contar com diversas instâncias do
      servidor de aplicações Zope conectadas a uma base de dados ZODB
      compartilhada.

   zc.buildout
      Sistema para criação, montagem e implementação de aplicações. Permite que
      sejam criados arquivos de configuração que detalham como deve se comportar
      cada instalação.
      Para saber mais, acesse `Buildout <http://www.buildout.org/>`_

   cli
      Do inglês Command Line Interface. Interface de linha de comando.

   Supervisor
      Solução cliente-servidor que permite o monitoramento e controle de
      processos em sistemas operacionais Unix-like.
      Para saber mais, acesse `Supervisord <http://supervisord.org/>`_

   Varnish
      Acelerador web de altíssima performance, desenvolvido levando em
      consideração a maneira como os sistemas operacionais atuais gerenciam
      recursos.
      Para saber mais, acesse `Varnish <http://varnish.projects.linpro.no/>`_

   LDAP
       Acrônimo que significa **Lightweight Directory Access Protocol**, o LDAP
       é um protocolo que define serviços de diretório. Existem várias soluções
       que implementam este protocolo -- como ferramentas de catálogo de
       usuários (AddressBook, OSXX) -- e também soluções de backend, como o
       Active Directory e o OpenLdap.

   crontab
       Tabela de trabalhos a serem executados de maneira programada pelo
       sistema operacional. Para verificar quais os trabalhos estão agendados
       por um usuário, utilize :command:`crontab -l -u <username>`

   ZODB
       Base de dados :term:`nosql` orientada a objetos desenvolvida pela
       `Zope Corporation <http://www.zope.com>`_. É utilizada como base de
       dados padrão pelo servidor de aplicações Zope -- e consequentemente
       pelo Plone.

   nosql
       Base de dados não relacional. Alguns exemplos são :term:`ZODB` e MongoDB.
       Este termo refere-se ao fato que estas bases não aderem ao padrão SQL.

   storage
       Implementação de armazenamento de dados para o :term:`ZODB`. Hoje são
       dois os storages mais utilizados: :term:`Filestorage` e
       :term:`Relstorage`.

   Filestorage
       Implementação de armazenamento para :term:`ZODB` que utiliza um arquivo
       no sistema de arquivos para persistir os dados. Usualmente este arquivo
       tem nome de Data.fs.

   Relstorage
       Implementação de armazenamento para :term:`ZODB` que persistir os dados
       em base de dados relacional (:term:`RDBMS`). Apesar do uso de uma base
       SQL, os dados armazenados através do Relstorage não são acessíveis sem
       a utilização do ZODB.

   RDBMS
       Sistema de gestão de base de dados relacional

   dsn
       Acrônimo de Data Source Name, é o identificador utilizado em conexões
       ODBC.