#coding=utf8
import urllib2,urllib,json,wx,sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Gui(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u'词典',size=(300,450))
        #panel=wx.Panel(self,-1)
        sizer=wx.BoxSizer(orient=wx.VERTICAL)
        sizer1=wx.BoxSizer(orient=wx.HORIZONTAL)
        self.inputText1=wx.TextCtrl(self,-1,"",style=wx.TE_PROCESS_ENTER)
        button=wx.Button(self,-1,u'查询')
        self.inputText2=wx.TextCtrl(self,-1,'',style=wx.TE_MULTILINE|wx.TE_READONLY)
        sizer1.Add(item=self.inputText1,proportion=1,flag=wx.EXPAND,border=5) 
        sizer1.Add(item=button,proportion=0,flag=wx.EXPAND,border=5)
        sizer.Add(sizer1,0,wx.EXPAND,5)
        sizer.Add(self.inputText2,5,wx.EXPAND,5)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
        self.Bind(wx.EVT_TEXT_ENTER,self.OnClick,self.inputText1)
    
    def OnClick(self,event):
        word=self.inputText1.GetValue()
        #wx.MessageBox(word)
        result=self.search(word)
        if result==0:
            self.inputText2.Value="未找到翻译结果"
            print "未找到翻译结果"
        elif result==1:  #输入为空的情况
            self.inputText2.Value="输入为空"
            print "输入未空"
            # continue
        elif result==2:
            self.inputText2.Value="有错误发生，请检查网络连接"
            print "有错误发生，请检查网络连接"
       
        
    def search(self,content):
        self.inputText2.Clear()
        #print content
        url="http://fanyi.youdao.com/openapi.do"
        parameter=[("keyfrom","myWebsite"),("key","423366321"),("type","data"),("doctype","json"),("version","1.1"),("q",content)]
        try:
            getUrl=url+'?'+urllib.urlencode(parameter)
            req=urllib2.Request(getUrl)
            answer=urllib2.urlopen(req).read()
            locations=json.loads(answer)
            basic=locations["basic"]
            explain=basic["explains"]
            web=locations["web"]  #this is the web part
        except KeyError:
            return 0
        except ValueError:
            return 1
        except:
            return 2
        else:
            self.inputText2.AppendText(u"翻译为："+"\n")
            for i in explain:
                self.inputText2.AppendText("   "+i+"\n")
            
            self.inputText2.AppendText("\n"+"网络释义"+"\n")
            for i in web:
                self.inputText2.AppendText(i["key"]+"      ") 
                for j in i["value"]:
                    self.inputText2.AppendText(j+"  ")
                
                self.inputText2.AppendText("\n\n")
               
    
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=Gui()
    frame.Show()
    app.MainLoop()
