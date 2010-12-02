#! /bin/env python

from FXPy.fox import *

# Default list of observation sites
default_sites = {
    'Bizerte, Tunisia' : 'DTTB',
    'Birmingham, Birmingham Nexrad' : 'KBMX',
    'Huntsville, Huntsville International' : 'KHSV',
    'Auburn-Opelika Airport' : 'KAUO',
    'Atlanta, Hartsfield Atlanta International Airport' : 'KATL'
}

# Dialog for adding new sites to the list
class SiteDialog(FXDialogBox):

    def __init__(self, owner):
        FXDialogBox.__init__(self, owner, 'Add New Site')
        FXMAPFUNC(self, SEL_UPDATE, FXDialogBox.ID_ACCEPT, SiteDialog.onUpdOk)
        frame = FXHorizontalFrame(self, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X)
        FXLabel(frame, None, None, LAYOUT_FILL_X)
        buttons = FXMatrix(frame, 1, PACK_UNIFORM_WIDTH)
        FXButton(buttons, 'OK', None, self, FXDialogBox.ID_ACCEPT)
        FXButton(buttons, 'Cancel', None, self, FXDialogBox.ID_CANCEL)
        FXHorizontalSeparator(self,
            LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|SEPARATOR_GROOVE)
        fields = FXMatrix(self, 2,
            MATRIX_BY_COLUMNS|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        FXLabel(fields, 'Site ID:',
            opts=JUSTIFY_RIGHT|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
        self.metar = FXTextField(fields, 12,
            opts=LAYOUT_FILL_X|LAYOUT_FILL_COLUMN|FRAME_SUNKEN|FRAME_THICK)
        FXLabel(fields, 'Site Description:',
            opts=JUSTIFY_RIGHT|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
        self.description = FXTextField(fields, 12,
            opts=LAYOUT_FILL_X|LAYOUT_FILL_COLUMN|FRAME_SUNKEN|FRAME_THICK)

    # Disable OK button if no text
    def onUpdOk(self, sender, sel, ptr):
        if self.description.getText() and self.metar.getText():
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),NULL)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),NULL)

# Main window class
class WeatherWindow(FXMainWindow):

    ID_GET_REPORT       = FXMainWindow.ID_LAST
    ID_ADD_SITE         = ID_GET_REPORT + 1
    ID_REMOVE_SITE      = ID_ADD_SITE + 1

    def __init__(self, app):
        FXMainWindow.__init__(self, app, 'Weather', w=800, h=600)

        # Register callbacks
        FXMAPFUNC(self, SEL_COMMAND,
            WeatherWindow.ID_GET_REPORT, WeatherWindow.onCmdGetReport)
        FXMAPFUNC(self, SEL_UPDATE,
            WeatherWindow.ID_GET_REPORT, WeatherWindow.onUpdGetReport)
        FXMAPFUNC(self, SEL_COMMAND,
            WeatherWindow.ID_ADD_SITE, WeatherWindow.onCmdAddSite)
        FXMAPFUNC(self, SEL_COMMAND,
            WeatherWindow.ID_REMOVE_SITE, WeatherWindow.onCmdRemoveSite)
        FXMAPFUNC(self, SEL_UPDATE,
            WeatherWindow.ID_REMOVE_SITE, WeatherWindow.onUpdRemoveSite)
        FXMAPFUNC(self, SEL_CLOSE, 0, WeatherWindow.onClose)

        # List of observation sites
        frame = FXPacker(self, LAYOUT_FILL_X)
        buttonframe = FXVerticalFrame(frame,
            LAYOUT_SIDE_TOP|LAYOUT_SIDE_RIGHT|LAYOUT_CENTER_Y)
        buttons = FXVerticalFrame(buttonframe, LAYOUT_FILL_Y)
        FXButton(buttons, 'Add New\nSite...', None, self, self.ID_ADD_SITE,
            FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X)
        FXButton(buttons, 'Remove\nSite', None, self, self.ID_REMOVE_SITE,
            FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X)
        gb = FXGroupBox(frame, 'Sites',
            GROUPBOX_TITLE_LEFT|FRAME_GROOVE|LAYOUT_FILL_X)
        frame = FXVerticalFrame(gb,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.list = FXList(frame, 5, opts=LIST_BROWSESELECT|LAYOUT_FILL_X)

        # Buttons along the bottom
        frame = FXHorizontalFrame(self, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X)
        button = FXButton(frame, 'Get Report', None, self, self.ID_GET_REPORT,
            LAYOUT_CENTER_X|FRAME_RAISED|FRAME_THICK)

        # Report text in the middle
        gb = FXGroupBox(self, 'Report',
            GROUPBOX_TITLE_LEFT|FRAME_GROOVE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        frame = FXVerticalFrame(gb,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.text = FXText(frame,opts=TEXT_READONLY|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # Initialize list of sites
        self.sites = default_sites

    # Enable or disable the "Remove Site" button
    def onUpdRemoveSite(self, sender, sel, ptr):
        if self.list.getCurrentItem() < 0:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),NULL)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),NULL)

    # Remove selected site from the list
    def onCmdRemoveSite(self, sender, sel, ptr):
        key = self.list.getItemText(self.list.getCurrentItem())
        try:
            del self.sites[key]
        except KeyError:
            pass
        self.list.removeItem(self.list.getCurrentItem())

    # Add a new site to the list
    def onCmdAddSite(self, sender, sel, ptr):
        dlg = SiteDialog(self)
        if dlg.execute():
            key = dlg.description.getText()
            siteid = dlg.metar.getText()
            self.sites[key] = siteid
            self.fillSiteList()

    # Enable or disable the "Get Report" button
    def onUpdGetReport(self, sender, sel, ptr):
        if self.list.getCurrentItem() < 0:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),NULL)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),NULL)

    # Grab latest report from the server
    def onCmdGetReport(self, sender, sel, ptr):
        description = self.list.getItemText(self.list.getCurrentItem())
        metar = self.sites[description]
        try:
            data = self.getData(metar)
        except:
            showModalErrorBox(self, MBOX_OK, 'Weather Report',
                "Sorry, couldn't get weather data for\n%s (%s)" % (description, metar))
            return 1
        self.text.setText(data)

    # FTP the data from this server
    def getData(self, metar):
        from ftplib import FTP
        from tempfile import mktemp
        self.getApp().beginWaitCursor()
        filename = mktemp()
        ftp = FTP('weather.noaa.gov')
        ftp.login()
        ftp.cwd('/data/observations/metar/decoded')
        ftp.retrbinary('RETR ' + metar + '.TXT', open(filename, 'w').write)
        ftp.quit()
        self.getApp().endWaitCursor()
        return open(filename, 'r').read()

    # Fill up the list of sites
    def fillSiteList(self):
        self.list.clearItems()
        descriptions = self.sites.keys()
        descriptions.sort()
        for desc in descriptions:
            self.list.appendItem(desc)

    # Read the list of sites from the registry
    def readSiteList(self):
        nsites = self.getApp().reg().readUnsignedEntry('SETTINGS',
            'NumSites', 0)
        if nsites > 0:
            self.sites.clear()
            for sitenum in xrange(nsites):
                desc = self.getApp().reg().readStringEntry('SETTINGS',
                    'SiteDescription%d' % sitenum, '')
                metar = self.getApp().reg().readStringEntry('SETTINGS',
                    'SiteMETAR%d' % sitenum, '')
                if desc and metar:
                    self.sites[desc] = metar

    # Write the list of sites back to the registry
    def writeSiteList(self):
        keys = self.sites.keys()
        self.getApp().reg().writeUnsignedEntry('SETTINGS', 'NumSites',
            len(keys))
        nsites = 0
        for key in keys:
            self.getApp().reg().writeStringEntry('SETTINGS',
                    'SiteDescription%d' % nsites, key)
            self.getApp().reg().writeStringEntry('SETTINGS',
                    'SiteMETAR%d' % nsites, self.sites[key])
            nsites = nsites + 1

    # Save settings before exiting
    def onClose(self, sender, sel, ptr):
        self.writeSiteList()
        self.getApp().exit(0)

    # Create and show the main window
    def create(self):
        FXMainWindow.create(self)
        self.readSiteList()
        self.fillSiteList()
        self.show(PLACEMENT_SCREEN)

def runme():
    app = FXApp('WeatherMan', 'Test')
    import sys
    app.init(sys.argv)
    WeatherWindow(app)
    app.create()
    app.run()

# Main program starts here
if __name__ == '__main__':
    runme()
