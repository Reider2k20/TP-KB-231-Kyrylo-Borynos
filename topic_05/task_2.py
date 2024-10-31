import requests

def print_cur_n():
    for elem in nbu_orig.json():
        print(elem['cc'], " | ", elem['txt'])

def print_cur_e():
    for elem in nbu_orig.json():
        print(elem['cc'], " | ", elem['rate'])

def conv():
    cur_code = (input("Enter currency code: ")).upper()
    cur_val = float(input("Enter the amount of currency: "))
    try:
        total = cur_val * (nbu[cur_code]["rate"])
        print(f"{total} UAH")
    except:
        print("The currency code is incorrect")

def r_conv():
    cur_code = (input("Enter currency code: ")).upper()
    cur_val = float(input("Enter the amount of UAH: "))
    try:
        total = cur_val / (nbu[cur_code]["rate"])
        print(f"{total} {cur_code}")
    except:
        print("The currency code is incorrect")

def action():
    while True:
        print("\npn — print currency names | pe — print exchange rate | с — conversion | rс — reverse conversion | ex — exit")
        q = input("Select an action: ")
        match q:
            case "pn":
                print_cur_n()
            case "pe":
                print_cur_e()
            case "c":
                conv()
            case "rc":
                r_conv()
            case "ex":
                exit(0)

nbu_orig = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")
nbu = {}
for elem in nbu_orig.json():
    nbu.update({elem['cc'] : elem})

action()