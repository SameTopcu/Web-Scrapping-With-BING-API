
# Product Price Scraper

This project is designed to fetch product prices and stock information from various e-commerce sites. Users can search for a product through a simple interface and view the results. Additionally, users can be redirected to the relevant site by double-clicking on the product links.

## Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Functions](#functions)
- [Contributors](#contributors)

## Overview

This project allows users to compare prices and check stock availability across various sites by searching for a product name. It uses Bing Search API and web scraping techniques to gather data.

## Technologies Used

- **Python**: The main programming language of the project.
- **tkinter**: Library used for the graphical user interface (GUI).
- **requests**: Library used for making HTTP requests.
- **BeautifulSoup**: Library used for parsing HTML and XML data.
- **webbrowser**: Used for directing users to relevant URLs.
- **Bing Search API**: API used for product searches.

## Installation

1. Ensure Python 3.x is installed.
2. Install the required Python libraries:

    ```bash
    pip install requests
    pip install beautifulsoup4
    ```

3. Clone or download the project to your local machine.

4. Obtain your Bing Search API key and insert it into the `api_key` variable in the `aiproject.py` file.

## Usage

1. Run the `aiproject.py` file:

    ```bash
    python aiproject.py
    ```

2. Enter a product name in the search bar and click the "Search Product" button.
3. Product details, prices, and stock statuses will be displayed on the screen.
4. You can be redirected to the relevant site by double-clicking on any product.

## Project Structure

- **apikeytest.py**: Test file used to verify the Bing API key and ensure the API is functioning correctly.
- **aiproject.py**: Main application file. Contains the user interface and functionality.

## Functions

### 1. `test_bing_search(api_key, query)`

- Takes the Bing API key and query to return search results.

### 2. `scrape_info_from_website(soup, site)`

- Processes HTML content to retrieve price and stock information based on the specified site.

### 3. `scrape_price(url)`

- Fetches the product price and stock information from the given URL.

### 4. `search_product(query, api_key)`

- Performs product search through Bing API and returns results.

### 5. `scrape_product_info(search_results)`

- Processes product names and URL information from Bing search results.

### 6. `search_product_gui(event=None)`

- Handles user search queries and displays results in the GUI.

### 7. `clear_results()`

- Clears the search results in the GUI.

### 8. `get_site_from_url(url)`

- Returns the site name based on the given URL.

### 9. `open_url(event)`

- Opens the selected product's URL in the default web browser.

### 10. `main()`

- Initializes the main GUI application and sets up necessary components.

## Contributors

- [Abdül Samed Topcu]

If you have any questions or feedback, please feel free to reach out!

























![image](https://github.com/user-attachments/assets/51187091-32c9-47e2-b872-932742b63e84)

# Product Price Scraper

Bu proje, çeşitli e-ticaret sitelerinden ürünlerin fiyat ve stok bilgilerini çekmek için oluşturulmuştur. Kullanıcı, basit bir arayüz aracılığıyla ürün adını arar ve sonuçları görebilir. Ayrıca, ürün bağlantılarına çift tıklayarak ilgili siteye yönlendirilebilir.

## İçindekiler

- [Genel Bakış](#genel-bakış)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Fonksiyonlar](#fonksiyonlar)
- [Katkıda Bulunanlar](#katkıda-bulunanlar)

## Genel Bakış

Bu proje, kullanıcıların bir ürün adı aratarak çeşitli sitelerdeki fiyatları karşılaştırmasını ve stok durumunu kontrol etmesini sağlar. Proje, Bing Search API ve web scraping tekniklerini kullanarak veri toplamaktadır.

## Kullanılan Teknolojiler

- **Python**: Projenin ana dili.
- **tkinter**: Kullanıcı arayüzü (GUI) için kullanılan kütüphane.
- **requests**: HTTP istekleri yapmak için kullanılan kütüphane.
- **BeautifulSoup**: HTML ve XML verilerini parse etmek için kullanılan kütüphane.
- **webbrowser**: Kullanıcıları ilgili URL'lere yönlendirmek için kullanılır.
- **Bing Search API**: Ürün aramaları yapmak için kullanılan API.

## Kurulum

1. Python 3.x yüklü olduğundan emin olun.
2. Gerekli Python kütüphanelerini yükleyin:

    ```bash
    pip install requests
    pip install beautifulsoup4
    ```

3. Projeyi yerel makinenize klonlayın veya indirin.

4. Bing Search API anahtarınızı alın ve `aiproject.py` dosyasındaki `api_key` değişkenine yerleştirin.

## Kullanım

1. `aiproject.py` dosyasını çalıştırın:

    ```bash
    python aiproject.py
    ```

2. Arama çubuğuna bir ürün adı girin ve "Search Product" butonuna tıklayın.
3. Ürün bilgileri, fiyatlar ve stok durumları ekranda görüntülenecektir.
4. Herhangi bir ürüne çift tıklayarak ilgili siteye yönlendirilebilirsiniz.

## Proje Yapısı

- **apikeytest.py**: Bing API anahtarını kontrol etmek ve API'nin çalıştığından emin olmak için kullanılan test dosyası.
- **aiproject.py**: Ana uygulama dosyası. Kullanıcı arayüzü ve işlevler bu dosyada yer almaktadır.

## Fonksiyonlar

### 1. `test_bing_search(api_key, query)`

- Bing API anahtarını ve sorgusunu alarak arama sonuçlarını döndürür.

### 2. `scrape_info_from_website(soup, site)`

- Belirtilen siteye göre fiyat ve stok bilgilerini almak için HTML içeriğini işler.

### 3. `scrape_price(url)`

- Belirtilen URL'den ürün fiyatını ve stok bilgisini çeker.

### 4. `search_product(query, api_key)`

- Bing API aracılığıyla ürün araması yapar ve sonuçları döndürür.

### 5. `scrape_product_info(search_results)`

- Bing arama sonuçlarından ürün adı ve URL bilgilerini işler.

### 6. `search_product_gui(event=None)`

- Kullanıcının arama sorgusunu işleyen ve sonuçları GUI'de gösteren fonksiyon.

### 7. `clear_results()`

- GUI'deki arama sonuçlarını temizler.

### 8. `get_site_from_url(url)`

- Verilen URL'ye göre site adını döndürür.

### 9. `open_url(event)`

- Kullanıcının seçtiği ürünü varsayılan web tarayıcısında açar.

### 10. `main()`

- Ana GUI uygulamasını başlatan ve gerekli bileşenleri oluşturan fonksiyon.

## Katkıda Bulunanlar

- [Abdül Samed Topcu]

Herhangi bir sorunuz veya geri bildiriminiz varsa, lütfen iletişime geçin!


