# -*- coding: utf-8 -*-
from click import make_pass_decorator
from jinja2 import Environment, PackageLoader, select_autoescape
from lxml.etree import XMLParser


class BaseEnv(type):
    """Metaclass for state representation

    Implements the Singleton pattern
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(BaseEnv, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class CmdEnv(metaclass=BaseEnv):
    """Runtime state representation.

    One and only one instance of CmdEnv can be instantiated per command call.
    """

    _engine: Environment
    _xml_parser: XMLParser

    def __init__(self):
        self._engine = Environment(
            loader=PackageLoader("ksvg_restyle", "templates"),
            autoescape=select_autoescape(),
        )
        self._xml_parser = XMLParser(
            ns_clean=True,
            remove_blank_text=True,
            resolve_entities=True,
            load_dtd=True,
            huge_tree=True,
        )

    @property
    def xml_parser(self) -> XMLParser:
        """Returns the XML parser instance

        Only one XML parser instance exists within the command call
        and is shared between all modules
        """
        return self._xml_parser

    def render_template(self, name: str, **kwargs) -> str:
        """Renders a Jinja2 template to string representation

        :param name: the name of the template to render
        :param kwargs: context variables provided to the template
        """
        return self._engine.get_template(name).render(**kwargs)


pass_env = make_pass_decorator(CmdEnv, ensure=True)
