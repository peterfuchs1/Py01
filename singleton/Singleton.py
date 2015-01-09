__author__ = 'mdorfinger'

"""
Das Singleton-Pattern sorgt dafür, dass nur eine Instanz der Klasse erstellt wird.
"""


class Singleton():
    """
    In der Init-Methode wird die Instance auf None gestellt, außerdem bekommt man die Klasse die nur einmal Instanziert werden darf.
    """

    def __init__(self, klasse):  # Klasse ist die, die nach dem @Singleton steht
        self.klasse = klasse
        self.instance = None  # beim ersten Aufruf ist die Instance none

    """
    In der Call-Methode wird überprüft, ob die Klasse schon eine Instanz hat.
    Wenn sie noch keine Instanz besitzt, wird eine neue erstellt. Die Instanz wird zurückgegeben.
    """

    def __call__(self):
        if self.instance is None:  # man überprüft beim Aufruf, instance none ist
            self.instance = self.klasse()  # wenn ja, wird eine neue Instanz der Klasse erstellt
        return self.instance  # die instance wird zurückgegeben