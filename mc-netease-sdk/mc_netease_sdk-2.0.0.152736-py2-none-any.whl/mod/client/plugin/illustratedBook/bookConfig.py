
#-*- coding: UTF-8 -*- 
from typing import List
from typing import Dict
from typing import Tuple
from typing import Iterable

class BookConfig:

    class Dirs:
        ResourceDir = "customBooks"    

    class presetData:
        jsonFile = "book_preset.main"
        panelName = "book_preset_panel"
        compNodeTargetPath = "/bookPanel/compsInPanel"

    class TextSize:
        infotext = 6
        footprint = 8
        content = 10
        smallTitle = 12
        middleTitle = 14
        title = 16

    TextOriginFontSize = 10.0

    class Colors:
        TextDefault = (0.1875, 0.01171875, 0.01171875, 1.0)
        BookTitle = (249.0/255.0, 221.0/255.0, 166.0/255.0, 1.0)
        SubTitle = (72.0/255.0, 30.0/255.0, 23.0/255.0, 1.0)
        CategoryButtonText = (66/255.0, 66/255.0, 66/255.0, 1.0)
        

    class TitleType:
        IconText = 0
        SimpleText = 1

    class TextAlign:
        Left = 0
        Right = 1
        Center = 2
        Fit_Center = 3
        Fit_Left = 4
        Fit_Right = 5

    class ImageReszieRule:
        Ninesliced = 0
        Fit = 1

    # 这里记录的是一些预设用到的数据
    class Images:
        blank = "textures/ui/book_gui/blank" 
        black = "textures/ui/book_gui/black"
        returnBtn = "textures/ui/book_gui/btn01"
        historyBtn = "textures/ui/book_gui/btn02"
        editBtn = "textures/ui/book_gui/btn03"
        bookSidePanel = "textures/ui/book_gui/btn04"        
        nextPageBtn = "textures/ui/book_gui/btn05"      
        prevPageBtn = "textures/ui/book_gui/btn06"      
        closeBtn = "textures/ui/book_gui/icon01"    
        lockBtn_dark = "textures/ui/book_gui/icon02" 
        gapline = "textures/ui/book_gui/icon03" 
        pageGap = "textures/ui/book_gui/icon04" 
        lockBtn_light = "textures/ui/book_gui/icon05" 
        arrowIcon = "textures/ui/book_gui/icon06" 
        orderIcon = "textures/ui/book_gui/icon07" 
        bookPanel = "textures/ui/book_gui/panel01" 
        bookTitleBg = "textures/ui/book_gui/panel02"   
        sqrtPanel_dark = "textures/ui/book_gui/panel03"   
        sqrtPanel_light = "textures/ui/book_gui/panel04"   
        rectPanel_dark = "textures/ui/book_gui/panel05" 
        rectPanel_alpha = "textures/ui/book_gui/panel06" 
        progressBar_light = "textures/ui/book_gui/progressbar01_01"
        progressBar_dark = "textures/ui/book_gui/progressbar01_bg"  
        testImage = "textures/ui/book_gui/testImage"  
        categoryDefaultIcon = "textures/items/book_normal"
        entryDefaultIcon = "textures/items/book_enchanted"
    
