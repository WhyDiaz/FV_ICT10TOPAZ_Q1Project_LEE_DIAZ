from pyscript import document, display

def adding_numbers(e):
    document.getElementById('output1').innerHTML = "" # clears previous output
    
    categorybox = document.getElementById('Category').value # get 1st input
    productname = document.getElementById('input2').value # get 2nd input
    stockquantity = document.getElementById('input3').value # get 3rd input
    
    result =  categorybox + "-" + productname + "-" + stockquantity # use operator to combine all the values
    display(result.upper(), target="output1") # display output in div
