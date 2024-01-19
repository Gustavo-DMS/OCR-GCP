from google.cloud import vision


client = vision.TextAnnotation()
        response = client.text({
    'image':  {'content': f""},
    'features': [{'type_': vision.Feature.Type.TEXT_DETECTION}],
    })
response_json = vision.AnnotateImageResponse.to_json(response)
print(response_json)
