from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from datetime import date
from datetime import datetime
import os
import itemsInfo
import POS_analytics


class POS_GUI:
    def __init__(self,root):
        self.root = root
        self.root.title("POINT OF SALE SYSTEM")
        self.root.configure(background = "black")
        self.root.grid_rowconfigure(0,weight = 1)
        self.root.grid_columnconfigure(0,weight = 1)
        self.screenWidth, self.screenHeight = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.entryAmount = ""
        self.transaction = []
        self.transactionTotal = 0
        
        self.window = Frame(self.root,width = self.screenWidth, height = self.screenHeight,bg = "white")
        self.window.pack(fill = 'both',expand = True)

        self.createNumberSection()
        self.createTotalsSection()
        self.createTransactionSection()
        self.createItemsSection()
        self.createControlSection()

    def updateEntry(self,newAmount):
        self.amountValue.config(text = newAmount)
        
        

    def createNumberSection(self):
        self.numsFrame = Frame(self.window, width = round(self.screenWidth/5), height = round(0.7*self.screenHeight),
                               bg = "blue",relief = RIDGE,bd=5)
        self.numsFrame.place(x=0,y=0)

        self.buttonsWidth = round(self.screenWidth/15)
        self.buttonsHeight = round(0.21*self.screenHeight)
        self.button1 = Button(self.numsFrame,command = lambda:numsButtonAction(1),text = "1",width = 10,
                              height = 6,bg = "#8787CE",fg = "white")
        self.button1.place(x=0,y=0)

        self.button2 = Button(self.numsFrame, command = lambda:numsButtonAction(2),text = "2", width = 10,
                              height = 6, bg = "#8787CE",fg = "white")
        self.button2.place(x=83,y=0)

        self.button3 = Button(self.numsFrame, command = lambda:numsButtonAction(3), text = "3", width = 10,
                              height = 6, bg = "#8787CE",fg = "white")
        self.button3.place(x=165,y=0)

        self.button4 = Button(self.numsFrame, command = lambda:numsButtonAction(4), text = "4", width = 10,
                              height = 6, bg = "#8787CE",fg = "white")
        self.button4.place(x=0,y=105)

        self.button5 = Button(self.numsFrame, command = lambda:numsButtonAction(5), text = "5", width = 10,
                              height = 6, bg = "#8787CE",fg = "white")
        self.button5.place(x=83,y=105)

        self.button6 = Button(self.numsFrame, command = lambda:numsButtonAction(6), text = "6", width = 10,
                              height = 6, bg = "#8787CE",fg = "white")
        self.button6.place(x=165,y=105)

        self.button7 = Button(self.numsFrame,command = lambda:numsButtonAction(7), text = "7", width = 10,
                              height = 6, bg = "#8787CE",fg = "white")
        self.button7.place(x=0,y=210)

        self.button8 = Button(self.numsFrame, command = lambda:numsButtonAction(8), text = "8", width = 10,
                              height = 6, bg = "#8787CE", fg = "white")
        self.button8.place(x=83,y=210)

        self.button9 = Button(self.numsFrame, command = lambda:numsButtonAction(9), text = "9", width = 10,
                              height = 6, bg = "#8787CE",fg = "white")
        self.button9.place(x=165,y=210)

        self.button0 = Button(self.numsFrame, command = lambda:numsButtonAction(0), text = "0", width = 10,
                              height = 6, bg = "#8787CE",fg = "white")
        self.button0.place(x=0,y = 315)

        self.buttonDecimal = Button(self.numsFrame, command = lambda:numsButtonAction(10),text = ".", width = 10,
                                    height = 6, bg = "#8787CE",fg = "white")
        self.buttonDecimal.place(x=83,y=315)

        self.buttonClear = Button(self.numsFrame, command = lambda:numsButtonAction(11),text = "CLEAR", width = 10,
                                  height = 6 ,bg = "#8787CE",fg = "white")
        self.buttonClear.place(x=165,y=315)

        self.buttonEnter = Button(self.numsFrame, command = lambda:numsButtonAction(12), text = "ENTER", width = 33,
                                  height = 4, bg = "#8787CE", fg = "white")
        self.buttonEnter.place(x=2,y=420)

    def createTotalsSection(self):
        self.totalFrame = Frame(self.window,width = round(self.screenWidth/1.5), height = round(0.2*self.screenHeight),
                                bg = "blue", bd = 5, relief = RIDGE,pady=5,padx = 5)
        self.totalFrame.place(x=0,y=500)

        self.subTotalLabel = Label(self.totalFrame, bg = "#8787CE", fg = "white",bd = 5, relief = RIDGE,text = "SUB-TOTAL: ",
                                   height = 3,width = 20)
        
        self.methodFrame = Frame(self.totalFrame,width = 400,height = 60,bg = "#8787CE",bd=5,relief=RIDGE,pady = 5,padx=5)
        self.methodFrame.place(x=0,y=0)

        methodFont = Font(size = 15)
        
        self.methodLabel = Label(self.methodFrame,text = "METHOD OF PAYMENT: ",bg = "#8787CE", fg = "white", font = methodFont)
        self.methodLabel.place(x=0,y=0)

        methodVariable = StringVar(self.methodFrame)
        methodVariable.set("SELECT METHOD")

        methodDropDown = OptionMenu(self.methodFrame,methodVariable,"SELECT METHOD","CASH")
        methodDropDown.place(x=235,y=0)

        self.amountFrame = Frame(self.totalFrame,width = 400,height = 60,bg = "#8787CE", bd = 5, relief = RIDGE,
                                 pady = 5, padx = 5)
        self.amountFrame.place(x=0,y=68)

        self.amountLabel = Label(self.amountFrame,text = "AMOUNT GIVEN: ", bg = "#8787CE",fg = "white", font = methodFont)
        self.amountLabel.place(x=0,y=0)


        self.amountValue = Label(self.amountFrame)
        self.amountValue.config(bg = "#8787CE", font = methodFont,fg = "white")
        self.amountValue.place(x=200,y=0)

        self.foodTotalFrame = Frame(self.totalFrame, width = 400, height = 60, bg = "#8787CE", bd = 5,
                                    relief = RIDGE, pady = 5, padx = 5)
        self.foodTotalFrame.place(x=420,y=0)

        self.foodTotalLabel = Label(self.foodTotalFrame, text = "TOTAL: ", bg = "#8787CE", fg = "white",font = methodFont)
        self.foodTotalLabel.place(x=0,y=0)

        self.foodTotalValue = Label(self.foodTotalFrame)
        self.foodTotalValue.config(bg = "#8787CE", font = methodFont,fg = "white")
        self.foodTotalValue.place(x=200,y=0)


        self.changeFrame = Frame(self.totalFrame, width = 400, height = 60, bg = "#8787CE", bd = 5,
                                 relief = RIDGE, pady = 5, padx = 5)
        self.changeFrame.place(x=420,y=68)

        self.changeLabel = Label(self.changeFrame, text = "CHANGE: ", bg = "#8787CE", fg = "white", font = methodFont)
        self.changeLabel.place(x=0,y=0)
        self.changeValueLabel = Label(self.changeFrame)
        self.changeValueLabel.config(bg = "#8787CE", font = methodFont, fg = "white")
        self.changeValueLabel.place(x=200,y=0)

    def createTransactionSection(self):
        self.transactionFrame = Frame(self.window, width = round(self.screenWidth/3.5), height = round(0.695*self.screenHeight),
                                      bg = "#F5F5FF", relief = RIDGE, bd = 5)
        self.transactionFrame.place(x=255,y=0)

        self.transactionTable = ttk.Treeview(self.transactionFrame, height = 23, columns = ("ITEM", "QTY", "PRICE"),
                                             show = 'headings')

        self.transactionTable.column("#1", anchor = CENTER, stretch = NO, width = 120)
        self.transactionTable.heading("#1",text = "ITEM")

        self.transactionTable.column("#2", anchor = CENTER, stretch = NO, width = 120)
        self.transactionTable.heading("#2", text = "QTY")

        self.transactionTable.column("#3", anchor = CENTER, stretch = NO, width = 120)
        self.transactionTable.heading("#3", text = "PRICE")

        self.transactionTable.place(x=0,y=0, width = 355)

        scrollbar = ttk.Scrollbar(self.transactionFrame, orient = "vertical", command = self.transactionTable.yview)
        self.transactionTable.configure(yscroll = scrollbar.set)
        scrollbar.place(y=25,x=335,height = 460)

        

    def createItemsSection(self):
        self.activeFrame = "items"
        labelFont = Font(size = 15)
        labelFont2 = Font(size = 20)
        
        self.itemsFrame = Frame(self.window, width = round(self.screenWidth/1.97),height = round(0.695*self.screenHeight),
                                      bg = "blue", relief = RIDGE, bd = 5,padx = 5, pady = 5)
        self.itemsFrame.place(x=621,y=0)

        img = Image.open("img\chaatButtonPic2.png")
        img = img.resize((300,300),Image.ANTIALIAS)
        chaatImg = ImageTk.PhotoImage(img)
        self.chaatButton = Button(self.itemsFrame,width = 180,height = 150,
                                  command = lambda:foodButtonAction(1),relief = RIDGE, bd = 5,bg = "#8787CE",
                                  image = chaatImg)
        self.chaatButton.image = chaatImg
        self.chaatButton.place(x=0,y=0)

        self.chaatLabel = Label(self.itemsFrame,text = "CHAAT",bg = "#8787CE",fg = "white",font = labelFont,
                                width = 16)
        self.chaatLabel.place(x=5,y=128)

        img = Image.open("img/wrapButtonPic.jpg")
        img = img.resize((300,300),Image.ANTIALIAS)
        wrapImg = ImageTk.PhotoImage(img)
        self.wrapButton = Button(self.itemsFrame, width = 180, height = 150,image = wrapImg,
                                 command = lambda:foodButtonAction(2),relief = RIDGE, bd = 5, bg = "#8787CE")
        self.wrapButton.image = wrapImg
        self.wrapButton.place(x=220,y=0)

        self.wrapLabel = Label(self.itemsFrame,text = "WRAP",bg = "#8787CE", fg = "white",font = labelFont,
                               width = 16)
        self.wrapLabel.place(x=225,y=128)

        
        img = Image.open("img/samosaButtonPic.png")
        img = img.resize((180,180),Image.ANTIALIAS)
        samosaImg = ImageTk.PhotoImage(img)
        self.samosaButton = Button(self.itemsFrame, width = 180, height = 150, image = samosaImg,
                                   command = lambda:foodButtonAction(3),relief = RIDGE, bd = 5, bg = "#8787CE")
        self.samosaButton.image = samosaImg
        self.samosaButton.place(x=440,y=0)

        self.samosaLabel = Label(self.itemsFrame,text = "SAMOSA",bg = "#8787CE",fg = "white",font = labelFont,
                                 width = 16)
        self.samosaLabel.place(x=445,y=128)

        img = Image.open("img/pakoraButtonPic.jpg")
        img = img.resize((300,300),Image.ANTIALIAS)
        pakoraImg = ImageTk.PhotoImage(img)
        self.pakoraButton = Button(self.itemsFrame, width = 180, height = 150, image = pakoraImg,
                                   command = lambda:foodButtonAction(4),relief = RIDGE, bd = 5, bg = "#8787CE")
        self.pakoraButton.image = pakoraImg
        self.pakoraButton.place(x=0,y=165)

        self.pakoraLabel = Label(self.itemsFrame,text = "PAKORA",bg = "#8787CE",fg = "white",font = labelFont,
                                 width = 16)
        self.pakoraLabel.place(x=5,y=293)

        img = Image.open("img/choleButtonPic.jpg")
        img = img.resize((180,180),Image.ANTIALIAS)
        choleImg = ImageTk.PhotoImage(img)
        self.choleButton = Button(self.itemsFrame, width = 180, height = 150, image = choleImg,
                                  command = lambda:foodButtonAction(5),relief = RIDGE, bd = 5, bg = "#8787CE")
        self.choleButton.image = choleImg
        self.choleButton.place(x=220,y=165)

        self.choleLabel = Label(self.itemsFrame,text = "CHOLE BHATURE", bg = "#8787CE",fg = "white",font = labelFont,
                                width = 16)
        self.choleLabel.place(x=225,y=293)

        img = Image.open("img/springButtonPic2.jpg")
        img = img.resize((300,300),Image.ANTIALIAS)
        springImg = ImageTk.PhotoImage(img)
        self.springButton = Button(self.itemsFrame,width = 180, height = 150, image = springImg,
                                   command = lambda:foodButtonAction(6),relief = RIDGE, bd = 5, bg = "#8787CE")
        self.springButton.image = springImg
        self.springButton.place(x=440,y=165)

        self.springLabel = Label(self.itemsFrame,text = "SPRING ROLLS", bg = "#8787CE", fg = "white",font = labelFont,
                                 width = 16)
        self.springLabel.place(x=445,y=293)

        img = Image.open("img/gappeButtonPic.jpg")
        img = img.resize((300,300),Image.ANTIALIAS)
        gappeImg = ImageTk.PhotoImage(img)
        self.gappeButton = Button(self.itemsFrame, width = 180, height = 140,text = "GAPPE",image = gappeImg,
                                  font = labelFont,
                                  command = lambda:foodButtonAction(7),relief = RIDGE,bd = 5,bg = "#8787CE",
                                  fg="white")
        self.gappeButton.image = gappeImg
        self.gappeButton.place(x=0,y=330)

        self.gappeLabel = Label(self.itemsFrame,text = "GOL GAPPE", bg = "#8787CE", fg = "white", font = labelFont,
                                width = 16)
        self.gappeLabel.place(x=5,y=448)

        self.sidesButton = Button(self.itemsFrame, width = 25, height = 9,
                                  command = lambda:foodButtonAction(8),relief = RIDGE,bd = 5,bg = "#8787CE",
                                  fg = "white")
        self.sidesButton.place(x=220,y=330)

        self.sidesLabel = Label(self.itemsFrame,width = 10,text = "SIDES", bg = "#8787CE",
                                fg = "white", font = labelFont2)
        self.sidesLabel.place(x=225,y=394)
        
        self.drinksButton = Button(self.itemsFrame,width = 25,height = 9,
                                   command = lambda:foodButtonAction(9),relief = RIDGE,bd = 5,bg = "#8787CE")
        self.drinksButton.place(x=440,y=330)

        self.drinksLabel = Label(self.itemsFrame, width = 11, text = "DRINKS", bg = "#8787CE",fg = "white",
                                 font = labelFont2)
        self.drinksLabel.place(x=445,y=394)

    def createControlSection(self):
        controlFont = Font(size = 14)
        self.controlFrame = Frame(self.window,width = round(self.screenWidth/3.05), height = round(0.2*self.screenHeight),
                                bg = "blue", bd = 5, relief = RIDGE,pady=2,padx = 2)
        self.controlFrame.place(x=851,y=500)
        self.homeButton = Button(self.controlFrame, width = 17, height = 2, command = self.loadHomepage,
                                 relief = RIDGE, bd = 5, bg = "#8787CE", text = "HOME", font = controlFont,fg = "white")
        self.homeButton.place(x=0,y=0)
        
        self.cancelButton = Button(self.controlFrame, width = 17, height = 2, command = self.resetTransaction,
                                   relief = RIDGE, bd = 5, bg = "#8787CE", text = "CANCEL", font = controlFont,fg = "white")
        self.cancelButton.place(x=201,y=0)

        self.completeButton = Button(self.controlFrame, width = 17, height = 2, command = self.completeTransaction,
                                     relief = RIDGE, bd = 5, bg = "#8787CE", text = "DONE", font = controlFont, fg = "white")
        self.completeButton.place(x=0,y=65)

        self.analyticsButton = Button(self.controlFrame, width = 17, height = 2, command = self.createAnalyticsSection,
                                      relief = RIDGE, bd = 5, bg = "#8787CE", text = "ANALYTICS", font = controlFont, fg = "white")
        self.analyticsButton.place(x=201,y=65)

    def createChaatSection(self):
        self.activeFrame = "chaat"
        chaatFont = Font(size = 20)
        self.itemsFrame.place_forget()

        self.chaatFrame = Frame(self.window, width = round(self.screenWidth/1.97),height = round(0.695*self.screenHeight),
                                bg = "blue", relief = RIDGE, bd = 5,padx = 5, pady = 5)
        self.chaatFrame.place(x = 621,y=0)

        self.papdiButton = Button(self.chaatFrame,width = 40,height = 14,command = lambda:chaatButtonAction(1),
                                 relief = RIDGE, bd = 5, bg = "#8787CE")
        self.papdiButton.place(x=0,y=0)
        self.papdiLabel = Label(self.chaatFrame,width = 12, text = "PAPDI CHAAT", bg = "#8787CE",
                                fg = "white", font = chaatFont)
        self.papdiLabel.place(x=45,y=90)

        self.alooButton = Button(self.chaatFrame,width = 40,height = 14, command = lambda:chaatButtonAction(2),
                                 relief = RIDGE, bd = 5, bg = "#8787CE")
        self.alooButton.place(x=335,y=0)

        self.alooLabel = Label(self.chaatFrame,width = 16, text = "ALOO TIKKI CHAAT", bg = "#8787CE",
                               fg = "white", font = chaatFont)
        self.alooLabel.place(x=355,y=80)

        self.samosaChaatButton = Button(self.chaatFrame, width = 40, height = 14, command = lambda:chaatButtonAction(3),
                                        relief = RIDGE, bd = 5, bg = "#8787CE")
        self.samosaChaatButton.place(x=0,y=245)

        self.samosaChaatLabel = Label(self.chaatFrame,width = 13,text = "SAMOSA CHAAT", bg = "#8787CE",
                                       fg = "white",font = chaatFont)
        self.samosaChaatLabel.place(x=40,y=340)

        self.daulatButton = Button(self.chaatFrame, width = 40, height = 14, command = lambda:chaatButtonAction(4),
                                   relief = RIDGE, bd = 5, bg = "#8787CE")
        self.daulatButton.place(x=335,y=245)

        self.daulatLabel = Label(self.chaatFrame, width = 16,text = "DAULAT KI CHAAT",bg = "#8787CE",
                                 fg = "white", font = chaatFont)
        self.daulatLabel.place(x=352,y=340)

    def createWrapSection(self):
        wrapFont = Font(size = 15)
        self.activeFrame = "wrap"
        self.itemsFrame.place_forget()

        self.wrapFrame = Frame(self.window, width = round(self.screenWidth/1.97),height = round(0.695*self.screenHeight),
                                bg = "blue", relief = RIDGE, bd = 5,padx = 5, pady = 5)
        self.wrapFrame.place(x = 621, y = 0)

        self.chickenButton = Button(self.wrapFrame, width = 40,height = 14, command = lambda:wrapButtonAction(1),
                                    relief = RIDGE, bd = 5, bg = "#8787CE")
        self.chickenButton.place(x=0,y=0)

        self.chickenLabel = Label(self.wrapFrame,width = 19, text = "CHICKEN TIKKA WRAP", bg = "#8787CE",
                                  fg = "white", font = wrapFont)
        self.chickenLabel.place(x=40,y=100)

        self.kebabButton = Button(self.wrapFrame, width = 40, height = 14, command = lambda:wrapButtonAction(2),
                                  relief = RIDGE, bd = 5, bg = "#8787CE")
        self.kebabButton.place(x=335,y=0)

        self.kebabLabel = Label(self.wrapFrame, width = 16, text = "KEBAB WRAP",bg = "#8787CE",
                                fg = "white", font = wrapFont)
        self.kebabLabel.place(x=390,y=100)

        self.mixedButton = Button(self.wrapFrame, width = 40, height = 14, command = lambda:wrapButtonAction(3),
                                relief = RIDGE, bd = 5, bg = "#8787CE")
        self.mixedButton.place(x=0,y=250)
        self.mixedLabel = Label(self.wrapFrame,width = 16,text = "MIXED WRAP", bg = "#8787CE",
                                fg = "white", font = wrapFont)
        self.mixedLabel.place(x=52,y=350)

        self.paneerButton = Button(self.wrapFrame, width = 40, height = 14, command = lambda:wrapButtonAction(4),
                                   relief = RIDGE, bd = 5, bg = "#8787CE")
        self.paneerButton.place(x=335,y=250)

        self.paneerLabel = Label(self.wrapFrame, width = 16, text = "PANEER WRAP", bg = "#8787CE",
                                 fg = "white", font = wrapFont)
        self.paneerLabel.place(x=395,y=350)

    
    def createSamosaSection(self):
        samosaFont = Font(size = 20)
        self.activeFrame = "samosa"
        self.itemsFrame.place_forget()

        self.samosaFrame = Frame(self.window, width = round(self.screenWidth/1.97),height = round(0.695*self.screenHeight),
                                 bg = "blue", relief = RIDGE, bd = 5,padx = 5, pady = 5)
        self.samosaFrame.place(x=621,y=0)

        self.meatSamosaButton = Button(self.samosaFrame, width = 88, height = 14, command = lambda:samosaButtonAction(1),
                                       relief = RIDGE, bd = 5, bg = "#8787CE")
        self.meatSamosaButton.place(x=0,y=0)

        self.meatSamosaLabel = Label(self.samosaFrame, width = 16, text = "LAMB SAMOSA", bg = "#8787CE",
                                     fg = "white", font = samosaFont)
        self.meatSamosaLabel.place(x=175,y=100)

        self.vegSamosaButton = Button(self.samosaFrame, width = 88, height = 14, command = lambda:samosaButtonAction(2),
                                      relief = RIDGE, bd = 5, bg = "#8787CE")
        self.vegSamosaButton.place(x=0,y=250)

        self.vegSamosaLabel = Label(self.samosaFrame, width = 16, text = "VEG SAMOSA", bg = "#8787CE",
                                    fg = "white", font = samosaFont)
        self.vegSamosaLabel.place(x=175,y=350)

    def createPakoraSection(self):
        pakoraFont = Font(size = 20)
        self.activeFrame = "pakora"
        self.itemsFrame.place_forget()

        self.pakoraFrame = Frame(self.window, width = round(self.screenWidth/1.97),height = round(0.695*self.screenHeight),
                                 bg = "blue", relief = RIDGE, bd = 5,padx = 5, pady = 5)
        self.pakoraFrame.place(x=621,y=0)

        self.fishPakoraButton = Button(self.pakoraFrame, width = 88, height = 14, command = lambda:pakoraButtonAction(1),
                                       relief = RIDGE, bd = 5, bg = "#8787CE")
        self.fishPakoraButton.place(x=0,y=0)

        self.fishPakoraLabel = Label(self.pakoraFrame, width = 16, text = "FISH PAKORA", bg = "#8787CE",
                                     fg = "white", font = pakoraFont)
        self.fishPakoraLabel.place(x=175,y=100)

        self.vegPakoraButton = Button(self.pakoraFrame, width = 88, height = 14, command = lambda:pakoraButtonAction(2),
                                      relief = RIDGE, bd = 5, bg = "#8787CE")
        self.vegPakoraButton.place(x=0,y=250)

        self.vegPakoraLabel = Label(self.pakoraFrame, width = 16, text = "VEG PAKORA", bg = "#8787CE",
                                    fg = "white", font = pakoraFont)
        self.vegPakoraLabel.place(x=175,y=350)

    def createSidesSection(self):
        self.activeFrame = "sides"
        self.itemsFrame.place_forget()

        sidesFont = Font(size = 15)

        self.sidesFrame = Frame(self.window, width = round(self.screenWidth/1.97),height = round(0.695*self.screenHeight),
                                bg = "blue", relief = RIDGE, bd = 5,padx = 5, pady = 5)
        self.sidesFrame.place(x=621,y=0)

        img = Image.open("img/masalaChipsButtonPic.jpg")
        img = img.resize((250,250),Image.ANTIALIAS)
        chipsImg = ImageTk.PhotoImage(img)

        self.chipsButton = Button(self.sidesFrame, width = 190, height = 220, command = lambda:sidesButtonAction(1),
                                  relief = RIDGE, bd = 5, bg = "#8787CE", image = chipsImg)
        self.chipsButton.image = chipsImg
        self.chipsButton.place(x=0,y=0)

        self.chipsLabel = Label(self.sidesFrame, width = 17, text = "MASALA CHIPS",bg = "#8787CE",
                                fg = "white",font = sidesFont)
        self.chipsLabel.place(x=4,y=198)

        img = Image.open("img/chutneyButtonPic.jpeg")
        img = img.resize((300,300), Image.ANTIALIAS)
        chutneyImg = ImageTk.PhotoImage(img)
        self.chutneyButton = Button(self.sidesFrame, width = 190, height = 220, command = lambda:sidesButtonAction(2),
                                    relief = RIDGE, bd = 5, bg = "#8787CE", image = chutneyImg)
        self.chutneyButton.image = chutneyImg
        self.chutneyButton.place(x=212,y=0)

        self.chutneyLabel = Label(self.sidesFrame, width = 17, text = "CHUTNEY", bg = "#8787CE",
                                  fg = "white", font = sidesFont)
        self.chutneyLabel.place(x=216,y=198)


        img = Image.open("img/mintChutneyButtonPic.jpg")
        img = img.resize((270,270),Image.ANTIALIAS)
        chutneyImg = ImageTk.PhotoImage(img)
        self.mintChutneyButton = Button(self.sidesFrame, width = 190, height = 220, command = lambda:sidesButtonAction(3), image = chutneyImg,
                                        relief = RIDGE, bd = 5, bg = "#8787CE")
        self.mintChutneyButton.image = chutneyImg
        self.mintChutneyButton.place(x=425,y=0)

        self.mintChutneyLabel = Label(self.sidesFrame, width = 17, text = "MINT CHUTNEY", bg = "#8787CE",
                                      fg = "white", font = sidesFont)
        self.mintChutneyLabel.place(x=429,y=198)
        
        img = Image.open("img/raitaButtonPic.jpg")
        img = img.resize((300,300),Image.ANTIALIAS)
        raitaImg = ImageTk.PhotoImage(img)
        self.raitaButton = Button(self.sidesFrame, width = 190, height = 220, command = lambda:sidesButtonAction(4),
                                  image = raitaImg,relief = RIDGE, bd = 5, bg = "#8787CE")
        self.raitaButton.image = raitaImg
        self.raitaButton.place(x=0,y=250)

        self.raitaLabel = Label(self.sidesFrame, width = 17, text = "RAITA", bg = "#8787CE",
                                fg = "white", font = sidesFont)
        self.raitaLabel.place(x=4,y=448)
        
        img = Image.open("img/saladButtonPic.jpg")
        img = img.resize((300,300),Image.ANTIALIAS)
        saladImg = ImageTk.PhotoImage(img)
        self.saladButton = Button(self.sidesFrame, width = 190, height = 220, command = lambda:sidesButtonAction(5),
                                  relief = RIDGE, bd = 5, bg = "#8787CE",image = saladImg)
        self.saladButton.image = saladImg
        self.saladButton.place(x=212,y=250)
        self.saladLabel = Label(self.sidesFrame,width = 17, text = "SALAD", bg = "#8787CE",
                                fg = "white", font = sidesFont)
        self.saladLabel.place(x=216, y = 448)
        

        img = Image.open("img/poppadumsButtonPic.jpg")
        img = img.resize((300,300),Image.ANTIALIAS)
        poppadomsImg = ImageTk.PhotoImage(img)
        self.poppadomsButton = Button(self.sidesFrame, width = 190, height = 220, command = lambda:sidesButtonAction(6),
                                    relief = RIDGE, bd = 5, bg = "#8787CE",image = poppadomsImg)
        self.poppadomsButton.image = poppadomsImg
        self.poppadomsButton.place(x=425,y=250)

        self.poppadomsLabel = Label(self.sidesFrame, width = 17, text = "POPPADOMS", bg = "#8787CE",
                                    fg = "white", font = sidesFont)
        self.poppadomsLabel.place(x=429,y=448)
        
    def createDrinksSection(self):
        self.activeFrame = "drinks"
        drinksFont = Font(size = 15)
        self.itemsFrame.place_forget()

        self.drinksFrame = Frame(self.window, width = round(self.screenWidth/1.97),height = round(0.695*self.screenHeight),
                                 bg = "blue", relief = RIDGE, bd = 5,padx = 5, pady = 5)
        self.drinksFrame.place(x=621,y=0)
        
        img = Image.open("img/cokeButtonPic.jpg")
        img = img.resize((250,300), Image.ANTIALIAS)
        cokeImg = ImageTk.PhotoImage(img)
        self.cokeButton = Button(self.drinksFrame, width = 145, height = 225, command = lambda: drinksButtonAction(1),
                                 relief = RIDGE, bd = 5, bg = "#8787CE",image = cokeImg)
        self.cokeButton.image = cokeImg
        self.cokeButton.place(x=0, y = 0)
        self.cokeLabel = Label(self.drinksFrame, width = 13, text = "COCA-COLA", bg = "#8787CE",
                                fg = "white", font = drinksFont)
        self.cokeLabel.place(x=4, y = 203)

        img = Image.open("img/dietCokeButtonPic.jpg")
        img = img.resize((250,300), Image.ANTIALIAS)
        dietCokeImg = ImageTk.PhotoImage(img)
        self.dietCokeButton = Button(self.drinksFrame, width = 145, height = 225, command = lambda: drinksButtonAction(2),
                                     relief = RIDGE, bd = 5, bg = "#8787CE", image = dietCokeImg)
        self.dietCokeButton.image = dietCokeImg
        self.dietCokeButton.place(x=159,y=0)
        self.dietCokeLabel = Label(self.drinksFrame, width = 13, text = "DIET COKE", bg = "#8787CE",
                                   fg = "white", font = drinksFont)
        self.dietCokeLabel.place(x=163, y = 203)

        img = Image.open("img/limcaButtonPic.jpg")
        img = img.resize((250,250), Image.ANTIALIAS)
        limcaImg = ImageTk.PhotoImage(img)
        self.limcaButton = Button(self.drinksFrame, width = 145, height = 225, command = lambda: drinksButtonAction(3),
                                  relief = RIDGE, bd = 5, bg = "#8787CE", image = limcaImg)
        self.limcaButton.image = limcaImg
        self.limcaButton.place(x=318,y=0)
        self.limcaLabel = Label(self.drinksFrame, width = 13, text = "LIMCA", bg = "#8787CE",
                                fg = "white", font = drinksFont)
        self.limcaLabel.place(x=322, y = 203)

        img = Image.open("img/thumsUpButtonPic.jpg")
        img = img.resize((300,300), Image.ANTIALIAS)
        thumsUpImg = ImageTk.PhotoImage(img)
        self.thumsUpButton = Button(self.drinksFrame, width = 145, height = 225, command = lambda: drinksButtonAction(4),
                                    relief = RIDGE, bd = 5, bg = "#8787CE", image = thumsUpImg)
        self.thumsUpButton.image = thumsUpImg
        self.thumsUpButton.place(x=477,y=0)
        self.thumsUpLabel = Label(self.drinksFrame, width = 13, text = "THUMS UP", bg = "#8787CE",
                                  fg = "white", font = drinksFont)
        self.thumsUpLabel.place(x=481,y=203)

        img = Image.open("img/waterButtonPic.jpg")
        img = img.resize((300,300), Image.ANTIALIAS)
        waterImg = ImageTk.PhotoImage(img)
        self.waterButton = Button(self.drinksFrame, width = 145, height = 225, command = lambda: drinksButtonAction(5),
                                  relief = RIDGE, bd = 5, bg = "#8787CE", image = waterImg)
        self.waterButton.image = waterImg
        self.waterButton.place(x=0,y=240)
        self.waterLabel = Label(self.drinksFrame, width = 13, text = "WATER", bg = "#8787CE",
                                fg = "white", font = drinksFont)
        self.waterLabel.place(x=4,y=443)

        img = Image.open("img/tropicalButtonPic.png")
        img = img.resize((180,240), Image.ANTIALIAS)
        tropicalImg = ImageTk.PhotoImage(img)
        self.tropicalButton = Button(self.drinksFrame, width = 145, height = 225, command = lambda: drinksButtonAction(6),
                                     relief = RIDGE, bd = 5, bg = "#8787CE", image = tropicalImg)
        self.tropicalButton.image = tropicalImg
        self.tropicalButton.place(x=159,y=240)
        self.tropicalLabel = Label(self.drinksFrame, width = 13, text = "JUICE", bg = "#8787CE",
                                   fg = "white", font = drinksFont)
        self.tropicalLabel.place(x= 163, y = 443)

        img = Image.open("img/chaiButtonPic.jpg")
        img = img.resize((250,250), Image.ANTIALIAS)
        chaiImg = ImageTk.PhotoImage(img)
        self.chaiButton = Button(self.drinksFrame, width = 145, height = 225, command = lambda: drinksButtonAction(7),
                                 relief = RIDGE, bd = 5, bg = "#8787CE", image = chaiImg)
        self.chaiButton.image = chaiImg
        self.chaiButton.place(x=318,y=240)
        self.chaiLabel = Label(self.drinksFrame, width = 13, text = "CHAI", bg = "#8787CE",
                               fg = "white", font = drinksFont)
        self.chaiLabel.place(x=322, y = 443)

        img = Image.open("img/lassiButtonPic.jpg")
        img = img.resize((250,250), Image.ANTIALIAS)
        lassiImg = ImageTk.PhotoImage(img)
        self.lassiButton = Button(self.drinksFrame, width = 145, height = 225, command = lambda: drinksButtonAction(8),
                                  relief = RIDGE, bd = 5, bg = "#8787CE", image = lassiImg)
        self.lassiButton.image = lassiImg
        self.lassiButton.place(x=477,y=240)
        self.lassiLabel = Label(self.drinksFrame, width = 13, text = "LASSI", bg = "#8787CE",
                                fg = "white", font = drinksFont)
        self.lassiLabel.place(x=481,y=443)

    def createChaiSection(self):
        self.activeFrame = "chai"
        chaiFont = Font(size = 20)
        self.itemsFrame.place_forget()
        self.drinksFrame.place_forget()

        self.chaiFrame = Frame(self.window, width = round(self.screenWidth/1.97),height = round(0.695*self.screenHeight),
                                 bg = "blue", relief = RIDGE, bd = 5,padx = 5, pady = 5)
        self.chaiFrame.place(x=621,y=0)

        self.masalaChaiButton = Button(self.chaiFrame, width = 88, height = 15, command = lambda: chaiButtonAction(1),
                                       relief = RIDGE, bd = 5, bg = "#8787CE")
        self.masalaChaiButton.place(x=0,y=0)
        self.masalaLabel = Label(self.chaiFrame, width = 13, text = "MASALA CHAI", bg = "#8787CE",
                                 fg = "white", font = chaiFont)
        self.masalaLabel.place(x=200,y=100)

        self.karakButton = Button(self.chaiFrame, width = 88, height = 15, command = lambda:chaiButtonAction(2),
                                  relief = RIDGE, bd = 5, bg = "#8787CE")
        self.karakButton.place(x=0,y=242)
        self.karakLabel = Label(self.chaiFrame, width = 13, text = "KARAK CHAI", bg = "#8787CE",
                                fg = "white", font = chaiFont)
        self.karakLabel.place(x=200,y=350)

    def updateTransactionTable(self, itemName):
        currentInfo = itemsInfo.linearSearchCurrentItems(itemName, "itemDict")
        database = sqlite3.connect("POS_DATABASE.db")
        c = database.cursor()
        c.execute('''SELECT ProductPrice FROM Products WHERE ProductName = ?''',(itemName,))
        retrievedPrice = float(c.fetchall()[0][0])
        print(retrievedPrice)
        if currentInfo == -1:
            newRecord = {"itemName":itemName, "quantity":1,"transactionPrice":retrievedPrice}
            print("NEW RECORD")
            print(newRecord)
            itemsInfo.currentItemsInfo.append(newRecord)
            self.transactionTable.insert("",'end',values = (newRecord['itemName'],newRecord['quantity'],
                                                            newRecord['transactionPrice']))
            print("CURRENT ITEMS INFO")
            print(itemsInfo.currentItemsInfo)
            self.transactionTotal = round((self.transactionTotal + newRecord['transactionPrice']),2)
            self.foodTotalValue.config(text = self.transactionTotal)
        else:
            itemsInfo.updateItemsInfoQty(itemName)
            itemsInfo.updateTransactionPrice(itemName)
            self.transactionTotal = round((self.transactionTotal + retrievedPrice), 2)
            self.foodTotalValue.config(text = self.transactionTotal)
            self.clearTransactionTable()
            for item in itemsInfo.currentItemsInfo:
                self.transactionTable.insert("",'end',values = (item['itemName'],item['quantity'],item['transactionPrice']))
            
            
    def clearTransactionTable(self):
        for item in self.transactionTable.get_children():
            self.transactionTable.delete(item)

    def loadHomepage(self):
        if self.activeFrame == "chaat":   
            self.chaatFrame.place_forget()
        elif self.activeFrame == "wrap":
            self.wrapFrame.place_forget()
        elif self.activeFrame == "samosa":
            self.samosaFrame.place_forget()
        elif self.activeFrame == "pakora":
            self.pakoraFrame.place_forget()
        elif self.activeFrame == "sides":
            self.sidesFrame.place_forget()
        elif self.activeFrame == "drinks":
            self.drinksFrame.place_forget()
        elif self.activeFrame == "chai":
            self.chaiFrame.place_forget()
        elif self.activeFrame == "analytics":
            self.analyticsFrame.place_forget()

        self.itemsFrame.place(x=621,y=0)
        self.numsFrame.place(x=0,y=0)
        self.totalFrame.place(x=0,y=500)
        self.controlFrame.place(x=851,y=500)
        self.transactionFrame.place(x=255,y=0)

    def resetTransaction(self):
        self.clearTransactionTable()
        itemsInfo.currentItemsInfo = []
        self.entryAmount = ""
        self.transactionTotal = 0
        self.amountValue.config(text = "")
        self.foodTotalValue.config(text = "")
        self.changeValueLabel.config(text = "")

    def updateTransactionsID(self):
        database = sqlite3.connect("POS_DATABASE.db")
        c = database.cursor()

        c.execute('''SELECT MAX(TransactionID) FROM Transactions''')
        results = c.fetchone()
        if results[0] is None:
            return "TRANS00001"
        else:
            numPart = int(results[0][5:])
            numPart += 1
            numPart = str(numPart)
            while len(numPart) != 5:
                numPart = "0" + numPart
            return "TRANS"+numPart

    def updateReceiptName(self):
        database = sqlite3.connect("POS_DATABASE.db")
        c = database.cursor()
        c.execute('''SELECT MAX(ReceiptFile) FROM Transactions''')
        results = c.fetchone()
        print(results)
        if results[0] is None:
            return "receipt00001"
        else:
            numPart = int(results[0][7:])
            numPart += 1
            numPart = str(numPart)
            while len(numPart) != 5:
                numPart = "0" + numPart
            return "receipt"+numPart
        
        

    def completeTransaction(self):
        if self.entryAmount == "":
            messagebox.showinfo(title = "PLEASE ENTER AMOUNT OF CASH GIVEN", message = "You cannot proceed until you enter the exact amount given by the customer in order to calculate and record the correct change") 
        else:
            database = sqlite3.connect("POS_DATABASE.db")
            c = database.cursor()
            receiptName = self.updateReceiptName()
            transID = self.updateTransactionsID()
            f = open(receiptName+".txt","w+")
            f.write("|\t\tITEM\t\t|\tQTY\t|\tPRICE\t\t|\n")
            todayDate = date.today()
            todayTime = datetime.now().strftime("%H:%M:%S")
            c.execute('''INSERT INTO Transactions VALUES (?,?,?,?)''',(transID,receiptName,todayDate,todayTime,))

            for item in itemsInfo.currentItemsInfo:
                c.execute('''SELECT * FROM Products WHERE ProductName = ?''',(item['itemName'],))
                prodInfo = c.fetchall()[0]
                itemSpaces = prodInfo[3] 
                line = "|"+item['itemName']
                for i in range(int(itemSpaces)):
                    line = line + "\t"
                line = line + "|\t" + str(item['quantity']) + "\t|\t" + str(item['transactionPrice'])+"\t\t|"
                f.write(line)
                f.write("\n")
                c.execute('''INSERT INTO Transaction_Products VALUES (?,?,?,?)''',(transID,prodInfo[0],item['quantity'],item['transactionPrice'],))

            f.write(" ----------------------------------------------------- \n")
            f.write("TOTAL: £" + str(self.transactionTotal) + "\n")
            f.write("AMOUNT GIVEN: £" + str(self.entryAmount) + "\n")
            changeAmount = round((float(self.entryAmount) - float(self.transactionTotal)),2)
            f.write("CHANGE: £" + str(changeAmount) + "\n")
            f.close()
            
            database.commit()
            database.close()

            changeAmount = float(self.entryAmount) - self.transactionTotal
            self.changeValueLabel.config(text = round(changeAmount,2))

            messagebox.showinfo(title = "TRANSACTION CONFIRMED",
                                message = "This transaction has been processed and a receipt has been generated. Press OK to continue")

            self.resetTransaction()

    def createAnalyticsSection(self):
        self.itemsFrame.place_forget()
        self.numsFrame.place_forget()
        self.totalFrame.place_forget()
        self.controlFrame.place_forget()
        self.transactionFrame.place_forget()

        titleFont = Font(size = 35)
        resultsTitleFont = Font(size = 20)

        self.analyticsFrame = Frame(self.window,height = self.screenHeight, width = self.screenWidth,bg = "blue")
        self.analyticsFrame.place(x=0,y=0)

        self.activeFrame = "analytics"

        self.analyticsTitleLabel = Label(self.analyticsFrame,text = "ANALYTICS", bg = "blue",fg = "white",
                                         font = titleFont)
        self.analyticsTitleLabel.place(x=525,y=25)

        img = Image.open("img/homeButtonPic.png")
        img = img.resize((100,100),Image.ANTIALIAS)
        homeImg = ImageTk.PhotoImage(img)
        self.analyticsHomeButton = Button(self.analyticsFrame,height = 100,width = 100,image = homeImg,
                                          command = self.loadHomepage,bg = "blue", bd = 5, relief = RIDGE)
        self.analyticsHomeButton.image = homeImg
        self.analyticsHomeButton.place(x=0,y=0)

        self.analyticsFilterFrame = Frame(self.analyticsFrame, height = 535,width = 300, bg = "blue", bd = 5,
                                          relief = RIDGE)
        self.analyticsFilterFrame.place(x=0,y=110)

        self.analyticsResultsCanvas = Canvas(self.analyticsFrame, height = 1000,width=965, bg = "blue", bd = 5,
                                           relief = RIDGE)
                
        self.analyticsResultsCanvas.place(x=300,y=110)

        

        self.analyticsResultsLabel = Label(self.analyticsResultsCanvas, text = "RESULTS WINDOW",bg = "blue",
                                           fg = "white", font=resultsTitleFont)
        self.analyticsResultsLabel.place(x=10,y=10)



        self.selectionFrame1 = Frame(self.analyticsFilterFrame,height = 520,width = 290, bg = "blue",padx = 5, pady = 5)
        self.selectionFrame1.place(x=0,y=0)

        self.individualQueriesButton = Button(self.selectionFrame1, height = 4, width = 35, bg = "#8787CE",bd = 5,
                                              relief = RIDGE,text = "PRODUCT PERFORMANCE",fg = "white",
                                              command = self.loadIndividualQueriesFilter)
        self.individualQueriesButton.place(x=5,y=10)

        self.pastReceiptsButton = Button(self.selectionFrame1, height = 4, width = 35, bg = "#8787CE", bd = 5,
                                         relief = RIDGE, text = "PAST RECEIPTS",fg = "white",command = self.loadReceiptFilter)
        self.pastReceiptsButton.place(x=5,y=100)

    def loadIndividualQueriesFilter(self):
        searchByOptionsFont = Font(size=12)
        labelFont = Font(size = 18)
        self.selectionFrame1.place_forget()
        self.individualQueriesFilter = Frame(self.analyticsFilterFrame, height = 520, width = 290, bg = "blue",
                                             padx=5,pady=5)
        self.individualQueriesFilter.place(x=0,y=0)


        self.searchByLabel = Label(self.individualQueriesFilter, bg = "blue", fg = "white", text = "SEARCH BY",
                                   font = labelFont)
        self.searchByLabel.place(x=65,y=5)
                                   
        self.searchByOptions = Listbox(self.individualQueriesFilter, selectmode = "multiple",bg = "#8787CE",fg = "white",
                                       bd = 5, relief = RIDGE,height = 2,width = 30,font = searchByOptionsFont, exportselection = 0)
        searchOptions = ["Revenue","Units Sold"]
        self.searchByOptions.place(x=0,y=50)

        self.searchForLabel = Label(self.individualQueriesFilter, bg = "blue", fg = "white", text = "SEARCH FOR",
                                    font = labelFont)
        self.searchForLabel.place(x=60, y = 120)
        
        for option in searchOptions:
            self.searchByOptions.insert(END,option)


        self.searchForOptions = Listbox(self.individualQueriesFilter, selectmode = "multiple",bg = "#8787CE",
                                        fg = "white", bd = 5, relief = RIDGE, height = 7,width = 30,
                                        font = searchByOptionsFont, exportselection = 0)

        
        itemsOptions = []
        database = sqlite3.connect("POS_DATABASE.db")
        c = database.cursor()
        c.execute('''SELECT ProductName FROM Products''')
        productNames = c.fetchall()
        for name in productNames:
            itemsOptions.append(name[0])

        searchForScrollbar = ttk.Scrollbar(self.individualQueriesFilter, orient = "vertical",
                                           command = self.searchForOptions.yview)
        self.searchForOptions.configure(yscroll = searchForScrollbar.set)
        searchForScrollbar.place(x=260,y=169,height = 135)
        
                
        self.searchForOptions.place(x=0,y=165)

        self.timePeriodLabel = Label(self.individualQueriesFilter, bg = "blue", fg = "white", text = "TIME PERIOD",
                                     font = labelFont)
        self.timePeriodLabel.place(x=61,y=315)
        
        for option in itemsOptions:
            self.searchForOptions.insert(END,option)

        self.timePeriodOptions = Listbox(self.individualQueriesFilter, bg = "#8787CE",
                                         fg = "white", bd = 5, relief = RIDGE, width = 30, font = searchByOptionsFont,
                                         height = 4, exportselection = 0)

        timePeriodOptions = ["7 Days", "1 Month", "3 Months", "6 Months", "1 Year", "3 Year", "All-Time"]
        
        self.timePeriodOptions.place(x=0,y=360)

        timePeriodScrollbar = ttk.Scrollbar(self.individualQueriesFilter, orient = "vertical",
                                            command = self.timePeriodOptions.yview)
        self.timePeriodOptions.configure(yscroll = timePeriodScrollbar.set)
        timePeriodScrollbar.place(x=260,y=365,height = 77)
        
        for option in timePeriodOptions:
            self.timePeriodOptions.insert(END,option)

        self.confirmIndividualChoiceButton = Button(self.individualQueriesFilter,height = 2,width = 20,bg = "#8787CE", bd = 5,
                                                    relief = RIDGE, text = "CONFIRM SELECTION", fg = "white",
                                                    command = self.confirmIndividualFilters)
        self.confirmIndividualChoiceButton.place(x=130,y=470)



    def confirmIndividualFilters(self):
        searchBySelections = []
        searchForSelections = []
        timeSelections = []
        for searchByOption in self.searchByOptions.curselection():
            searchBySelections.append(self.searchByOptions.get(searchByOption))
            
        for searchForOption in self.searchForOptions.curselection():
            searchForSelections.append(self.searchForOptions.get(searchForOption))

        for timeOption in self.timePeriodOptions.curselection():
            timeSelections.append(self.timePeriodOptions.get(timeOption))

        analysis = POS_analytics.processIndividualAnalysis(searchBySelections,searchForSelections,timeSelections)
        self.loadIndividualAnalysis(analysis)

    def loadIndividualAnalysis(self,individualAnalysis):
        tableFont = Font(size = 15)
        tableStyle = ttk.Style()
        tableStyle.configure("Treeview",font = tableFont,rowheight = 40)
        
        if individualAnalysis[0]['quantity'] is None:
            try:
                self.revenueTable.place_forget()
            except:
                pass
            
            self.revenueTable = ttk.Treeview(self.analyticsResultsCanvas, height = 11,columns = ("PRODUCT NAME","REVENUE"),
                                             show = 'headings')
            self.revenueTable.column("#1",anchor = CENTER, stretch = NO, width = 475)
            self.revenueTable.heading("#1", text = "PRODUCT NAME")

            self.revenueTable.column("#2", anchor = CENTER, stretch = NO, width =  473)
            self.revenueTable.heading("#2", text = "REVENUE")

            self.revenueTable.place(x=10,y=50,width = 950)

            scrollbar = ttk.Scrollbar(self.analyticsResultsCanvas, orient = "vertical", command = self.revenueTable.yview)
            self.revenueTable.configure(yscroll = scrollbar.set)
            scrollbar.place(y=75,x=942,height = 440)
                
            for analysis in individualAnalysis:
                self.revenueTable.insert("",'end', values = (analysis['name'],analysis['revenue']))

        elif individualAnalysis[0]['revenue'] is None:
            try:
                self.revenueTable.place_forget()
            except:
                pass
            
            self.revenueTable = ttk.Treeview(self.analyticsResultsCanvas,height = 11,columns = ("PRODUCT NAME", "UNITS SOLD"),
                                             show = 'headings')
            self.revenueTable.column("#1",anchor = CENTER,stretch = NO, width = 475)
            self.revenueTable.heading("#1", text = "PRODUCT NAME")

            self.revenueTable.column("#2", anchor = CENTER, stretch = NO, width = 472)
            self.revenueTable.heading("#2", text = "UNITS SOLD")

            self.revenueTable.place(x=10,y=50,width = 950)

            scrollbar = ttk.Scrollbar(self.analyticsResultsCanvas, orient = "vertical", command = self.revenueTable.yview)
            self.revenueTable.configure(yscroll = scrollbar.set)
            scrollbar.place(y=75,x=942,height = 440)
            
            for analysis in individualAnalysis:
                print("ANALYSIS")
                print(analysis)
                self.revenueTable.insert("",'end',values = (analysis['name'],analysis['quantity']))
                

        else:
            try:
                self.revenueTable.place_forget()
            except:
                pass
            
            self.revenueTable = ttk.Treeview(self.analyticsResultsCanvas,height = 11, columns = ("PRODUCT NAME", "UNITS SOLD", "REVENUE"),
                                             show = 'headings')

            self.revenueTable.column("#1",anchor = CENTER, stretch = NO, width = 315)
            self.revenueTable.heading("#1", text = "PRODUCT NAME")

            self.revenueTable.column("#2", anchor = CENTER, stretch = NO, width = 315)
            self.revenueTable.heading("#2", text = "UNITS SOLD")

            self.revenueTable.column("#3", anchor = CENTER, stretch = NO, width = 316)
            self.revenueTable.heading("#3", text = "REVENUE")

            self.revenueTable.place(x=10,y=50,width = 950)

            scrollbar = ttk.Scrollbar(self.analyticsResultsCanvas, orient = "vertical", command = self.revenueTable.yview)
            self.revenueTable.configure(yscroll = scrollbar.set)
            scrollbar.place(y=75,x=942,height = 440)

            for analysis in individualAnalysis:
                self.revenueTable.insert("",'end',values = (analysis['name'],analysis['quantity'],analysis['revenue']))

    def loadReceiptFilter(self):
        self.selectionFrame1.place_forget()
        optionsFont = Font(size = 12)
        labelFont = Font(size=18)

        self.receiptFilterFrame = Frame(self.analyticsFilterFrame, height = 520, width = 290, bg = "blue",
                                             padx=5,pady=5)
        self.receiptFilterFrame.place(x=0,y=0)

        self.timePeriodLabel4 = Label(self.receiptFilterFrame,bg = "blue", fg = "white", font = labelFont,
                                      text = "TIME PERIOD")
        self.timePeriodLabel4.place(x=55,y=10)

        self.timePeriodOptions4 = Listbox(self.receiptFilterFrame, selectmode = "multiple", bg = "#8787CE",
                                         fg = "white", bd = 5, relief = RIDGE, width = 30, font = optionsFont,
                                         height = 8, exportselection = 0)

        timePeriodOptions = ["7 Days", "1 Month", "3 Months", "6 Months", "1 Year", "3 Year", "All-Time","Custom Date Range"]
        
        self.timePeriodOptions4.place(x=0,y=55)
        
        for option in timePeriodOptions:
            self.timePeriodOptions4.insert(END,option)

        self.confirmReceiptChoiceButton = Button(self.receiptFilterFrame,height = 2,width = 20,bg = "#8787CE", bd = 5,
                                                    relief = RIDGE, text = "CONFIRM SELECTION", fg = "white",
                                                    command = self.confirmReceiptFilters)
        self.confirmReceiptChoiceButton.place(x=130,y=470)
        
    def confirmReceiptFilters(self):
        self.timeSelections4 = []
        for timeOption in self.timePeriodOptions4.curselection():
            self.timeSelections4.append(self.timePeriodOptions4.get(timeOption))
        if "Custom Date Range" in self.timeSelections4:
            self.loadReceiptCustomDateRange()
        else:
            retrievedReceipt = []
            values = POS_analytics.receiptRetrieval(self.timeSelections4)
            self.loadPastReceipts(values)

    def loadReceiptCustomDateRange(self):
        entryFont = Font(size=16)
        labelFont = Font(size = 18)
        self.receiptFilterFrame.place_forget()
        self.customReceiptFilterFrame = Frame(self.analyticsFilterFrame, height = 520, width = 290, bg = "blue",
                                             padx=5,pady=5)
        self.customReceiptFilterFrame.place(x=0,y=0)

        self.startDateLabel = Label(self.customReceiptFilterFrame, bg = "blue", fg = "white", text = "START DATE: ",
                                   font = labelFont)
        self.startDateLabel.place(x=65,y=5)


        self.startDateEntry = Entry(self.customReceiptFilterFrame,width = 23,font = entryFont)
        self.startDateEntry.place(x=0,y=50)
        self.startDateEntry.insert(0,"YYYY-MM-DD")

        self.endDateLabel = Label(self.customReceiptFilterFrame, bg = "blue", fg = "white", text = "END DATE: ",
                                   font = labelFont)
        self.endDateLabel.place(x=65,y=100)

        self.endDateEntry = Entry(self.customReceiptFilterFrame,width = 23,font = entryFont)
        self.endDateEntry.place(x=0,y=145)
        self.endDateEntry.insert(0,"YYYY-MM-DD")

        self.confirmCustomDateRangeButton = Button(self.customReceiptFilterFrame,height = 2,width = 20,bg = "#8787CE", bd = 5,
                                                    relief = RIDGE, text = "CONFIRM SELECTION", fg = "white",
                                                    command = self.confirmCustomDateRange)
        self.confirmCustomDateRangeButton.place(x=130,y=470)

    def confirmCustomDateRange(self):
        startDate = self.startDateEntry.get()
        endDate = self.endDateEntry.get()
        retrievedReceipt = []
        retrievedReceipt.append(POS_analytics.customReceiptRetrieval(startDate,endDate))
        retrievedReceipt.append(POS_analytics.receiptRetrieval(self.timeSelections4)[0])
        print("RETRIEVED RECEIPT:")
        print(retrievedReceipt)
        print("INDIVIDUAL RECEIPTS:")
        for receipt in retrievedReceipt:
            print(receipt)
        self.loadPastReceipts(retrievedReceipt)
        

    def loadPastReceipts(self,retrievedData):

        tableFont = Font(size = 15)
        receiptData = []
        for receipt in retrievedData:
            for data in receipt:
                if data not in receiptData:
                    receiptData.append(data)

        self.receiptsTable = ttk.Treeview(self.analyticsResultsCanvas,height = 11,
                                          columns = ("ReceiptID","Date","Time"),show = 'headings')
        self.receiptsTable.column("#1",anchor = CENTER, stretch = NO,width = 315)
        self.receiptsTable.heading("#1", text = "ReceiptID")

        self.receiptsTable.column("#2",anchor = CENTER,stretch = NO,width = 315)
        self.receiptsTable.heading("#2",text = "Date")

        self.receiptsTable.column("#3",anchor = CENTER, stretch = NO, width = 316)
        self.receiptsTable.heading("#3",text = "Time")

        self.receiptsTable.place(x=10,y=50,width = 950)

        tableStyle = ttk.Style()
        tableStyle.configure("Treeview",font = tableFont,rowheight = 40)

        for receipt in receiptData:
            self.receiptsTable.insert("",'end',values = (receipt[0],receipt[1],receipt[2]))

        scrollbar = ttk.Scrollbar(self.analyticsResultsCanvas, orient = "vertical", command = self.receiptsTable.yview)
        self.receiptsTable.configure(yscroll = scrollbar.set)
        scrollbar.place(x=942,y=75,height = 440)

        self.receiptsTable.bind("<Double-1>", self.onDoubleClick)

    def onDoubleClick(self,event):
        item = self.receiptsTable.selection()
        for i in item:
            fileName = self.receiptsTable.item(i, "values")[0] + ".txt"
            print(fileName)
            os.startfile(fileName)
            
    
        

initSystem = POS_GUI(Tk())
def numsButtonAction(entry):
        nums = ["0","1","2","3","4","5","6","7","8","9","."]
        if entry >= 0 and entry <= 10:
            initSystem.entryAmount = initSystem.entryAmount + nums[entry]
            initSystem.updateEntry(initSystem.entryAmount)

        elif entry == 11:
            initSystem.entryAmount = ""
            initSystem.updateEntry(initSystem.entryAmount)
        elif entry == 12:
            initSystem.updateEntry(initSystem.entryAmount)
            changeAmount = float(initSystem.entryAmount) - initSystem.transactionTotal
            initSystem.changeValueLabel.config(text = round(changeAmount,2))

def foodButtonAction(itemNum):
    if itemNum == 1:
        initSystem.createChaatSection()
    elif itemNum == 2:
        initSystem.createWrapSection()
    elif itemNum == 3:
        initSystem.createSamosaSection()
    elif itemNum == 4:
        initSystem.createPakoraSection()
    elif itemNum == 5:
        initSystem.updateTransactionTable("Chole Bhature")
    elif itemNum == 6:
        initSystem.updateTransactionTable("Spring Rolls")
    elif itemNum == 7:
        initSystem.updateTransactionTable("Gol Gappe")
    elif itemNum == 8:
        initSystem.createSidesSection()
    elif itemNum == 9:
        initSystem.createDrinksSection()

def chaatButtonAction(chaatNum):
    if chaatNum == 1:
        initSystem.updateTransactionTable("Papdi Chaat")
    elif chaatNum == 2:
        initSystem.updateTransactionTable("Aloo Tikki Chaat")
    elif chaatNum == 3:
        initSystem.updateTransactionTable("Samosa Chaat")
    elif chaatNum == 4:
        initSystem.updateTransactionTable("Daulat Ki Chaat")
        
def wrapButtonAction(wrapNum):
    if wrapNum == 1:
        initSystem.updateTransactionTable("Chicken Tikka Wrap")
    elif wrapNum == 2:
        initSystem.updateTransactionTable("Kebab Wrap")
    elif wrapNum == 3:
        initSystem.updateTransactionTable("Mixed Wrap")
    elif wrapNum == 4:
        initSystem.updateTransactionTable("Paneer Wrap")

def samosaButtonAction(samosaNum):
    if samosaNum == 1:
        initSystem.updateTransactionTable("Lamb Samosa")
    elif samosaNum == 2:
        initSystem.updateTransactionTable("Veg Samosa")

def pakoraButtonAction(pakoraNum):
    if pakoraNum == 1:
        initSystem.updateTransactionTable("Fish Pakora")
    elif pakoraNum == 2:
        initSystem.updateTransactionTable("Veg Pakora")

def sidesButtonAction(sideNum):
    if sideNum == 1:
        initSystem.updateTransactionTable("Masala Chips")
    elif sideNum == 2:
        initSystem.updateTransactionTable("Chutney")
    elif sideNum == 3:
        initSystem.updateTransactionTable("Mint Chutney")
    elif sideNum == 4:
        initSystem.updateTransactionTable("Raita")
    elif sideNum == 5:
        initSystem.updateTransactionTable("Salad")
    elif sideNum == 6:
        initSystem.updateTransactionTable("Poppadoms")

def drinksButtonAction(drinkNum):
    if drinkNum == 1:
        initSystem.updateTransactionTable("Coca-Cola")
    elif drinkNum == 2:
        initSystem.updateTransactionTable("Diet Coke")
    elif drinkNum == 3:
        initSystem.updateTransactionTable("Limca")
    elif drinkNum == 4:
        initSystem.updateTransactionTable("ThumsUp")
    elif drinkNum == 5:
        initSystem.updateTransactionTable("Water")
    elif drinkNum == 6:
        initSystem.updateTransactionTable("Juice")
    elif drinkNum == 7:
        initSystem.createChaiSection()
    elif drinkNum == 8:
        initSystem.updateTransactionTable("Lassi")

def chaiButtonAction(chaiNum):
    if chaiNum == 1:
        initSystem.updateTransactionTable("Masala Chai")
    elif chaiNum == 2:
        initSystem.updateTransactionTable("Karak Chai")

def controlButtonAction(controlNum):
    if controlNum == 1:
        initSystem.chaatFrame.place_forget()
        initSystem.wrapFrame.place_forget()
        initSystem.samosaFrame.place_forget()
        initSystem.pakoraFrame.place_forget()
        initSystem.sidesFrame.place_forget()
        initSystem.drinksFrame.place_forget()
        initSystem.chaiFrame.place_forget()

        initSystem.itemsFrame.place(x=621,y=0)

while True:
    initSystem.root.mainloop()
            
