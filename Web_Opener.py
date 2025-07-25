import webbrowser
from Automation.web_data import websites


def open_Web(webname):
    website_name = webname.lower().split()
    counts = {}
    
    for name in website_name:
        counts[name] = counts.get(name, 0) + 1
    
    urls_to_open = []
    
    for name, count in counts.items():
        if name in websites:
            urls_to_open.extend([websites[name]] * count)
        
    for url in urls_to_open:
            webbrowser.open(url)

    if urls_to_open:
        print("Opening...")
        

    
