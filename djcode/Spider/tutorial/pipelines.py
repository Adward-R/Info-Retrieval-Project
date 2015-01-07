# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class YahooSportsPipeline(object):
    filename = 0

    def __init__(self):
        YahooSportsPipeline.filename += 1

    def process_item(self, item, spider):
        f = file(str(YahooSportsPipeline.filename), "w")
        f.write(item["link"] + "\n")
        for line in item["headline"]:
            f.write(line.encode("utf-8") + "\n")
        for line in item["content"]:
            f.write(line.encode("utf-8") + "\n")
        f.close()
        YahooSportsPipeline.filename += 1
        return item

    def __del__(self):
        YahooSportsPipeline.filename -= 1

class FIFAPipeline(object):
    filename = 0

    def __init__(self):
        FIFAPipeline.filename += 1

    def process_item(self, item, spider):
        f = file(str(FIFAPipeline.filename), "w")
        f.write(item["link"] + "\n")
        for line in item["title"]:
            f.write(line.encode("utf-8") + "\n")
        for line in item["content"]:
            f.write(line.encode("utf-8") + "\n")
        f.close()
        FIFAPipeline.filename += 1
        return item

    def __del__(self):
        FIFAPipeline.filename -= 1
