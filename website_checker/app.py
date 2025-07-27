print("Website URL Checker.")
url = str(input("\nEnter a website URL.\n"))

if type(url) == str:
    if url.startswith("https"):
        print("This Website uses HTTPS (Secure).")
    elif url.startswith("http"):
        print("This Website uses HTTP (Not Secure).")
    else:
        print("This URL is not valid")
else:
    print("Invalid URL")
