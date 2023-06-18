import justpy as jp
import definition
import json

# sample: Handle requests at /api?w=word
#127.0.0.1:8000/api?w=moon
#class Api:
#    @classmethod
#    def serve(cls, req):
#        wp = jp.WebPage()
#        word = req.query_params.get('w')
##        jp.Div(a=wp, text=word.title()) # return all page
#        wp.html = word.title() # return only the word
#        return wp
#        
#jp.Route("/api", Api.serve)
#jp.justpy()
        
        
class Api:
    """Handles requests at /api?w=word
    """
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')

        defined = definition.Definition(word).get()

        response = {
            "word":word,
            "definition":defined
        }

        wp.html = json.dumps(response)
        return wp


