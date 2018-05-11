@classmethod  
def validate_response(cls, schema, resp, body):  
    # Only check the response if the status code is a success code  
    # TODO(cyeoh): Eventually we should be able to verify that a failure  
    # code if it exists is something that we expect. This is explicitly  
    # declared in the V3 API and so we should be able to export this in  
    # the response schema. For now we'll ignore it.  
    if resp.status in HTTP_SUCCESS:  
        cls.expected_success(schema['status_code'], resp.status)  
  
        # Check the body of a response  
        body_schema = schema.get('response_body')  
        if body_schema:  
            try:  
                jsonschema.validate(body, body_schema)  
            except jsonschema.ValidationError as ex:  
                msg = ("HTTP response body is invalid (%s)") % ex  
                raise exceptions.InvalidHTTPResponseBody(msg)  
        else:  
            if body:  
                msg = ("HTTP response body should not exist (%s)") % body  
                raise exceptions.InvalidHTTPResponseBody(msg)  
  
        # Check the header of a response  
        header_schema = schema.get('response_header')  
        if header_schema:  
            try:  
                jsonschema.validate(resp, header_schema)  
            except jsonschema.ValidationError as ex:  
                msg = ("HTTP response header is invalid (%s)") % ex  
                raise exceptions.InvalidHTTPResponseHeader(msg)  