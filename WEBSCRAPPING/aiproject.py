import tkinter as tk
from tkinter import messagebox, ttk
import requests
import webbrowser
from bs4 import BeautifulSoup
import re

def scrape_info_from_website(soup, site):
    price_tags = {
        "vatanbilgisayar.com": soup.find('span', class_='product-list__price'),
        "trendyol.com": soup.find('span', class_='prc-dsc'),
        "amazon.com.tr": soup.find('span', class_='a-price-whole'),
        "hepsiburada.com": soup.find('del', class_='price-old'),
        "akakce.com": soup.find('span', class_='pt_v8'),
        "teknosa.com": soup.find('span', class_='prc')
    }

    stock_tags = {
        "vatanbilgisayar.com": soup.find('button', class_='btn btn-success btn-stock favoriteButton'),
        "trendyol.com": soup.find_all('button', class_='add-to-basket'),
        "amazon.com.tr": soup.find('div', id='availability'),
        "hepsiburada.com": soup.find('div', class_='product-availability'),
        "akakce.com": soup.find('div', class_='product-stock'),
        "teknosa.com": soup.find('button', id='productOutOfStockFromAll')
    }

    price_tag = price_tags.get(site)
    stock_tag = stock_tags.get(site)

    if price_tag:
        price_text = price_tag.text.strip()
        price_text = price_text.replace('TL', '').replace('.', '').replace(',', '.')
        try:
            price = float(price_text)
        except ValueError:
            price = None
    else:
        price = None

    in_stock = True  # Varsayılan olarak stokta kabul edelim

    if site == "trendyol.com" and stock_tag:
        in_stock = not any('sold-out' in tag['class'] for tag in stock_tag)
    elif site == "teknosa.com":
        in_stock = soup.find('button', id='addToCartButton') is not None
    elif site == "vatanbilgisayar.com":
        in_stock = soup.find('button', class_='btn btn-success btn-stock favoriteButton') is None
    elif stock_tag:
        stock_text = stock_tag.text.strip().lower()
        in_stock = not any(keyword in stock_text for keyword in ["yok", "tükendi", "stokta yok", "stok dışı"])

    return price, in_stock

def scrape_price(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"
    headers = {"User-Agent": user_agent}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        messagebox.showerror("Error", f"Error fetching the URL: {response.status_code}")
        return None, None

    soup = BeautifulSoup(response.content, 'html.parser')
    site = get_site_from_url(url)
    
    return scrape_info_from_website(soup, site)

def search_product(query, api_key):
    url = f"https://api.bing.microsoft.com/v7.0/search?q={query}&responseFilter=Webpages&count=40"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        messagebox.showerror("Error", f"Error fetching the search results: {response.status_code}")
        return None

    data = response.json()
    return data

def scrape_product_info(search_results):
    products = []
    if 'webPages' in search_results:
        web_pages = search_results['webPages']['value']
        for page in web_pages:
            name = page['name']
            url = page['url']
            # Teknosa kategori sayfası yerine ürün sayfasını kontrol et
            if "teknosa.com" in url and "/p-" not in url:
                continue
            products.append({'name': name, 'url': url})
    return products

def search_product_gui(event=None):
    query = search_entry.get().strip()
    if query:
        search_results = search_product(query, api_key)
        if search_results:
            products = scrape_product_info(search_results)
            clear_results()
            prices = []
            for product in products:
                price, in_stock = scrape_price(product['url'])
                if price is not None:
                    prices.append(price)
                    stock_status = "In Stock" if in_stock else "Out of Stock"
                    results_tree.insert('', 'end', values=(product['name'], f"{price} TL", stock_status, product['url']))
            
            if prices:
                min_price = min(prices)
                max_price = max(prices)
                average_price = sum(prices) / len(prices)
                min_price_label.config(text=f"Minimum Price: {min_price} TL")
                max_price_label.config(text=f"Maximum Price: {max_price} TL")
                avg_price_label.config(text=f"Average Price: {average_price:.2f} TL")
            else:
                min_price_label.config(text="Minimum Price: N/A")
                max_price_label.config(text="Maximum Price: N/A")
                avg_price_label.config(text="Average Price: N/A")
        else:
            messagebox.showinfo("No Search Results", "No search results found.")

def clear_results():
    for item in results_tree.get_children():
        results_tree.delete(item)
    min_price_label.config(text="Minimum Price: N/A")
    max_price_label.config(text="Maximum Price: N/A")
    avg_price_label.config(text="Average Price: N/A")

def get_site_from_url(url):
    sites = [
        "vatanbilgisayar.com",
        "trendyol.com",
        "amazon.com.tr",
        "hepsiburada.com",
        "akakce.com",
        "teknosa.com"
    ]
    for site in sites:
        if site in url:
            return site
    return None

def open_url(event):
    item = results_tree.selection()[0]
    url = results_tree.item(item, "values")[3]
    webbrowser.open(url)

def main():
    global api_key, results_tree, search_entry, min_price_label, max_price_label, avg_price_label

    api_key = "bbc5a773d22843bcba9c917e4257f10b" #Change your API Key to your IP Key.

    window = tk.Tk()
    window.title("Product Price Scraper")
    window.geometry("900x600")

    frame = tk.Frame(window)
    frame.pack(pady=20)

    search_entry = tk.Entry(frame, width=50)
    search_entry.grid(row=0, column=0, padx=10)

    search_button = tk.Button(frame, text="Search Product", command=search_product_gui)
    search_button.grid(row=0, column=1, padx=10)

    clear_button = tk.Button(frame, text="Clear Results", command=clear_results)
    clear_button.grid(row=0, column=2, padx=10)

    columns = ("Name", "Price", "Stock Status", "URL")
    results_tree = ttk.Treeview(window, columns=columns, show='headings', height=15)
    results_tree.heading("Name", text="Name")
    results_tree.heading("Price", text="Price")
    results_tree.heading("Stock Status", text="Stock Status")
    results_tree.heading("URL", text="URL")
    results_tree.pack(fill=tk.BOTH, expand=True)

    results_tree.bind("<Double-1>", open_url)

    min_price_label = tk.Label(window, text="Minimum Price: N/A")
    min_price_label.pack()

    max_price_label = tk.Label(window, text="Maximum Price: N/A")
    max_price_label.pack()

    avg_price_label = tk.Label(window, text="Average Price: N/A")
    avg_price_label.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
