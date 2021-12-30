import re
from strsimpy.normalized_levenshtein import NormalizedLevenshtein
class Cleansing:
    
    def __init__(self):
        pass
    
    def raise_error(self, params):
        """ raise error if params is not valid """
        for key, value in params.items():
            if params[key] is None:
                raise TypeError(f"{key} cannot be None")
        
    def convert_to_string(self, text):
        result = str(text) if type(text) != str else text
        return result
    
    def case_sensitive(self, text, case_sensitive):
        """ case sensitive : upper, lower, capitalize or title """
        result = self.convert_to_string(text)
        if case_sensitive == 'upper':
            result = result.upper()
        elif case_sensitive == 'lower':
            result = result.lower()
        elif case_sensitive == 'capitalize':
            result = result.capitalize()
        elif case_sensitive == 'title':
            result = result.title()
        return result
    
    def alfabeth_only(self, text, case_sensitive='capitalize'):
        """ case sensitive : upper, lower, capitalize or title """
        self.raise_error({"text": text, "case_sensitive": case_sensitive})
        result = self.convert_to_string(text)
        regex = re.compile('[^a-zA-Z ]')
        result = regex.sub('', result)
        result = result.split()
        result = " ".join(result)
        result = self.case_sensitive(result, case_sensitive)
        return result
    
    def number_only(self, number, output_type='int'):
        """ output_type : int or str """
        self.raise_error({"number": number, "output_type": output_type})
        result = self.convert_to_string(number)
        result = re.sub("[^0-9]", "", result)
        result = int(result) if output_type == 'int' else str(result)
        return result

    def clean_name(self, name, case_sensitive='upper'):
        """ case sensitive : upper, lower, capitalize or title """
        self.raise_error({"name": name, "case_sensitive": case_sensitive})
        ouput = self.alfabeth_only(name, case_sensitive)
        result =  {
            'input': name,
            'output' : ouput
        }
        return result
    
    def split_name(self, name, case_sensitive='upper', num_split=3):
        """ 
        case sensitive : upper, lower, capitalize or title
        num_split : number of split 2 or 3 
        when num_split is 2 : then the first name will be the first word and the last name will be the second until the last word
        when num_split is 3 : then the first name will be the first word, the middle name will be the second word and the last name will be the third until the last word
        """
        self.raise_error({"name": name, "case_sensitive": case_sensitive, "num_split": num_split})
        if num_split > 3:
            raise TypeError("num_split must 2 or 3")
        name = self.case_sensitive(name, case_sensitive)
        original_name = name
        nama = self.clean_name(name)['output']
        nama_split = nama.split()
        full_name = " ".join(nama_split)
        if num_split == 2:
            if len(nama_split) == 1:
                first_name = nama_split[0]
                last_name = ''
            elif len(nama_split) == 2:
                first_name = nama_split[0]
                last_name = nama_split[1]
            elif len(nama_split) >= 3:
                first_name = nama_split[0]
                last_name = " ".join(nama_split[1:])
            result ={
                "original_name": original_name,
                'full_name' : full_name,
                'first_name' : first_name,
                'last_name' : last_name
            }
        if num_split == 3:
            if len(nama_split) == 1:
                first_name = nama_split[0]
                middle_name = ''
                last_name = ''
            elif len(nama_split) == 2:
                first_name = nama_split[0]
                middle_name = ''
                last_name = nama_split[1]
            elif len(nama_split) == 3:
                first_name = nama_split[0]
                middle_name = nama_split[1]
                last_name = nama_split[2]
            elif len(nama_split) >= 4:
                first_name = nama_split[0]
                middle_name = nama_split[1]
                last_name = " ".join(nama_split[2:])
            result ={
                "original_name": original_name,
                'full_name' : full_name,
                'first_name' : first_name,
                'middle_name' : middle_name,
                'last_name' : last_name
            }
        return result
    
    def clean_nik(self, nik, output_type='str'):
        """ output_type : int or str """
        self.raise_error({"nik": nik, "output_type": output_type})
        original_nik = nik   
        nik = self.number_only(nik, output_type='str')
        nik = nik.replace('.', '').replace(',', '')   
        kode_provinsi = [
            '11', '12', '13', '14', '15', '16', '17', '18', 
            '19', '21', '31', '32', '33', '34', '35', '36', 
            '51', '52', '53', '61', '62', '63', '64', '65', 
            '71', '72', '73', '74', '75', '76', '81', '82', 
            '91', '92',
            ]
        description = []
        output = nik
        if len(nik) != 16 and len(nik) != 15:
            description.append('NIK length must be 15-16 Digits')
            output = None    
        if nik[-4:] == '0000':
            description.append('The last 4 digits cannot be 0000')   
            output = None     
        if nik[:2] not in kode_provinsi:
            description.append('The first 2 digits are not in the list of provincial codes')
            output = None
        keterangan = ", ".join(description) if description else "NIK format is correct"
        result =  {
            'input': original_nik,
            'output': int(output) if output_type == 'int' else str(output) if output is not None else None,
            'is_valid' : True if output is not None else False,
            'description' : keterangan
        }
        return result

class Matching(Cleansing):
    
    def __init__(self):
        pass
    
    def exact_match(self, first_text, second_text):
        self.raise_error({"first_text": first_text, "second_text": second_text})
        first_text = self.alfabeth_only(first_text)
        second_text = self.alfabeth_only(second_text)
        result = {
            'first_text' : first_text,
            'second_text' : second_text,
            'score' : 1 if first_text == second_text else 0,
            'max_score' : 1
        }
        return result
    
    def levenshtein_match(self, first_text, second_text):
        self.raise_error({"first_text": first_text, "second_text": second_text})
        first_text = self.alfabeth_only(first_text)
        second_text = self.alfabeth_only(second_text)
        levenshtein = NormalizedLevenshtein()
        result = {
            'first_text' : first_text,
            'second_text' : second_text,
            'score' : levenshtein.similarity(first_text, second_text),
            'max_score' : 1
        }
        return result
    
    def part_exact_match(self, first_text, second_text):
        self.raise_error({"first_text": first_text, "second_text": second_text})
        first_text = self.alfabeth_only(first_text)
        second_text = self.alfabeth_only(second_text)
        score = 0
        max_score = 0
        for nama1 in first_text.split():
            max_score = max_score + 1
            for nama2 in second_text.split():
                if nama1 == nama2:
                    score = score + 1
        result = {
            'first_text' : first_text,
            'second_text' : second_text,
            'score' : score,
            'max_score' : max_score
        }
        return result
    
    def part_levenshtein_match(self, first_text, second_text):
        self.raise_error({"first_text": first_text, "second_text": second_text})
        first_text = self.alfabeth_only(first_text)
        second_text = self.alfabeth_only(second_text)
        similarity_results = []
        max_score = 0
        for nama1 in first_text.split():
            similarity_sementara = []
            max_score = max_score + 1      
            for nama2 in second_text.split():
                similarity_sementara.append(NormalizedLevenshtein().similarity(nama1, nama2))  
            similarity_results.append(max(similarity_sementara))
        result = {
            'first_text' : first_text,
            'second_text' : second_text,
            'score' : sum(similarity_results),
            'max_score' : max_score
        }
        return result
    
    def all_method_match(self, first_text, second_text):
        self.raise_error({"first_text": first_text, "second_text": second_text})
        first_text_clean = self.alfabeth_only(first_text)
        second_text_clean = self.alfabeth_only(second_text)
        exact_match_result = self.exact_match(first_text_clean, second_text_clean)
        levenshtein_result = self.levenshtein_match(first_text_clean, second_text_clean)
        part_exact_match_result = self.part_exact_match(first_text_clean, second_text_clean)
        part_levenshtein_result = self.part_levenshtein_match(first_text_clean, second_text_clean)
        result = {
            'first_text' : first_text,
            'second_text' : second_text,
            'first_text_clean' : first_text_clean,
            'second_text_clean' : second_text_clean,
            'exact_match' : {
                'score' : exact_match_result['score'],
                'max_score' : exact_match_result['max_score']
            },
            'levenshtein' : {
                'score' : levenshtein_result['score'],
                'max_score' : levenshtein_result['max_score']
            },
            'part_exact_match' : {
                'score' : part_exact_match_result['score'],
                'max_score' : part_exact_match_result['max_score']
            },
            'part_levenshtein' : {
                'score' : part_levenshtein_result['score'],
                'max_score' : part_levenshtein_result['max_score']
            }
        }
        return result