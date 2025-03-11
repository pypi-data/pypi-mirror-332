Command Line
============

The **fitrequest** tool automatically generates a command-line interface (CLI) based on the methods it creates.
Each class includes a ``cli_run`` method that launches a `Typer <https://typer.tiangolo.com/>`_ application containing all the generated methods from fitrequest.
This setup ensures that configuration validation and authentication are seamlessly handled.

Additionally, the output is formatted using the `rich library <https://rich.readthedocs.io/en/stable/introduction.html>`_,
which enhances readability with color-coding.
This feature makes it straightforward to test the generated requests quickly and efficiently.

To utilize the CLI tool, simply add the ``cli_run`` function as a console script in your project's pyproject.toml file, as demonstrated below.


.. code-block:: toml

  [project.scripts]
  restapi-cli = "tests.demo_decorator_pydantic_return:RestApiClient.cli_run"


Below an example of output:

.. image:: images/restapi-cli.png
