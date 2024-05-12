# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymongo
import json
from bson.objectid import ObjectId
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class CSVDBexamsrcPipeline:
    def process_item(self, item, spider):
        '''
        Viết code để xuất ra file csv, thông tin item trên dòng
        mỗi thông tin cách nhau với dấu ,
        Header là: nameX,genreX,typeX,priceexX,priceinX,taxX,avaX,reviewX
        Lưu dữ liệu thành file mang tên csvdataexamsrcX.csv
        '''
        with open('csvdataexamsrc20020331.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([
                item['title20020331'],
                item['genre20020331'],
                item['type20020331'],
                item['priceex20020331'],
                item['pricein20020331'],
                item['tax20020331'],
                item['ava20020331'],
                item['review20020331']
            ])
        return item
    pass
