from pyscript import document, display
 
 
def create_order(e):
    math = document.getElementById('math')
    mathprice = float(math.value) * int(math.checked)
 
    ss = document.getElementById('ss')
    ssprice = float(ss.value) * int(ss.checked)
 
    science = document.getElementById('science')
    scienceprice = float(science.value) * int(science.checked)
 
    english = document.getElementById('english')
    englishprice = float(english.value) * int(english.checked)
 
    filipino = document.getElementById('filipino')
    filipinoprice = float(filipino.value) * int(filipino.checked)
 
    ve = document.getElementById('ve')
    veprice = float(ve.value) * int(ve.checked)
 
    ict = document.getElementById('ict')
    ictprice = float(ict.value) * int(ict.checked)
 
    cat = document.getElementById('cat')
    catprice = float(cat.value) * int(cat.checked)
 
    music = document.getElementById('music')
    musicprice = float(music.value) * int(music.checked)
 
    sub = (mathprice + ssprice + scienceprice + englishprice + filipinoprice
           + veprice + ictprice + catprice + musicprice)
    vat = sub * 0.12
    total = sub + vat
 
    document.getElementById("Subtotal").innerHTML = f"₱{sub:.2f}"
    document.getElementById("VAT").innerHTML = f"₱{vat:.2f}"
    document.getElementById("Total_Amount").innerHTML = f"₱{total:.2f}"
 
 
def adding_numbers(e):
    output = document.getElementById('output1')
    output.innerHTML = ""  # clears previous output
 
    categorybox = document.getElementById('Category').value  # get 1st input
    productname = document.getElementById('input2').value.strip()  # get 2nd input
    stockquantity = document.getElementById('input3').value.strip()  # get 3rd input
 
    # basic validation so the SKU is never half-empty
    if categorybox == "0" or productname == "" or stockquantity == "":
        display("Please fill in all three fields.", target="output1")
        return
 
    result = categorybox + "-" + productname + "-" + stockquantity
    display(result.upper(), target="output1")