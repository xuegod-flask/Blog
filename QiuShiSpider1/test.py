import scrapy


class test1(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()

def myname():
    for i in range(1,10):
        a = test1()
        name = "flask"+str(i)
        a['name'] = name
        yield a
result = myname()
for i in result:
    print(i)