import json
from jsonschema import validate, ValidationError

def parseRequest() ->dict:
        schema_path='orderCreationSchema.json'
        file_path='sampleMsg.json' #insert topic name here?
        try:
          with open(schema_path,'r') as schema_json_file:
             orderCreationSchema=json.load(schema_json_file)
          with open(file_path,'r') as request_file:
             orderCreationRequest=json.load(request_file)
          validate(instance=orderCreationRequest, schema=orderCreationSchema)
        except ValidationError as e:
          return (f"Schema validation error {e.message}")
        return orderCreationRequest