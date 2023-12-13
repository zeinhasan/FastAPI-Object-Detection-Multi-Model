# Project: FastAPI for Custom Object Detection 

## End-point: [[https://xxxxxx.a.run.app](https://test-deployment-jht5j43saa-uc.a.run.app/predic)](https://test-deployment-jht5j43saa-uc.a.run.app/predict)
### Method: POST
>```
>https://test-deployment-jht5j43saa-uc.a.run.app/predict?image
>```
### Body formdata

|Param|value|Type|
|---|---|---|
|file|Path_to_Image.jpg|file|
|model_name|"Name Model"|Text|

### Name Model
1. apple
2. banana
3. chili
4. pokchoy
5. orange

### Response

```json
{
    "results": [
        {
            "name": "Bok-Choy-Siap-Panen",
            "bounding_box": {
                "x1": 0.0005950927734375,
                "y1": 0.0,
                "x2": 415.91009521484375,
                "y2": 415.9314880371094
            },
            "confidence": 0.9964873790740967
        }
    ],
    "annotated_image":"Image.jpg decoded in latin"
}
```



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
