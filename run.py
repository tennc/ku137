from scrapy import cmdline
cmd_str = 'scrapy crawl ku137net -o ku137.csv'
cmdline.execute(cmd_str.split(' '))