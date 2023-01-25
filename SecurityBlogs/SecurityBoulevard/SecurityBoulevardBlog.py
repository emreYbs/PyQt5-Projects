#!/usr/bin/env python3
#emreYbs2023

#Notes to people who have visited my simple project repo related to PyQt5 -while I practise with some hobby Pyhon GUI apps-:

#PyQt5 is the latest version of a GUI widgets toolkit developed by Riverbank Computing. 
#It is a Python interface for Qt, one of the most powerful, and popular cross-platform GUI library. 
#PyQt5 is a blend of Python programming language and the Qt library.
#If interested in this lovely Python library, check this:https://www.geeksforgeeks.org/python-introduction-to-pyqt5/

# For infoSec related people, this blog_(https://securityboulevard.com)_ is one of the must to follow resources to keep updated related to current cybersecurity landscape. 


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from bs4 import BeautifulSoup
import requests


class TabWidget(QTabWidget):
    """Set tup the tab and windows layout"""
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)
        self.setWindowTitle("SecurityBoulevard_Blog")
        self.setWindowIcon(QIcon('/home/emre/Downloads/security-boulevard-logo.png'))#ChangeAccordingtoYourUserNameAndPATH
        self.setTabsClosable(True)
        self.tabCloseRequested.connect( self.close_current_tab )
        self.setDocumentMode(True)
        width = 600
        height = 500
        self.setMinimumSize(width, height)
        baseurl = "https://securityboulevard.com/" #Again, indeed a good blog for InfoSec people to keep up with the current cybersecurity related news, threats
        url = QUrl((baseurl))
        reqs = requests.get(baseurl)
        sp = BeautifulSoup(reqs.text, 'html.parser')
        tlt = sp.title.string
        view = HtmlView(self)
        view.load(url)
        ix = self.addTab(view, tlt)
        
    def close_current_tab(self, i):
        if self.count()<2:
            return
        self.removeTab(i)

class HtmlView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        QWebEngineView.__init__(self, *args, **kwargs)
        self.tab = self.parent()
        

    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab:
            webView = HtmlView(self.tab)
            baseurl = "https://securityboulevard.com/"
            reqs = requests.get(baseurl)
            sp = BeautifulSoup(reqs.text, 'html.parser')
            tlt = sp.title.string
            ix = self.tab.addTab(webView, tlt)
            self.tab.setCurrentIndex(ix)
            return webView
        return QWebEngineView.createWindow(self, windowType)

      
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = TabWidget()
    main.show()
    sys.exit(app.exec_())
