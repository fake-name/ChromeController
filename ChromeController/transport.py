""" Client for the Google Chrome browser's remote debugging api.

    > a = Shell(host='localhost', port=92222)

    a.tablist has a list of details on open tabs.

    > a.connect(tab=index, updateTabs=True)

    will connect a.soc to the webservice endpoint for tablist[index]'th
    tab.  index is an integer, and updateTabs is True or False. Both tab
    and updateTabs are optional, defaulting to 0 and True respectively.

    At this point a.soc.send and a.soc.recv will synchronously write
    commands and read responses.  The api is semi-asynchronous with
    responses for commands, but also spontaeneous events will be
    send by the browser. For this kind of advance usage, select/pol
    on soc is advised.

    As a convenience, the shell connection object offers a method that, by
    injecting JavaScript into the first tab, commands Chrome to open a URL
    in a new tab::

    a.open_url('http://www.aldaily.com/')

    You can also optionally specify a different tab to operate on.
"""
import json
import requests
import websocket


class Shell(object):
    """A remote debugging connection to Google Chrome.

       > a = Shell(host='localhost', port=92222)

       a.tablist has a list of details on open tabs.

       > a.connect(tab=index, update_tabs=True)

       will connect a.soc to the webservice endpoint for tablist[index]'th
       tab.  index is an integer, and update_tabs is True or False. Both tab
       and updateTabs are optional, defaulting to 0 and True respectively.

       At this point a.soc.send and a.soc.recv will synchronously write
       commands and read responses.  The api is semi-asynchronous with
       responses for commands, but also spontaeneous events will be
       send by the browser. For this kind of advance usage, select/pol
       on soc is advised.  """

    def __init__(self, host='localhost', port=9222):
        """ init """
        self.host = host
        self.port = port
        self.soc = None
        self.tablist = None
        self.find_tabs()

    def connect(self, tab=None, update_tabs=True):
        """Open a websocket connection to remote browser, determined by
           self.host and self.port.  Each tab has it's own websocket
           endpoint - you specify which with the tab parameter, defaulting
           to 0.  The parameter update_tabs, if True, will force a rescan
           of open tabs before connection. """
        if update_tabs or not self.tablist:
            self.find_tabs()
        if not tab:
            tab = 0
        wsurl = self.tablist[tab]['webSocketDebuggerUrl']
        if self.soc.connected:
            self.soc.close()
        self.soc = websocket.create_connection(wsurl)
        return self.soc

    def close(self):
        """ Close websocket connection to remote browser."""
        if self.soc:
            self.soc.close()
            self.soc = None

    def find_tabs(self):
        """Connect to host:port and request list of tabs
             return list of dicts of data about open tabs."""
        # find websocket endpoint
        response = requests.get("http://%s:%s/json" % (self.host, self.port))
        self.tablist = json.loads(response.text)
        return self.tablist

    def open_url(self, url):
        """Open a URL in the oldest tab."""
        if not self.soc or not.self.soc.connected:
            self.connect(tab=0)
        # force the 'oldest' tab to load url
        navcom = json.dumps({"id": 0,
                             "method": "Page.navigate",
                             "params": {"url": url}})
        # This code would open a new window, but browsers really dont
        # like doing so.  And, the results are irritating at best.
        # navcom=json.dumps({"id":0,"method":"Runtime.evaluate",
        #  "params":{"expression": "window.open('%s', #'_blank',
        # 'toolbar=1,scrollbars=1,location=1,statusbar=0,menubar=1,resizable=1'
        # )" % (url) }})
        self.soc.send(navcom)
        return self.soc.recv()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
