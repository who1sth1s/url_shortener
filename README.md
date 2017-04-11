# url_shortener

## Service
- register : register input url to shortener url. but you can't register duplicate url
- access : shortener url redirect to registered url
- stats : show visit count, how many people access shortener url


## Test Case
### Register
- Request : if you don't input url parameter any value, return error and 400 status code
```Json
POST

{
  "url": "http://www.google.co.kr"
}
```
- Response
```Json
Content-type: application/json
Status code: 201 or 200

{
  "url": "http://localhost:3000/1"
}
```
### Access
- Request : if you access invalid url, return error and 400 status code
```Json
GET
http://localhost:3000/1
```
- Response
```
Status code: 301
redirect registered url
```
### Stats
- Request : if you access invalid url, return error and 400 status code
```Json
GET
http://localhost:3000/1/stats
```
- Response
```Json
Content-type: application/json
Status code: 200
{
  "visit": 13
}
```

## Performance test
|    ms    | count |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 |
|:--------:|:-----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|  service |       |    |    |    |    |    |    |    |    |    |    |
| register | case1 | 64 | 42 | 18 | 86 | 16 | 23 | 66 | 19 | 36 | 84 |
|          | case2 |  6 |  7 |  6 |  5 | 13 |  9 |  7 |  8 | 12 |  7 |
|  access  |       | 43 | 25 | 17 | 38 |  8 | 38 | 13 | 28 | 14 | 18 |
|   stats  |       | 49 |  4 |  2 |  2 |  3 |  2 |  8 |  2 |  9 |  2 |

__For accurate http performance test, every test progressed postman__
