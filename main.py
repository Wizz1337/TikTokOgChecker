from threading import Thread, active_count
from os import name, system as terminal
from string import ascii_letters, digits
from requests import get as GET
from random import choice
from colored import fg
from pystyle import *
PrintAll = True
Checked = 0
Valid = 0
Try = 0

def Banner():
    terminal("cls" if name == "nt" else "clear")
    Banner1 = """
        ______         
     .-'      `-.      
   .'            `.    
  /    14XniT0     \   
 ;      6CATt      ;`  
 |       vda       |;  
 ;      DZ5qW      ;|  
 '\    Xze1D5f    / ;  
  \`.           .' /   
   `.`-._____.-' .'    
     / /`_____.-'      
    / / /              
   / / /
  / / /
  \/_/"""
    Banner2 = """
╔═╗╔═╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
║ ║║ ╦  ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
╚═╝╚═╝  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═"""

    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red, Add.Add(Banner1, Banner2, center=True), 2)) + "\n")

def colorPrint(Content, Available):
    global PrintAll
    if Available:
        print(f"[ {fg(119)}Available {fg(7)}] {Content}\n")
    else:
        if not PrintAll:
            print(f"[ {fg(197)}Not Available {fg(7)}] {Content}")

def CheckUsername(username):
    global Checked, Valid, Try
    Headers = {
        "Host": "www.tiktok.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cookie": "ttwid=1%7CXFixaE7udCkZoTfZMgzyRnlmG0VRmcoRiorI9ieElUU%7C1652384429%7Cb0d3f9da60e07b4f146d3b6f3087d015c20a775c03782da69fa12baf1d0b4093; tt_csrf_token=6gjnlpgP-glzqIKy-wUyyOFv-COJ4ZT6Ua-I; _abck=9484F33F2084F8FABEB33926102A1DCF~-1~YAAQJRYwFxft+I2AAQAAz0TJuQdBBr+letEYpQKCgSKmH5KS8+PbrTYrw3PW/Ixf5gZif0LJ9MxNyVtiPwjHyNadHs9JjGQjtNUcrzJu1Ah16wq0cPjQS94XEmbbJP2sZM2aHd2PEUd2qKiwmrBdA0Gb8jG6d1DrkaXjh4oFzOs3EjdMHaOxdJ/djDpXnNzW7juAtyy6uEZOBZCPpA0gcjmDMEAJkb/6TTwM9Yj8dZs+DmhkBpczd/J0qegmrB+H/Nx8tHd0Cc1bmIVkCy8oyqiNlHzf5khR6Mg/XVaiBMg5GSYIAnmNHk7v+HR9smV5bUkfjT0Kxdy9IYxTzJsw48ZBNCYt5W1nePaDfsYDdYlIfQ+329304Z0ivZl8~-1~-1~-1; ak_bmsc=EE004AEC152DF7224640E7AA7B0749F2~000000000000000000000000000000~YAAQJRYwFxjt+I2AAQAAz0TJuQ90tz+zy/+a5aIED0uG4uqJPuOOzf1jU7s7z9mFtxaq0V3fsf9hJp6G8FMGaoEwYEb++vlG5X+At9UXUbZNFQktKrN8Q8Cl9OhtiKiqegYl4tViM0QR7GanUdtwrKRibAKqQt9Cnv2cE9o9GRmfVMTocWHjk4p8GC303JuiNKXJh9PBy56AI8HDBW5hxSdUIvS6kHCbX1CFwyesv4/Couj62p9RDNhkjOv1uL6FgB16+KHBq3mDLKOZ8nO+1RqbKFWRF6BzDa+HL+ka1O3o0r1NXJRFwpVncxvuXxQ54znsNPvNuiUU924FLT+i89L6VZLAbYfQnU5zsBlRiKhwUgQjInTa+6FhrpJxIudG78w01v5yPjJjcQ==; bm_sz=EE4A7F9158A80ACB32242146334C4A69~YAAQJRYwFxrt+I2AAQAAz0TJuQ/TlC27HHOYl/yotpyLJrk8HfOJdbhnEDlVeQDGCjMOn/RDXaS+ze+hThc+XC8XzdEX+cbIRe5KskXb8/IP5jfvgyXhwYVuLibcIe4KtdFoukl6CAHTNuy2i4rDIazTwj0mRT8pv9XSgSuPVt0FOiJ5Ps+ugZ0MH0TJgHSh3iRHMAjiv3tKT39lufEcpdeRZ2sNs1Zp5oj7VpX43drbzhSk9LAALkqUq3IPNvKRTgWEFgTsUMr8Dwhcr0EvFbE1OWZotEw7NVGs1BOUQ0Yk1Dk=~4534839~3487554; __tea_cache_tokens_1988={%22_type_%22:%22default%22}; csrf_session_id=a3e07f594084c3432e77cc91e9520303; cookie-consent={%22ga%22:false%2C%22af%22:false%2C%22fbp%22:false%2C%22lip%22:false%2C%22bing%22:false%2C%22ttads%22:false%2C%22version%22:%22v7%22}; msToken=VLDAYAxNKTbqyqHu5CUoaknDVWwTSzSpHgB_CsRBj_zGnxEpa2Mq1-RAgbWuFl2oLzVv3itfX4ipXR03BXxdsgLnovCj47nbRvFf1P3thSrqkfYwjgeH85Slvk9LwZUJmQdQ; bm_mi=8E83C1D2DCEBF1F40467AD9C3A60E80B~YAAQJRYwFzbt+I2AAQAAQnHJuQ+I6sE2fJ9cbemYaLBeD7T5ao/BtwHUeWRCaeUKAriT0a8M5qRGjg1hWXVukPfppvXo/CzV1M4baIpIgsP2wqYgxHnK9E+x2rWZFbqWTLxNQE4TBW4m5TCzE0jH0pAqrItNrAqsc0uwdgobKlKLaSl09DXqe39iKUXPx1RxdmSiXeII5vs8L1r5pMyWBZUVx9ePfQxZEu+w0iy4kUeSpitE6tPqC9iWsQfE/iGios543O8Ns2injYAiMA2C/a83Q7vJVgiTwHSHa4uTCr5+oPYYjBU4iDIWGdzXY4nUMw==~1; bm_sv=1EEAC93A20785CFFA93AE7CF99EF8D71~YAAQJRYwFzjt+I2AAQAAQnfJuQ+aDfBhlj/V17EHN2sV5+rMvBFxMzsmWQGFuO2EJKlpT1onS0cTDQ62dAUN+U36XeB39aa+KfYfWudVGFklCco+DADwqJogJ7XsUIKLTsWeKlrr21vjNjeJey9uAowqkvx5BycPT+T1ULgsAHcMHUc8ed036IIQ9hZnakFB5O9l09kovExduPBKNKEDRIR4tW/FzILoBrtC28UTELTeocc3Q7xJ/xKVcL3TQzWi~1; msToken=wqPMkBvY_DbFsbkUBrcRj00pKAUOX5VK0mJGwiCf28wU3_5bRciybfB8KdcuvgVsfolZLl4z00kJDRpX5ArrfsvoUUobXqUm8NAUqmxSSzwtKYv5kXa_RcbG9wOG3J1M2kXK",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }
    sendREQ = GET(f"https://www.tiktok.com/@{username}", headers=Headers)
    if sendREQ.status_code == 404:
        colorPrint(Content=username, Available=True); Valid += 1; Checked += 1
    elif sendREQ.status_code == 200:
        colorPrint(Content=username, Available=False); Checked += 1
    else:
        #print(f"[ - ] An error occured : {sendREQ.text} | {sendREQ.status_code}")
        Try += 1; pass

def UpdateTitle():
    global Checked, Valid, Try
    terminal(f"title Thread : {active_count()} / Checked : {Checked} / Valid : {Valid} / Try : {Try}")

def Start(Threads, Lenght):
    while True:
        Thread(target=UpdateTitle).start()
        username = ''.join(choice(ascii_letters + digits) for i in range(int(Lenght)))
        if (active_count() <= int(Threads)):
            try:
                Thread(target=CheckUsername, args=(username,)).start()
            except:
                pass

if (__name__ == "__main__"):
    Banner(); Ask = True
    while Ask:
        try:
            Threads = Write.Input("Thread Amount [200] : ", Colors.purple_to_red, interval=0.0001)
            Lenght = Write.Input("Name lenght [4] : ", Colors.purple_to_red, interval=0.0001)
            Printing = Write.Input("Print Only Hits [y/n] : ", Colors.purple_to_red, interval=0.0001)
            if Printing.lower().startswith("y"):
                PrintAll = True
            else:
                PrintAll = False
                
            Ask = False
        except:
            pass
    
    Banner(); Start(Threads, Lenght)