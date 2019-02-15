class Validate:
    """Provides a set of methods for validating function arguments."""

    @staticmethod
    def required(value, name):
        """Check that a required value was provided. If not, raise a `ValueError`."""
        if value is None:
            raise ValueError("{} must be supplied".format(name))

    @staticmethod
    def positive(value, name):
        """Check that a value provided is positive. If not, raise a `ValueError`."""
        if value <= 0:
            raise ValueError("{} must be positive".format(name))

    @staticmethod
    def non_negative(value, name):
        """Check that a value provided is non-negative. If not, raise a `ValueError`."""
        if value < 0:
            raise ValueError("{} must be non-negative".format(name))

    @staticmethod
    def one_only(values, names):
        """Check that one, and only one, of a set of values was provided.
        If not, raise a `ValueError`."""
        provided_names = [v[1] for v in zip(values, names) if v[0] is not None]

        if len(provided_names) == 0:
            raise ValueError("one of {} must be supplied".format(" or ".join(names)))
        elif len(provided_names) > 1:
            raise ValueError("{} were supplied; only one can be specified"
                             .format(" and ".join(provided_names)))

    @staticmethod
    def one_of_allowable(value, allowable, name):
        """Check that the value provided is one of a set of allowable values.  If not,
        raise a `ValueError`."""
        if value not in allowable:
            raise ValueError("{} must be one of: {}".format(name, allowable))
