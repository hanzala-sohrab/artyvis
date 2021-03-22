# artyvis

- Artyvis internship task - [Website scraper]

- Scrapes the website https://www.houseofindya.com/ for list of necklace sets under jewelry and corresponding description, price and image urls.

- Main code can be found [here](https://github.com/hanzala-sohrab/artyvis/blob/main/scraper/spiders/necklace_set_spider.py)
    ```python
    import scrapy


    class NecklaceSetSpider(scrapy.Spider):
        name = "necklace_set"
        start_urls = [
            'https://www.houseofindya.com/zyra/necklace-sets/cat'
        ]

        def parse(self, response):
            for items in response.css("div.catgList ul"):
                for item in items.css("li"):
                    yield {
                        'description': item.css("div.catgName p::text").get(),
                        'price': item.css("div.catgName span::text").get()[1:],
                        'image': item.css('img::attr(data-original)').get()
                    }
    ```

## Steps to run the scraper

1. Clone this repo
```shell
git clone https://github.com/hanzala-sohrab/artyvis.git
```
2. Change directory
```shell
cd artyvis
```
3. Run the scraper and store the data in JSON format
```shell
scrapy crawl necklace_set -O necklace_set.json
```
4. Run the scraper and store the data in CSV format
```shell
scrapy crawl necklace_set -O necklace_set.csv
```

**<details><summary><ins>JSON Result</ins></summary>**
```json
[
  {
    "description": "Gold Kundan Green Bead String Earring Necklace Set",
    "price": "2000",
    "image": "https://img.faballey.com/Images/Product/ZNS00049/1.jpg"
  },
  {
    "description": "Gold Kundan Tukdi Earring Necklace Set",
    "price": "2500",
    "image": "https://img.faballey.com/Images/Product/ZNS00007/1.jpg"
  },
  {
    "description": "Gold Maroon Kundan Floral Necklace Set",
    "price": "2250",
    "image": "https://img.faballey.com/Images/Product/ZNS00058/1.jpg"
  },
  {
    "description": "Gold Kundan Blue Bead Earring Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00041/1.jpg"
  },
  {
    "description": "Rose Gold Plated Crystal Necklace Set",
    "price": "2450",
    "image": "https://img.faballey.com/Images/Product/ZNS00064/1.jpg"
  },
  {
    "description": "Gold Kundan Red Drop Meena Earring Necklace Set",
    "price": "2250",
    "image": "https://img.faballey.com/Images/Product/ZNS00054/1.jpg"
  },
  {
    "description": "Blue Bead Kundan Earring Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00050/1.jpg"
  },
  {
    "description": "Gold Red Kundan Bead Earring Necklace Set",
    "price": "1600",
    "image": "https://img.faballey.com/Images/Product/ZNS00003/1.jpg"
  },
  {
    "description": "Gold Kundan Dual Pearl Earring Necklace Set",
    "price": "2000",
    "image": "https://img.faballey.com/Images/Product/ZNS00052/1.jpg"
  },
  {
    "description": "Gold Kundan Blue Bead Pearl Earring Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00042/1.jpg"
  },
  {
    "description": "Gold Green Kundan Bead Drop Earring Necklace Set",
    "price": "3750",
    "image": "https://img.faballey.com/Images/Product/ZNS00018/1.jpg"
  },
  {
    "description": "Gold Textured Contemporary Choker Necklace Set",
    "price": "1100",
    "image": "https://img.faballey.com/Images/Product/ZNS00070/1.jpg"
  },
  {
    "description": "Gold Kundan Green Drop Pearl Earring Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00047/1.jpg"
  },
  {
    "description": "Gold Round Kundan Pearl Earring Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00035/1.jpg"
  },
  {
    "description": "Gold Kundan Mangtika Earring Necklace Set",
    "price": "3500",
    "image": "https://img.faballey.com/Images/Product/ZNS00002/1.jpg"
  },
  {
    "description": "Gold Kundan Aqua Stone Floral Pendant Necklace Set",
    "price": "1475",
    "image": "https://img.faballey.com/Images/Product/ZNS00062/1.jpg"
  },
  {
    "description": "Gold Kundan Cascade Earring Necklace Set",
    "price": "2250",
    "image": "https://img.faballey.com/Images/Product/ZNS00039/1.jpg"
  },
  {
    "description": "White Blue Diamond Drop String Earring Necklace Set",
    "price": "2875",
    "image": "https://img.faballey.com/Images/Product/ZNS00031/1.jpg"
  },
  {
    "description": "Gold Kundan Multi Pearl String Earring Necklace Set",
    "price": "2000",
    "image": "https://img.faballey.com/Images/Product/ZNS00048/1.jpg"
  },
  {
    "description": "Gold Kundan Multicolor Stone Earring Necklace Set",
    "price": "2000",
    "image": "https://img.faballey.com/Images/Product/ZNS00053/1.jpg"
  },
  {
    "description": "White Blue Diamond Earring Pendant Necklace Set",
    "price": "2625",
    "image": "https://img.faballey.com/Images/Product/ZNS00011/1.jpg"
  },
  {
    "description": "Gold Kundan Green Drop Double Orb Earring Necklace Set",
    "price": "2250",
    "image": "https://img.faballey.com/Images/Product/ZNS00038/1.jpg"
  },
  {
    "description": "Dual Gold Kundan Green Bead Earring Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00055/1.jpg"
  },
  {
    "description": "Gold Kundan Pear Dainty Drop Earrings Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00046/1.jpg"
  },
  {
    "description": "Gold Green Kundan Floral Pendant Necklace Set",
    "price": "2100",
    "image": "https://img.faballey.com/Images/Product/ZNS00063/1.jpg"
  },
  {
    "description": "White Diamond Floral Bunch Earring Necklace Set",
    "price": "2750",
    "image": "https://img.faballey.com/Images/Product/ZNS00032/1.jpg"
  },
  {
    "description": "Gold Kundan Earring Pearl String Pendant Necklace Set",
    "price": "1500",
    "image": "https://img.faballey.com/Images/Product/ZNS00008/1.jpg"
  },
  {
    "description": "Gold Kundan Pearl Earring Necklace Set",
    "price": "2375",
    "image": "https://img.faballey.com/Images/Product/ZNS00044/1.jpg"
  },
  {
    "description": "Silver Oxidized Green Stone Star Earring Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00021/1.jpg"
  },
  {
    "description": "Gold Orb Kundan Double Pearl Earrings Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00051/1.jpg"
  },
  {
    "description": "Dual Gold Kundan Pearl Earring Necklace Set",
    "price": "2000",
    "image": "https://img.faballey.com/Images/Product/ZNS00056/1.jpg"
  },
  {
    "description": "Gold Leaf Kundan Double Pearl Earrings Necklace Set",
    "price": "1750",
    "image": "https://img.faballey.com/Images/Product/ZNS00045/1.jpg"
  },
  {
    "description": "White Diamond Aqua Drop Earring Necklace Set",
    "price": "2450",
    "image": "https://img.faballey.com/Images/Product/ZNS00013/1.jpg"
  }
]
```
</details>