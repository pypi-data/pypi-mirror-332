Annotated burp interfaces for python/jython

# Installation
    pip install dumpserver
    
# Usage 1

    import dumpserver

    class LoggerAddon:
        def request(self, flow: http.HTTPFlow):
            print({flow.request.method} {flow.request.url}")
    
        def response(self, flow: http.HTTPFlow):
            print({flow.response.status_code} {flow.request.url}")
    

# Install Requires

    python>=3.6.0



    