from typing import Match


def resolveEqFirstDegree(equation):
    """
    Resolve a mathematical equation of first degree.
    Example of equation: ax +b = 0.
    This function returns x = -b/a as a solution for this equation.
    """
    posX = equation.find('x')
    posEqual =equation.find('=')
    a = equation[0:posX]
    b = equation[posX+1:posEqual]

    x = -int(b)/int(a)

def getFormula(expression):
    """
    Returns an algebra formula for the given expression.
    It returns an empty string if no corresponding formula could be found.
    """
    formula = ""
    exp = expression.replace(" ","") #remove whitespaces from expression

    if exp == "(a+b)²":
        formula = "a²+2ab+b²"
    elif exp == "(a-b)²":
        formula ="a²-2ab+b²"
    elif exp == "(a+b)(a-b)" or exp == "(a-b)(a+b)":
        formula ="a²-b²" 
    elif exp == "(a+b+c)²":
        formula = "a²+b²+c²+2ab+2ac+2bc"

    if formula != "":
        formula = exp + "=" + formula   
    
    return formula  