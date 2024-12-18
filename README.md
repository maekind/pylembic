# pylembic

## Description

This package provides validation of Alembic migrations for Python projects.

It will check:

- Linearity: Ensures a clean and predictable migration chain.
- Circular dependencies: Prevents migration failures due to loops in the
dependency chain.
- Orphan migrations: Identifies migrations improperly created without linking
to any other migration.
- Multiple bases/heads: Identifies multiple bases or heads in the migration graph.
- Graph visualization: Provides a visual way to catch anomalies and understand the
migration flow.

## Installation

You can install this package using pip:

```bash
pip install pylembic
```

## Usage

### Testing

You can use this module with your preferred testing framework as follows:

```python
from os import path

from pytest import fixture

from pylembic.migrations import Validator


@fixture
def with_alembic_config_path():
    # We assume the migrations folder is at the root of the project,
    # and this test file is in the tests folder, also at the root of the project.
    # TODO: Feel free to adjust the path to your project's migrations folder.
    return path.abspath(
        path.join(path.dirname(path.dirname(__file__)), "migrations")
    )


def test_migrations(with_alembic_config_path):
    migration_validator = Validator(with_alembic_config_path)
    assert migration_validator.validate()
```

### Visualizing the migration graph

You can show the migrations graph by calling the method `show_graph`:

```python

from os import path

from pylembic.migrations import Validator

alembic_config_path = path.abspath(path.join("your path", "migrations"))

migration_validator = Validator(alembic_config_path)

migration_validator.show_graph()
```

### Command line

You can also use the command line for:

- Validating migrations:

    ```bash
    pylembic ./path/to/migrations --validate
    ```

- Visualizing the migration graph:

    ```bash
    pylembic ./path/to/migrations --show-graph
    ```

(c) 2024, <a href="mailto:marco@marcoespinosa.com">Marco Espinosa</a>
