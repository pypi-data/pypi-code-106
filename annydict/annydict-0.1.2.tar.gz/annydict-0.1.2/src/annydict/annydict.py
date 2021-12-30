from sqlitedict import SqliteDict
import gc

class TemporyDatabase:

    def __init__(self):
        gc.collect()
        self.tempdb = SqliteDict('./userDb.sqlite', autocommit=True)
        self.gdb = SqliteDict('./sheetdata.sqlite', autocommit=True)

    def check_key(self, number, key):
        status = False
        keyValue = None
        try:
            status =  True if key in self.tempdb[number] else False
            if status:
              keyValue = self.tempdb[number][key]
              print("keyValue")
              print(keyValue)
        except:
            status = False
        return {"status":status,"value":keyValue}
        
    def checkr(self, number):
        status = False
        try:
            status = True if number in self.tempdb else False
        except Exception as e:
            print("checkr error:",e)
            status = False
        return status

    def createFirstkv(self, number, key, value):
        try:
             self.tempdb[number] = {key: value}
        except Exception as e:
            print("createFirstkv error => ",e)

    def doUp(self, number, key, value):
        try:
            old_data = self.tempdb[number]
            print(f"oldData:{old_data}")
            new_pair = {key:value}
            old_data.update(new_pair)
            new_data = dict(old_data)
            self.tempdb[number] = new_data
            print(f"newData:{new_data}")
        except Exception as e:
            print(" doUp ERROR =>",e)

    def doMassUp(self, number, dict_data):
        try:
            old_data = self.tempdb[number]
            old_data.update(dict_data)
            new_data = dict(old_data)
            self.tempdb[number] = new_data
        except:
            pass

    def gv(self, number, key):
        try:
            return self.tempdb[number][key]
        except:
            return "not found"
    
    def getRecord(self, number):
        try:
            return dict(self.tempdb[number])
        except:
            return False

    def dv(self, number, key):
        try:
            old_data = self.tempdb[number]
            del old_data[key]
            self.tempdb[number] = old_data
            
        except:
            print("dv error")

    def deletMultiplkeys(self, number, keys):
        try:
            old_data = self.tempdb[number]
            for key in keys:
                del old_data[key]
            self.tempdb[number] = old_data
        except Exception as e:
            print("dv error",e)

    def deleteRoot(self, number):
        try:
            self.tempdb[number] = {}
            self.tempdb.__delitem__(number)
        except:
            print("deleteRoot error")

    def createG(self,key,value):
        try:
            #print("KEYS:",list(self.gdb))r
            self.gdb[key] = value
        except Exception as e:
            print("createG error:",e)
    
    def getg(self,key):
        try:
            #print("KEYS:",list(self.gdb))
            glb = self.gdb[key]
        except Exception as e:
            print("getg error",e)
        return glb

    def getGColvalues(self,key):
        rangeOfStart = 2
        try:
            glb = self.gdb[key]
            items_dict =  {}
            for i in range(rangeOfStart,len(glb)):
                place = glb[i][1].strip(" ").strip("\n")
                ct = glb[i][2]
                if place:
                    items_dict[i-1] = f"{place}@{ct}"
        except Exception as e:
            print("getg ERROR",e)
        return items_dict

    def lvl2_manipulate(self, number,key,key1,value1):
        try:
            old_data = self.tempdb[number]
            child_data = old_data[key]
            new_pair = {key1:value1}
            child_data.update(new_pair)
            old_data.update(child_data)
            new_data = dict(old_data)
            self.tempdb[number] = new_data
        except Exception as e:
            print("lvl2_manipulate ERROR =>",e)
   
    def mass_lvl2_manipulate(self,number,key,data):
        try:
            for k,v in data.items():
                old_data = self.tempdb[number]
                child_data = old_data[key]
                child_data.update(data)
                old_data.update(child_data)
                new_data = dict(old_data)
                self.tempdb[number] = new_data
        except Exception as e:
            print("mass_lvl2_manipulate error:",e)