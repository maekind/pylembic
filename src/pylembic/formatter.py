from logging import Formatter


class CustomFormatter(Formatter):
    """Custom formatter that handles missing fields gracefully."""

    params = [
        "bases",
        "dependency",
        "down_revisions",
        "heads",
        "migration",
        "orphans",
        "up_revisions",
    ]

    def format(self, record):
        """Format the log record with default values for missing fields."""
        for param in self.params:
            if not hasattr(record, param):
                setattr(record, param, "")

        return super().format(record)
