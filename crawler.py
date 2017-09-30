from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': 'SelfieImages'})
google_crawler.crawl(keyword='smiling selfies men', max_num=100,
                     date_min=None, date_max=None,
                     min_size=(640,480), max_size=None)
