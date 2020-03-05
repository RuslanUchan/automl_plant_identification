# Plant Identification Backend

Sample backend using Cloud Functions and AutoML prediction API

Get training and testing data here: [link-to-dropbox](https://www.dropbox.com/sh/a0gkly9tztjltwe/AAC0qg7tK34sp5epUhAHNXMpa?dl=0)

Explanation:

- `image_to_base64`: convert image test data to base64 to mock AutoML REST API directly (using curl or python script)

- `functions`: accept POST request with `content` field for image data. Process the request using AutoML prediction services, then return prediction result

- `labeling`: script to label plant data
