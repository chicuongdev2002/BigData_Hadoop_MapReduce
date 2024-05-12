# BIGDATA
## Web
[LinkWeb](https://books.toscrape.com/)
![image](https://github.com/chicuongdev2002/BigData_Hadoop_MapReduce/assets/124854803/a5947bdd-8bac-4716-98fa-cd1a9262cfdc)
## Hướng dẫn
- Chạy file Python để lấy dữ liệu từ web
```
scrapy runspider SpiderCrawler20020331.py
```
- Chạy MapReducer từ máy ảo
```
ssh hduser@192.168.1.247
```
- Chạy HDFS
```
	start-dfs.sh
	start-yarn.sh
  cd $HADOOP_HOME
```
- Chạy lệnh để sử dụng MapReducer
```
hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.6.5.jar
-files "/home/hduser/mycode/mapper.py,/home/hduser/mycode/reducer.py"
-mapper "python mapper.py"
-reducer "python reducer.py"
-input /mydata/*
-output /myresult/out-res01
```
- Kiểm tra kết qủa
```
hdfs dfs -cat /myresult/out-res01/part-00000
```

