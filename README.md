OpenALPR Web Service
--------------------

This is a simple web service that uses the OpenALPR Python bindings to respond to HTTP requests with license plate data.

Given an HTTP POST request that contains an image file upload (named image), the web service responds with JSON data in the following format:

```
{
  "version": 2,
  "data_type": "alpr_results",
  "epoch_time": 1436708576996,
  "img_width": 600,
  "img_height": 600,
  "processing_time_ms": 124.857529,
  "regions_of_interest": [
    {
      "x": 0,
      "y": 0,
      "width": 600,
      "height": 600
    }
  ],
  "results": [
    {
      "plate": "627WWI",
      "confidence": 89.564888,
      "matches_template": 0,
      "plate_index": 0,
      "region": "",
      "region_confidence": 0,
      "processing_time_ms": 25.04812,
      "requested_topn": 0,
      "coordinates": [
        {
          "x": 238,
          "y": 362
        },
        {
          "x": 363,
          "y": 364
        },
        {
          "x": 363,
          "y": 419
        },
        {
          "x": 237,
          "y": 417
        }
      ],
      "candidates": [
        {
          "plate": "627WWI",
          "confidence": 89.564888,
          "matches_template": 0
        },
        {
          "plate": "627WI",
          "confidence": 84.637611,
          "matches_template": 0
        },
        {
          "plate": "627WNI",
          "confidence": 80.985237,
          "matches_template": 0
        },
        {
          "plate": "G27WWI",
          "confidence": 80.492332,
          "matches_template": 0
        },
        {
          "plate": "6Z7WWI",
          "confidence": 80.17498,
          "matches_template": 0
        },
        {
          "plate": "627WMI",
          "confidence": 80.110176,
          "matches_template": 0
        },
        {
          "plate": "627MWI",
          "confidence": 79.492249,
          "matches_template": 0
        },
        {
          "plate": "627WRI",
          "confidence": 79.323647,
          "matches_template": 0
        },
        {
          "plate": "627WHI",
          "confidence": 79.313904,
          "matches_template": 0
        },
        {
          "plate": "B27WWI",
          "confidence": 79.274544,
          "matches_template": 0
        }
      ]
    }
  ]
}
```