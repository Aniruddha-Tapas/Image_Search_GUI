from feature_extraction import ColorDescriptor
from searcher import Searcher
import cv2
import time
import wx
import threading


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='Image Search Engine')
        self.panel = wx.Panel(self)
        self.PhotoMaxSize = 500
        self.maxPercent = 100
        self.percent = 0
        self.results = []

        self.createWidgets()

    def createWidgets(self):
        title1 = 'Query Image'
        title2 = 'Search Results'
        instructions = 'Browse for an image'
        # img = wx.EmptyImage(500, 375)
        img = wx.EmptyImage(400, 300)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img))

        img21 = wx.EmptyImage(200, 150)
        self.imageCtrl21 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img21))
        img22 = wx.EmptyImage(200, 150)
        self.imageCtrl22 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img22))
        img23 = wx.EmptyImage(200, 150)
        self.imageCtrl23 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img23))
        img24 = wx.EmptyImage(200, 150)
        self.imageCtrl24 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img24))
        img25 = wx.EmptyImage(200, 150)
        self.imageCtrl25 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img25))
        img26 = wx.EmptyImage(200, 150)
        self.imageCtrl26 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img26))
        img27 = wx.EmptyImage(200, 150)
        self.imageCtrl27 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img27))
        img28 = wx.EmptyImage(200, 150)
        self.imageCtrl28 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img28))
        img29 = wx.EmptyImage(200, 150)
        self.imageCtrl29 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.BitmapFromImage(img29))


        # img20 = wx.EmptyImage(200, 150)
        # self.imageCtrl20 = wx.StaticBitmap(self.panel, wx.ID_ANY,wx.BitmapFromImage(img20))


        instructLbl = wx.StaticText(self.panel, label=instructions)
        title1 = wx.StaticText(self.panel, label=title1)
        title2 = wx.StaticText(self.panel, label=title2)
        title3 = wx.StaticText(self.panel, label='')
        title4 = wx.StaticText(self.panel, label='')

        self.photoTxt = wx.TextCtrl(self.panel, size=(200, -1))

        browseBtn = wx.Button(self.panel, label='Upload')
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)

        self.searchBtn = wx.Button(self.panel, label='Search Images')
        # searchBtn.Bind(wx.EVT_BUTTON, self.searchImages)
        self.searchBtn.Bind(wx.EVT_BUTTON, self.onButton1)
        self.searchBtn.SetEvtHandlerEnabled(False)


        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.btnsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.sizer3 = wx.BoxSizer(wx.VERTICAL)
        self.sizer4 = wx.BoxSizer(wx.VERTICAL)

        #self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY), 0, wx.ALL | wx.EXPAND, 5)
        # self.sizer.Add(wx.StaticLine(self.panel, wx.ID_ANY), 0, wx.ALL | wx.EXPAND, 5)

        self.sizer1.Add(title1, 0, wx.ALL, 5)
        self.sizer1.Add(self.imageCtrl, 0, wx.ALL, 5)

        self.sizer1.Add(instructLbl, 0, wx.ALL, 5)
        self.sizer1.Add(self.photoTxt, 0, wx.ALL, 5)
        self.btnsizer1.Add(browseBtn, 0, wx.ALL, 5)
        self.btnsizer1.Add(self.searchBtn, 0, wx.ALL, 5)
        self.sizer1.Add(self.btnsizer1, 0, wx.ALL, 5)

        self.sizer2.Add(title2, 0, wx.ALL, 5)
        self.sizer2.Add(self.imageCtrl21, 0, wx.ALL, 5)
        self.sizer2.Add(self.imageCtrl24, 0, wx.ALL, 5)
        self.sizer2.Add(self.imageCtrl27, 0, wx.ALL, 5)

        self.sizer3.Add(title3, 0, wx.ALL, 5)
        self.sizer3.Add(self.imageCtrl22, 0, wx.ALL, 5)
        self.sizer3.Add(self.imageCtrl25, 0, wx.ALL, 5)
        self.sizer3.Add(self.imageCtrl28, 0, wx.ALL, 5)

        self.sizer4.Add(title4, 0, wx.ALL, 5)
        self.sizer4.Add(self.imageCtrl23, 0, wx.ALL, 5)
        self.sizer4.Add(self.imageCtrl26, 0, wx.ALL, 5)
        self.sizer4.Add(self.imageCtrl29, 0, wx.ALL, 5)
        # self.sizer3.Add(self.imageCtrl20, 0, wx.ALL, 5)

        # self.mainSizer.Add(self.sizer, 0, wx.ALL, 5)
        self.mainSizer.Add(self.sizer1, 0, wx.ALL, 5)
        self.mainSizer.Add(self.sizer2, 5, wx.ALL, 5)
        self.mainSizer.Add(self.sizer3, 5, wx.ALL, 5)
        self.mainSizer.Add(self.sizer4, 5, wx.ALL, 5)

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)

        self.panel.Layout()

    def onBrowse(self, event):
        """
        Browse for file
        """
        self.percent = 0

        wildcard = "Image files (*.png)|*.png"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()

        self.searchBtn.SetEvtHandlerEnabled(True)


    def onView(self):
        """
        Attempts to load the image and display it
        """
        filepath = self.photoTxt.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)

        """
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()

        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW, NewH)
        print(NewH,NewW)
        """

        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
        self.panel.Refresh()
        self.mainSizer.Fit(self)

    def searchImages(self):
        self.onceUsed = False
        filepath = self.photoTxt.GetValue()

        cd = ColorDescriptor((8, 12, 3))
        query_img = filepath
        print query_img
        query = cv2.imread(query_img)
        features = cd.describe(query)

        # perform the search
        index_filepath = "index.csv"
        dataset_filepath = "dataset"

        searcher = Searcher(index_filepath)
        self.results = searcher.search(features)

        # display the query
        # cv2.imshow("Query", query)

        # loop over the results
        # load the result image and display it

        # result = cv2.imread(dataset_filepath + "/" + resultID)

        result_filepath = dataset_filepath + "/" + self.results [0][1]
        original_img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
        img = original_img.Scale(200, 150)
        self.imageCtrl21.SetBitmap(wx.BitmapFromImage(img))
        self.imageCtrl21.Bind(wx.EVT_LEFT_DOWN, lambda evt, index= 1, score=self.results[0][0], p_img=original_img : self.enlargeImage(evt,index,score, p_img))
        self.panel.Refresh()

        result_filepath = dataset_filepath + "/" + self.results[1][1]
        original_img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
        img = original_img.Scale(200, 150)
        self.imageCtrl22.SetBitmap(wx.BitmapFromImage(img))
        self.imageCtrl22.Bind(wx.EVT_LEFT_DOWN, lambda evt, index= 2, score=self.results[1][0], p_img=original_img : self.enlargeImage(evt, index, score, p_img))
        self.panel.Refresh()

        result_filepath = dataset_filepath + "/" + self.results[2][1]
        original_img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
        img = original_img.Scale(200, 150)
        self.imageCtrl23.SetBitmap(wx.BitmapFromImage(img))
        self.imageCtrl23.Bind(wx.EVT_LEFT_DOWN, lambda evt, index= 3, score=self.results [2][0], p_img=original_img : self.enlargeImage(evt, index, score, p_img))
        self.panel.Refresh()

        result_filepath = dataset_filepath + "/" + self.results [3][1]
        original_img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
        img = original_img.Scale(200, 150)
        self.imageCtrl24.SetBitmap(wx.BitmapFromImage(img))
        self.imageCtrl24.Bind(wx.EVT_LEFT_DOWN, lambda evt, index= 4, score=self.results [3][0], p_img=original_img : self.enlargeImage(evt, index, score, p_img))
        self.panel.Refresh()

        result_filepath = dataset_filepath + "/" + self.results [4][1]
        original_img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
        img = original_img.Scale(200, 150)
        self.imageCtrl25.SetBitmap(wx.BitmapFromImage(img))
        self.imageCtrl25.Bind(wx.EVT_LEFT_DOWN, lambda evt, index= 5, score=self.results [4][0], p_img=original_img : self.enlargeImage(evt, index, score, p_img))
        self.panel.Refresh()

        result_filepath = dataset_filepath + "/" + self.results [5][1]
        original_img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
        img = original_img.Scale(200, 150)
        self.imageCtrl26.SetBitmap(wx.BitmapFromImage(img))
        self.imageCtrl26.Bind(wx.EVT_LEFT_DOWN, lambda evt, index= 6, score=self.results [5][0], p_img=original_img : self.enlargeImage(evt, index, score, p_img))
        self.panel.Refresh()

        result_filepath = dataset_filepath + "/" + self.results [6][1]
        original_img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
        img = original_img.Scale(200, 150)
        self.imageCtrl27.SetBitmap(wx.BitmapFromImage(img))
        self.imageCtrl27.Bind(wx.EVT_LEFT_DOWN, lambda evt, index= 7, score=self.results [6][0], p_img=original_img : self.enlargeImage(evt, index, score, p_img))
        self.panel.Refresh()

        result_filepath = dataset_filepath + "/" + self.results [7][1]
        original_img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
        img = original_img.Scale(200, 150)
        self.imageCtrl28.SetBitmap(wx.BitmapFromImage(img))
        self.imageCtrl28.Bind(wx.EVT_LEFT_DOWN, lambda evt, index= 8, score=self.results [7][0], p_img=original_img : self.enlargeImage(evt, index, score, p_img))
        self.panel.Refresh()

        result_filepath = dataset_filepath + "/" + self.results [8][1]
        original_img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
        img = original_img.Scale(200, 150)
        self.imageCtrl29.SetBitmap(wx.BitmapFromImage(img))
        self.imageCtrl29.Bind(wx.EVT_LEFT_DOWN, lambda evt, index= 9, score=self.results [8][0], p_img=original_img : self.enlargeImage(evt, index, score, p_img))
        self.panel.Refresh()

    def onButton1(self, evt):
        self.StartThread(self.DoWork1)

    def DoWork1(self):
        self.StartThread(self.showProgress)

        taskPercent = 0
        taskPercent += 100
        self.StartThread(self.updateProgress, taskPercent)
        self.searchImages()
        self.searchBtn.SetEvtHandlerEnabled(False)
        self.destoryProgress()

    def StartThread(self, func, *args):
        thread = threading.Thread(target=func, args=args)
        thread.setDaemon(True)
        thread.start()

    def showProgress(self):
        self.progress = wx.ProgressDialog("Processing...", "Searching similiar images in the dataset",
                                          maximum=self.maxPercent, parent=self, style=wx.PD_SMOOTH)

    def destoryProgress(self):
        self.progress.Destroy()


    def updateProgress(self, percent):
        keepGoing = True
        time.sleep(1)
        while keepGoing and self.percent < percent:
            self.percent += 1
            (keepGoing, skip) = self.progress.Update(self.percent)
            time.sleep(0.13)

    def enlargeImage(self,event, index, sim_score,p_image):
        print event
        print index
        print sim_score
        print p_image
        print self.results
        frame = EnlargedImage(self.results)
        sim_score = "{0:.2f}".format(round(sim_score, 2))
        frame.displayImage(index,p_image,sim_score)
        frame.Show()

class EnlargedImage(wx.Frame):
    def __init__(self,res):
        wx.Frame.__init__(self, None, title='Image Viewer')
        self.panel = wx.Panel(self)
        self.dataset_filepath = "dataset"
        self.img_index = 0
        self.curr_score = ""
        self.curr_img = None
        self.curr_results = list(res)
        print self.curr_results

        self.createWidgets()

    def createWidgets(self):
        self.photoTitle = wx.TextCtrl(self.panel, size=(400,-1))
        self.photoTitle.SetEditable(False)
        self.photoTitle.SetCanFocus(False)
        img = wx.EmptyImage(400,300)
        self.imageCtrl = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                         wx.BitmapFromImage(img))
        self.sim_score_text = wx.StaticText(self.panel, label="Similarity Score:")
        self.photoTxt = wx.TextCtrl(self.panel, size=(200,-1))
        self.photoTxt.SetEditable(False)
        self.photoTxt.SetCanFocus(False)
        prevBtn = wx.Button(self.panel, label='<<Previous')
        prevBtn.Bind(wx.EVT_BUTTON, self.onPrev)
        nextBtn = wx.Button(self.panel, label='Next>>')
        nextBtn.Bind(wx.EVT_BUTTON, self.onNext)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.mainSizer.Add(wx.StaticLine(self.panel, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        self.Sizer2.Add(self.photoTitle, 0, wx.ALL, 5)
        self.Sizer2.Add(self.imageCtrl, 0, wx.ALL, 5)
        self.sizer1.Add(self.sim_score_text , 0, wx.ALL, 5)
        self.sizer1.Add(self.photoTxt, 0, wx.ALL, 5)
        self.sizer.Add(prevBtn, 0, wx.ALL, 5)
        self.sizer.Add(nextBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(self.Sizer2, 0, wx.ALL, 5)
        self.mainSizer.Add(self.sizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.mainSizer.Add(self.sizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)

        self.panel.Layout()

    def displayImage(self,index,img,score):
        text= "Search Result "+ str(index)
        self.photoTitle.SetValue(text)
        self.img_index = index
        self.curr_score = score
        self.curr_img = img
        img = img.Scale(400,300)
        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
        self.photoTxt.SetValue(score)
        self.panel.Refresh()


    def onNext(self, event):
        if(self.img_index==1):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[1][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[1][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=2
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==2):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[2][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[2][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=3
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==3):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[3][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[3][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=4
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==4):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[4][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[4][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=5
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==5):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[5][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[5][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=6
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==6):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[6][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[6][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=7
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==7):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[7][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[7][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=8
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==8):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[8][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[8][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=9
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()



    def onPrev(self, event):
        if(self.img_index==2):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[0][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[0][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=1
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==3):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[1][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[1][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=2
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        if(self.img_index==4):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[2][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[2][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=3
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==5):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[3][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[3][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=4
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==6):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[4][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[4][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=5
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        if(self.img_index==7):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[5][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[5][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=6
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==8):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[6][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[6][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=7
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()
        elif(self.img_index==9):
            result_filepath = self.dataset_filepath + "/" + self.curr_results[7][1]
            img = wx.Image(result_filepath, wx.BITMAP_TYPE_ANY)
            img = img.Scale(400,300)
            self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
            sim_score = "{0:.2f}".format(round(self.curr_results[7][0], 2))
            self.photoTxt.SetValue(sim_score)
            self.img_index=8
            text= "Search Result "+ str(self.img_index)
            self.photoTitle.SetValue(text)
            self.panel.Refresh()

if __name__ == '__main__':
    app = wx.App(0)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
