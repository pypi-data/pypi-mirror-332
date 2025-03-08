Development
-----------

This project is built and published using `uv <https  ://docs.astral.sh/uv>`__. To setup a development environment for this project you can follow these steps:

1. Install `uv <https://docs.astral.sh/uv/#installation>`__.
2. Navigate to the root folder and install the project's virtual environment:

.. code:: shell

   uv sync

3. You should now have ``.venv`` directory created containing the project's virtual environment files. You can optionally activate the environment subshell by running:

.. code:: shell

   source .venv/bin/activate

4. To deactivate the environment subshell, run:

.. code:: shell

   deactivate

5. Format the code by running the command:

.. code:: shell

   uv run ruff format

6. Check the code linting by running the command:

.. code:: shell

   uv run ruff check

7. Run the unit tests by running the command:

.. code:: shell

   uv run pytest

8. To export the detailed dependency list, run the following:

.. code:: shell

   # Export the package dependencies to requirements.txt
   uv export --no-default-groups > requirements.txt

   # If you wish to include development dependencies as well, run the following command
   uv export --group dev > requirements-dev.txt

   # The same as above if you wish to export documentation dependencies
   # Use the flag --no-hashes to exclude the hash values
   uv export --group docs --no-hashes > requirements-docs.txt
