#!/usr/bin/env python3

import sys
sys.path.insert(0, 'nbdoc')

from showdoc import ShowDoc

def example_function(param1: str, param2: int = 42, *args, **kwargs):
    """
    This is an example function to test ShowDoc markdown generation.
    
    This function demonstrates how ShowDoc can generate clean markdown
    documentation from numpy-style docstrings.
    
    Parameters
    ----------
    param1 : str
        The first parameter, a string value
    param2 : int, optional
        The second parameter, an integer with default value 42
    *args
        Variable length argument list
    **kwargs
        Arbitrary keyword arguments
        
    Returns
    -------
    str
        A formatted string containing the parameters
        
    Raises
    ------
    ValueError
        If param1 is empty
    """
    if not param1:
        raise ValueError("param1 cannot be empty")
    return f"param1: {param1}, param2: {param2}, args: {args}, kwargs: {kwargs}"

class ExampleClass:
    """
    An example class to test ShowDoc with classes.
    
    This class demonstrates how ShowDoc handles class documentation
    with proper markdown formatting.
    
    Attributes
    ----------
    value : str
        The stored value
    count : int
        A counter value
    """
    
    def __init__(self, value: str):
        """
        Initialize the ExampleClass.
        
        Parameters
        ----------
        value : str
            The initial value to store
        """
        self.value = value
        self.count = 0
    
    def increment(self, amount: int = 1):
        """
        Increment the counter.
        
        Parameters
        ----------
        amount : int, optional
            The amount to increment by, default is 1
            
        Returns
        -------
        int
            The new counter value
        """
        self.count += amount
        return self.count

if __name__ == "__main__":
    print("Testing ShowDoc with markdown output...")
    print("=" * 50)
    
    # Test function documentation
    print("Function Documentation:")
    print("-" * 30)
    func_doc = ShowDoc(example_function, markdown=True)
    print(func_doc.markdown_output)
    
    print("\n" + "=" * 50)
    
    # Test class documentation
    print("Class Documentation:")
    print("-" * 30)
    class_doc = ShowDoc(ExampleClass, markdown=True)
    print(class_doc.markdown_output)
    
    print("\n" + "=" * 50)
    
    # Test method documentation
    print("Method Documentation:")
    print("-" * 30)
    method_doc = ShowDoc(ExampleClass.increment, markdown=True)
    print(method_doc.markdown_output) 