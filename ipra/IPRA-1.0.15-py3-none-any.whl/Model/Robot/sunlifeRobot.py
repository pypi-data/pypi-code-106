from os import write
import time
from bs4 import BeautifulSoup
import xlsxwriter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ipra.Model.Robot.baseRobot import BaseRobot
import threading

class SunLifeRobot(BaseRobot):
    def __init__(self, policyList, frame, reportPath, inputPath):
        super().__init__(policyList, frame, reportPath, inputPath)
        self.logger.writeLogString('SUNLIFE-INIT','ROBOT INIT')
        self.maxPolicyListSize = len(policyList)
        self.workbook = xlsxwriter.Workbook(self.reportPath+'SUNLIFE_report.xlsx')
        
        self.basicInfo_sheet = self.workbook.add_worksheet(name="General Information")
        self.basicInfo_sheet.write(0, 0, "Policy No.")

        self.scope_sheet = self.workbook.add_worksheet(name="Customer Information")
        self.scope_sheet.write(0, 0, "Policy No.")

        self.value_sheet = self.workbook.add_worksheet(name="Coverage Details")
        self.value_sheet.write(0, 0, "Policy No.")

        self.value_payment = self.workbook.add_worksheet(name="Policy Value")
        self.value_payment.write(0, 0, "Policy No.")

        self.logger.writeLogString('SUNLIFE-INIT','maxPolicyListSize:'+str(self.maxPolicyListSize))
        
    def waitingLoginComplete(self):
        self.logger.writeLogString('SUNLIFE-LOGIN','START LOGIN')
        self.browser.get("https://new.sunlife.com.hk/index.aspx?login_from=p")
        self.frame.setStatusLableText("Waiting Login")
        
        while not self.isLogin and not self.isStopped:
            try:
                self.browser.window_handles[1]
                time.sleep(1)
                self.browser.close()
                time.sleep(1)
                self.browser.switch_to.window(self.browser.window_handles[0])
                
                self.isLogin=True
                self.browser.find_element_by_link_text('Individual Life Policy Enquiry').click()
                time.sleep(1)
                
                downLine = Select(self.browser.find_element_by_id('Search_DropDownList2'))
                downLine.select_by_visible_text('Downline')
                
                time.sleep(1)
                
                downLineSelectValue = Select(self.browser.find_element_by_id('Search_select2'))
                downLineSelectValue.select_by_visible_text('Yes')
                
                time.sleep(1)

            except:
                time.sleep(2)
        else:
            pass

        if self.isLogin:
            self.frame.setStatusLableText("Logged in")
            self.logger.writeLogString('SUNLIFE-LOGIN','LOGIN COMPLETED')

    def scrapPolicy(self):
        for policy in self.policyList:
            if self.isStopped:
                return
            try:
                self.frame.setStatusLableText("Processing "+str(policy))
                self.logger.writeLogString('SUNLIFE','PROCESSING:'+str(policy))
                
                input = self.browser.find_element_by_id('Search_text1')
                input.clear()
                input.send_keys(str(policy))
                
                self.browser.find_element_by_id('Search_ImageButton1').click()
                self.browser.find_element_by_link_text(str(policy)).click()
                
                time.sleep(1)
                soup = BeautifulSoup(self.browser.page_source, 'lxml')
                file1 = open(str(self.reportPath+policy)+"_basic"+".txt","a",encoding="utf-8")#append mode 
                file1.write(soup.prettify()) 
                file1.close()
                
                self.browser.find_element_by_id('CUST_INFO').click()
                time.sleep(1)
                soup = BeautifulSoup(self.browser.page_source, 'lxml')
                file1 = open(str(self.reportPath+policy)+"_customerInfo"+".txt","a",encoding="utf-8")#append mode 
                file1.write(soup.prettify()) 
                file1.close()
                
                self.browser.find_element_by_id('COV_DTL').click()
                time.sleep(1)
                soup = BeautifulSoup(self.browser.page_source, 'lxml')
                file1 = open(str(self.reportPath+policy)+"_coverageDetails"+".txt","a",encoding="utf-8")#append mode 
                file1.write(soup.prettify()) 
                file1.close()
                
                self.browser.find_element_by_id('POL_VAL').click()
                time.sleep(1)
                soup = BeautifulSoup(self.browser.page_source, 'lxml')
                file1 = open(str(self.reportPath+policy)+"_polictValue"+".txt","a",encoding="utf-8")#append mode 
                file1.write(soup.prettify()) 
                file1.close()
            except:
                self.logger.writeLogString('SUNLIFE',str(policy)+" NOT FOUND")
                self.frame.setStatusLableText(policy+" is not found")
            finally:
                self.frame.setStatusLableText(policy+" completed")
                self.logger.writeLogString('SUNLIFE',str(policy)+" COPMLETED")
                self.frame.setStatusProgresValueByValue(1)
                self.buildReportQueue.append(policy)
                self.buildHeaderQueue.append(policy)
                
                self.browser.find_element_by_id('lblBack').click()
                
    
    def buildReport(self):
        self.buildReportThread = threading.Thread(target = self.__buildReport)
        self.buildReportThread.start()
        self.buildReportHeaderFullFlow()
        pass

    def buildReportOnly(self):
        self.buildReportThread = threading.Thread(target = self.__buildReportOnly)
        self.buildReportThread.start()
        self.buildReportHeaderHalfFlow()
        pass

    def buildReportHeaderFullFlow(self):
        self.buildHeaderThread = threading.Thread(target = self.__buildReportHeaderFullFlow)
        self.buildHeaderThread.start()
        pass
    
    def buildReportHeaderHalfFlow(self):
        self.buildHeaderThread = threading.Thread(target = self.__buildReportHeaderHalfFlow)
        self.buildHeaderThread.start()
        pass

    def __buildReportHeaderFullFlow(self):
        pass

    def __buildReportHeaderHalfFlow(self):
        pass

    def __buildReport(self):
        pass

    def __buildReportOnly(self):
        pass
