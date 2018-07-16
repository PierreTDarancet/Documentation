

class Something:
    """
    This is the doc string for something, here you should explain what this class does.
    Why is this class useful. You can even give examples of how you would use it here.

    Parameters
    ----------
    file_name : A string which is the file name of some file I would like to open.
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def openFile(self):
        """
        This function opens the file that is passed into the class.

        Parameters
        ----------
        None

        Returns
        -------
        A file object.
        """

        return open(self.file_name, 'r')
