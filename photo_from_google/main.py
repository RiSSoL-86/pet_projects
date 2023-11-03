from icrawler.builtin import GoogleImageCrawler

def photo_from_google(photo):
    """Ищет 5-ть фото по Вашему запросу."""
    crawler = GoogleImageCrawler()
    crawler.crawl(keyword=photo, max_num=5, overwrite=True)

def main():
    photo = input('Что ищем? Хлопец: ')
    photo_from_google(photo)
    
if __name__ == '__main__':
    main()
