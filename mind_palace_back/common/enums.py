import inspect


class DjangoChoicesEnum:

    @classmethod
    def keys(cls):
        return [
            attribute_name
            for attribute_name in dir(cls)
            if not attribute_name.startswith('__') and not inspect.ismethod(
                getattr(cls, attribute_name)
            )
        ]

    @classmethod
    def values(cls):
        return [
            getattr(cls, attribute_name)
            for attribute_name in dir(cls)
            if not attribute_name.startswith('__') and not inspect.ismethod(
                getattr(cls, attribute_name)
            )
        ]

    @classmethod
    def choices(cls) -> tuple:
        """
        Get tuple of attributes and their values.

        Returns:
            choices_tuple: Tuple of tuples that represent all user defines attributes on this
            enum class where first value is attribute value and second is attribute name.
        """
        return tuple([
            (attribute_name, getattr(cls, attribute_name))
            for attribute_name in dir(cls)
            if not attribute_name.startswith('__') and not inspect.ismethod(
                getattr(cls, attribute_name)
            )
        ])

    @classmethod
    def choices_as_dict(cls) -> dict:
        """
        Get dict of attributes as a dict where key is attribute name and attribute value as value.

        Returns:
            attributes dict
        """
        return dict(cls.choices())
