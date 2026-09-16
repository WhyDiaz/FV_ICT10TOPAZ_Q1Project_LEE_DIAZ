from pyscript import document, display

def adding_categories(e):
    document.getElementById('output1').innerHTML = "" # clears previous output
    num1 = float(document.getElementById('input1').value) #get 1st input
    num2 = float(document.getElementById('input2').value) #get 2nd input
    result = num1 + num2 # use operator to compute
    display(result, target= "output1") #diplay output in div
