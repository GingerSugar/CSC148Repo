class Foo:
    """A class foo

    === Attributes ===
    sap: a public integer

    === Representation Invariants ===
    0 <= sap <= 100
    """

    sap: int

    # bar: a private string
    _bar: str

    def __init__(self, sap: int):
        """Initializer for foo class"""
        self.sap = sap
        self._bar = sap / 20
