
# Functions for formatting values

def FDollar2(DollarValue):

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber2(Value):

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FNumber0(Value):

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FDateShort(InputtedDate):

    InputtedDateStr = InputtedDate.strftime("%Y-%m-%d")

    return InputtedDateStr


def FDateMedium(InputtedDate):

    InputtedDateStr = InputtedDate.strftime("%Y-%m-%d")

    return InputtedDateStr


def FDateLong(InputtedDate):

    InputtedDateStr = InputtedDate.strftime("%d-%b-%y")

    return InputtedDateStr

