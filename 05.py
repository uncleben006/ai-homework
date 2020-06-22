import wx 
import os
import my_frame  


# FileDialog(parent, title, defaultDir="", defaultFile="",
#            wildcard=FileSelectorDefaultWildcardStr, style=FD_DEFAULT_STYLE,
#            pos=DefaultPosition, size=DefaultSize, name=FileDialogNameStr)

class CustomEvent(my_frame.MyFrame): 

    def new( self,event ): 
        self.SetTitle('記事本')
        self.my_rich_text.Clear()
    
    def open( self, event ):
        self.my_rich_text.Clear()
        with wx.FileDialog(
                    self, 
                    "開啟舊檔囉!~", 
                    wildcard="盡量給我文字檔 (*.txt)|*",
                    style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
                ) as fileDialog:
            
            # 如果按了 cancel
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            # 找到檔案路徑，一行一行寫進 rich text
            path = fileDialog.GetPath()
            name = fileDialog.GetFilename()

            self.SetTitle(name)
            
            if os.path.exists(path):
                with open( path , encoding='utf-8' ) as fobj:
                    for line in fobj:
                        self.my_rich_text.WriteText(line)
    
    def save( self, event ):
        try:
            f = open(os.path.join(self.dirname, self.filename), 'w', encoding='utf-8')
            f.write(self.my_rich_text.GetValue())
            f.close()
        except:
            try:
                fileDialog = wx.FileDialog (
                    self, 
                    "儲存檔案囉!~", 
                    ".", "", 
                    wildcard="任何形式唷~|*", 
                    style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
                )
                if (fileDialog.ShowModal() == wx.ID_OK):
                    self.filename = fileDialog.GetFilename()
                    self.dirname = fileDialog.GetDirectory()
                    f = open(os.path.join(self.dirname, self.filename), 'w', encoding='utf-8')
                    f.write(self.my_rich_text.GetValue())
                    f.close()
                    self.SetTitle(self.filename)
                fileDialog.Destroy()
            except:
                pass

    def exit( self, event ):
        self.Destroy()

    def about(self,event):
        wx.MessageBox("作者：王柏元")


def main():        
    app = wx.App() 
    frame = CustomEvent(None) 
    frame.Show() 
    app.MainLoop() 

if __name__ == '__main__':
    main()
