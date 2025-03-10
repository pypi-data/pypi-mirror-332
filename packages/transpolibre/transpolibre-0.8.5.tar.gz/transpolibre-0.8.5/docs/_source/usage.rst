=====
Usage
=====
Thusly.

Help
----

.. code-block:: bash

  $ transpolibre --help
  usage: transpolibre [-h] [-a API_KEY] [-d] [-f FILE] [-l] [-o] [-s SOURCE_LANG] [-t TARGET_LANG] [-u URL] [-v] [-V]
  
  Translate PO files with LibreTranslate
  
  options:
    -h, --help            show this help message and exit
    -a API_KEY, --api-key API_KEY
                          LibreTranslate API key
    -d, --debug           Debugging
    -f FILE, --file FILE  PO file to translate
    -l, --list            List available languages
    -o, --overwrite       Overwrite existing translations
    -s SOURCE_LANG, --source-lang SOURCE_LANG
                          Source Language ISO 639 code (Default en)
    -t TARGET_LANG, --target-lang TARGET_LANG
                          Target Language ISO 639 code (Default es)
    -u URL, --url URL     LibreTranslate URL (Default http://127.0.0.1:8000)
    -v, --verbose         Increase output verbosity
    -V, --version         Show version

Examples
--------
To translate a single PO file:

.. code-block:: bash

  transpolibre -f locale/es/myprogram.po

To translate specifying to/from language:

.. code-block:: bash

  transpolibre -s en -t fr -f locale/fr/myprogram.po

To use a particular LibreTranslate server:

.. code-block:: bash

  transpolibre -u http://192.168.1.100:8000 -s en -t it -f locale/it/myprogram.po

To list languages available on a LibreTranslate server:

.. code-block:: bash

  transpolibre -u http://192.168.1.100:8000 --list

To translate all the PO files in a directory:

.. code-block:: bash

  for i in locale/eo/*.po
      do transpolibre -u http://192.168.1.100:8000 -s en -t eo -f $i
  done

Dotenv
------
The LibreTranslate URL and API key can be stored using dotenv, so it doesn't
need to be specified on the command line. For instance instead of doing this:

.. code-block:: bash

  transpolibre --url http://192.168.1.100:8000

You can add the URL adding the ``LT_URL`` variable to an ``.env``
file in the base directory:

.. code-block:: bash

  LT_URL="http://192.168.1.100:8000"

The same can be done with the API key, such as:

.. code-block:: bash

  LT_API_KEY="00000000000000000000000000000"

