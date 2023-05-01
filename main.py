import wx
import pyperclip


class LoginDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, title="Login")
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.logged_in = False
        self.title = wx.StaticText(self, label="Enter Master Password", pos=(60, 10))
        self.title.SetFont(font)
        self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER, pos=(70, 45))
        self.password.SetSize(150, 25)
        login = wx.Button(self, label='LOGIN', style=wx.BORDER_NONE, pos=(100, 80), size=(80, 30))
        login.SetBackgroundColour(wx.Colour(169, 222, 249))
        login.Bind(wx.EVT_BUTTON, self.onLogin)
        self.SetSize((300, 150))
        self.Show()

    def onLogin(self, event):
        masterPassword = "admin"
        user_password = self.password.GetValue()
        if user_password == masterPassword:
            self.logged_in = True
            self.Close()
        else:
            message = wx.MessageBox('Incorrect password!', 'Error', wx.OK | wx.ICON_ERROR)


class AddData(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        parent.SetSize((400, 380))
        font = wx.Font(23, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        font2 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font3 = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

        # titles
        self.title = wx.StaticText(self, label="PASSWORD KEEPER", pos=(85, 20))
        self.title.SetFont(font)
        self.subTitle = wx.StaticText(self, label="Add new account", pos=(130, 50))
        self.subTitle.SetFont(font2)

        # site name
        self.label_site = wx.StaticText(self, label="Site name:", pos=(30, 120))
        self.label_site.SetFont(font3)
        self.user_site = wx.TextCtrl(self, pos=(130, 120), size=(170, 25))

        # username
        self.label_username = wx.StaticText(self, label="Username:", pos=(30, 170))
        self.label_username.SetFont(font3)
        self.user_user = wx.TextCtrl(self, pos=(130, 170), size=(170, 25))

        # password
        self.label_pass = wx.StaticText(self, label="Password:", pos=(30, 220))
        self.label_pass.SetFont(font3)
        self.user_pass = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER, pos=(130, 220), size=(170, 25))

        # submit
        self.submit = wx.Button(self, label='Submit', style=wx.BORDER_NONE, pos=(90, 280), size=(100, 30))
        self.submit.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.submit.SetFont(font3)
        self.submit.Bind(wx.EVT_BUTTON, self.onSubmit)

        # search
        self.search = wx.Button(self, label='Search', style=wx.BORDER_NONE, pos=(230, 280), size=(100, 30))
        self.search.SetBackgroundColour(wx.Colour(237, 231, 177))
        self.search.SetFont(font3)

    def write(self):
        file = open('data.txt', "a")
        site = self.user_site.GetValue()
        username = self.user_user.GetValue()
        password = self.user_pass.GetValue()

        codedSite = ""
        codedUsername = ""
        codedPassword = ""
        for letter in site:
            if letter == ' ':
                codedSite += ' '
            else:
                codedSite += chr(ord(letter) + 4)

        for letter in username:
            if letter == ' ':
                codedUsername += ' '
            else:
                codedUsername += chr(ord(letter) + 4)

        for letter in password:
            if letter == ' ':
                codedPassword += ' '
            else:
                codedPassword += chr(ord(letter) + 4)

        file.write(codedSite + ',' + codedUsername + ',' + codedPassword + '\n')
        file.close()

    def onSubmit(self, event):
        self.write()
        message = wx.MessageBox('Site: ' + self.user_site.GetValue() + '\nUsername: ' + self.user_user.GetValue() + '\nPassword: ' + self.user_pass.GetValue(), 'Data added successfully', wx.OK | wx.ICON_INFORMATION)
        self.user_site.SetValue("")
        self.user_user.SetValue("")
        self.user_pass.SetValue("")


class SearchData(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        font = wx.Font(23, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        font2 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font3 = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)

        # titles
        self.title = wx.StaticText(self, label="PASSWORD KEEPER", pos=(85, 20))
        self.title.SetFont(font)
        self.subTitle = wx.StaticText(self, label="Search for account data", pos=(105, 50))
        self.subTitle.SetFont(font2)

        # site name
        self.label_site = wx.StaticText(self, label="Enter site name:", pos=(140, 90))
        self.label_site.SetFont(font3)
        self.user_site = wx.TextCtrl(self, pos=(80, 125), size=(230, 25))

        # username
        self.label_username = wx.StaticText(self, label="Username:", pos=(50, 180))
        self.res_username = wx.StaticText(self, label="", pos=(150, 180))
        self.label_username.Hide()

        # password
        self.label_pass = wx.StaticText(self, label="Password:", pos=(50, 230))
        self.res_pass = wx.StaticText(self, label="", pos=(150, 230))
        self.label_pass.Hide()

        #search
        self.search = wx.Button(self, label='Search', style=wx.BORDER_NONE, pos=(90, 280), size=(100, 30))
        self.search.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.search.SetFont(font3)
        self.search.Bind(wx.EVT_BUTTON, self.onSearch)

        # add
        self.add = wx.Button(self, label='Add new', style=wx.BORDER_NONE, pos=(230, 280), size=(100, 30))
        self.add.SetBackgroundColour(wx.Colour(237, 231, 177))
        self.add.SetFont(font3)

        # copy
        img = wx.Image("copy.png", type=wx.BITMAP_TYPE_ANY)
        img = img.Scale(25, 25, wx.IMAGE_QUALITY_HIGH)
        pic = wx.BitmapFromImage(img)

        self.button = wx.BitmapButton(self, -1, pic, style=wx.BORDER_NONE, pos=(315, 225))
        self.Bind(wx.EVT_BUTTON, self.onCopy, self.button)
        self.button.Hide()

    def onSearch(self, event):
        sitename = self.user_site.GetValue()
        uncodedUser = ""
        uncodedPass = ""
        flag = False
        file = open('data.txt', "r")
        for line in file.readlines():
            uncodedSite = ""
            tmp = line.split(',')
            for letter in tmp[0]:
                if letter == ' ':
                    uncodedSite += ' '
                else:
                    uncodedSite += chr(ord(letter) - 4)
            if sitename == uncodedSite:
                flag = True
                self.button.Show()
                self.label_pass.Show()
                self.label_username.Show()
                for letter in tmp[1]:
                    if letter == ' ':
                        uncodedUser += ' '
                    else:
                        uncodedUser += chr(ord(letter) - 4)
                for letter in tmp[2]:
                    if letter == ' ':
                        uncodedPass += ' '
                    else:
                        uncodedPass += chr(ord(letter) - 4)
                self.res_username.SetLabel(uncodedUser)
                self.res_pass.SetLabel(uncodedPass)
        if not flag:
            message = wx.MessageBox('There is no such data', 'Error', wx.OK | wx.ICON_ERROR)
            flag = False
        file.close()

    def onCopy(self, event):
        pyperclip.copy(self.res_pass.GetLabel())
        message = wx.MessageBox('Password copied to clipboard', 'Successfully copied', wx.OK | wx.ICON_INFORMATION)


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="Password keeper")
        self.SetBackgroundColour(wx.Colour(169, 222, 249))
        dlg = LoginDialog()
        dlg.ShowModal()
        authenticated = dlg.logged_in
        if not authenticated:
            self.Close()
        self.Show()

        self.panel1 = AddData(self)
        self.panel2 = SearchData(self)
        self.panel2.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel1, 1, wx.EXPAND)
        self.sizer.Add(self.panel2, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.panel1.search.Bind(wx.EVT_BUTTON, self.onSwitch)
        self.panel2.add.Bind(wx.EVT_BUTTON, self.onSwitch)

    def onSwitch(self, event):
        if self.panel1.IsShown():
            self.panel1.Hide()
            self.panel2.Show()
        else:
            self.panel1.Show()
            self.panel2.Hide()
        self.Layout()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
