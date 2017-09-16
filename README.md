image-crawler template for aliyun FunctionCompute
=======
this function service can download all *.jpg file. from privided url.

### Steps:
* [create one log project and log store.](https://help.aliyun.com/document_detail/54604.html)
* [create one buckets](https://promotion.aliyun.com/ntms/act/ossdoclist.html), it will be used to store these pictures
* create one function without trigger. setup function compute service :https://help.aliyun.com/document_detail/51733.html

### How to set up function:
* create local folder: code , and download image_crawler.py into into this folder.
* use fcli client.
```
    >> fcli shell
    >> mks demo
    >> cd demo
    >> mkf image_crawler -h image_crawler.handler -d code -t python2.7
    >> invk crawler_image -s "{\"url\":\"http://www.xxxx.com\"}"
```
