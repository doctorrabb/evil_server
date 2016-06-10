class Payload (object):
    def __init__ (self, listener):
        self.listener = listener

    def run (self):

        from core.design.colors import YES

        results = dict ()

        def detect_os (data):

            if 'User-Agent' in data:
                if 'OS X' in data:
                    results ['OS'] = 'Mac OS X'
                elif 'Linux' in data:
                    results ['OS'] = 'Linux'
                elif 'Windows' in data:
                    results ['OS'] = 'Windows'

        def detect_browser (data):

            if 'User-Agent' in data:
                if 'Chrome' in data:
                    results ['Browser'] = 'Chrome'
                elif 'Firefox' in data:
                    results ['Browser'] = 'Firefox'
                elif 'Safari' in data:
                    results ['Browser'] = 'Safari'
                elif 'Explorer' in data:
                    results ['Browser'] = 'Internet Explorer'
                elif 'Opera' in data:
                    results ['Browser'] = 'Opera'




        for i in self.listener.get_data ().split ('\n'):
            detect_os (i)
            detect_browser (i)

        for i in results:
            print YES + i + ' - ' + results [i]