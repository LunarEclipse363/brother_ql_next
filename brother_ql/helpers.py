
import logging

logger = logging.getLogger(__name__)

class ElementsManager(object):
    """
    A class managing a collection of 'elements'.
    Those elements are expected to be objects that
    * can be compared for equality against each other
    * have the attribute .identifier
    """
    elements = [] #: list of elements contained by this manager
    element_name = "element" #: what an element is

    def iter_identifiers(self):
        """ Returns an iterator over the identifiers of all the elements in this manager """
        for element in self.elements:
            yield element.identifier

    def iter_elements(self):
        """ Returns an iterator over all the element objects in this manager """
        for element in self.elements:
            yield element

    def identifiers(self):
        """ Returns a list of the identifiers of all the elements in this manager """
        return list(map(lambda e : e.identifier, self.elements))

    def get(self, identifier: str, default=None):
        """
        Returns the element object with the given identifier, or if it doesn't exist, the default value

        :param identifier: the identifier to look for
        :param default: what to return if the given identifier is not found
        """
        return next(filter(lambda l : l.identifier == identifier, self.elements), default)

    def __getitem__(self, key):
        value = next(filter(lambda l : l.identifier == key, self.elements), None)
        if value is not None:
            return value
        else:
            raise KeyError()
