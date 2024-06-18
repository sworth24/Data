
import PyPDF2
import pdfplumber
import os
import pandas as pd
import openpyxl


def remove_word(x):
    z=x.split()
    new_word=[]
    for word in z:
        if word!= 'cat':
            new_word.append(word)
    print(new_word)

y= 'There was a cat called toffee'


def print_rest_word(x):
    words=x.split()
    new_word=[]
    found_cat = False
    for i in range(len(words)):
        if found_cat:
            new_word.append(words[i])
        elif words[i] == 'cat':
            found_cat = True
    print(new_word)


def print_word_after_cat(x):
    words=x.split()
    for i in range(len(words)):
        if words[i] == 'cat' and i < len(words) - 1:
            print(words[i +1])
            return


pdf_dir  = r"C:\Users\sworthington\OneDrive - Warner Bros. Discovery\IQ Vision\Vendor Spreadsheet checks\NamingConventionStages"

def process_pdfs(pdf_dir):
    for filename in os.listdir(pdf_dir):   
        if filename.endswith('.pdf'):
            pdf_file = open(os.path.join(pdf_dir, filename), 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for i in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[i]
                text += page.extract_text()
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_file = open(os.path.join(pdf_dir, txt_filename), 'w')
            txt_file.write(text)
            pdf_file.close()
            txt_file.close()
    

process_pdfs(pdf_dir)
      




        
def print_words_after_convention(x):
    words=x.split()
    words_after_convention = []
    for i in range(len(words)):
        if words[i].lower() == 'convention' and i< len(words) - 2 and words[i+1] == ':':
            words_after_convention.append(words[i +2])
    return words_after_convention




def print_word_after_description(x):
    words=x.split()
    description_indices = [i for i, word in enumerate(words) if word == 'Description :']
    for description_index in description_indices:
        j= description_index +1
        while j< len(words) and not words[j]. startswith('Naming'):
            print(words[j])
            j+=1
        print()


def print_word_after_convention(x):
    words = x.split()
    words_after_convention = []
    for i in range(len(words)):
        if words[i].lower() == 'convention' and i < len(words) - 2 and words[i +1] == ':':
            return words[i+2]
    return None

def get_words_after_convention(x):
    words = x.split()
    words_after_convention = []
    for i in range(len(words)):
        if words[i].lower() == 'convention' and i < len(words) - 2 and words[i + 1] == ':':
            words_after_convention.append(words[i + 2])  # Store the word after 'Convention:'
    return words_after_convention


def get_word_after_convention(x):
    words = x.split()
    for i in range(len(words)):
        if words[i].lower() == 'convention' and i < len(words) - 2 and words[i + 1] == ':':
            return words[i+2]  
        
    

def get_words_after_label(x):
    words = x.split()
    words_after_label = []
    for i in range(len(words)):
        if words[i].lower() == 'label' and i < len(words) - 2 and words[i + 1] == ':':
            words_after_label.append(' '.join([words[i+2], words[i+3], words[i+4], words[i+5]]))
    return words_after_label

def get_word_after_label(x):
    words = x.split()
    words_after_label = []
    for i in range(len(words)):
        if ((words[i].lower() == 'label' or words[i].lower() == 'levellabel')and i < len(words) - 2 and words[i + 1] == ':') or words[i].lower() == 'label:':
            words_after_label = words[i+2:i+6]
            return combine_strings(words_after_label)
    return None


def get_words_after_description(x):
    words = x.split()
    for i in range(len(words)):
        if (words[i].lower() == 'description' and i < len(words) - 2 and words[i + 1] == ':') or words[i].lower() == 'description:':
            if i + 3 < len(words) and words[i + 3].lower() == 'ident':
                return ' '.join(words[i + 2:i + 5])
            else:
                return ' '.join(words[i + 2:i + 4])
    return ''
     
def get_words_after_summer_threshold(x):
    words = x.split()
    for i in range(len(words)):
        if (words[i].lower() == 'summer' and words[i+1]== 'threshold' and words[i + 2] == ':') or (words[i+1] == 'summer' and words[i+2].lower() == 'threshold:'):
            return ' '.join(words[i + 3 and i+4])
        else:
            return 
    return ''

def get_words_after_winter_threshold(x):
    words = x.split()
    for i in range(len(words)):
        if (words[i].lower() == 'winter' and words[i+1]== 'threshold' and words[i + 2] == ':') or (words[i+1] == 'winter' and words[i+2].lower() == 'threshold:'):
            return ' '.join(words[i + 3 and i+4])
        else:
            return 
    return ''

                                          

def is_billable(x):
    words = x.split()
    billable = []
    for word in words:
        if word == '*BILLABLE*' or word == '*NON-BILLABLE*':
            billable.append(word)
    return billable



def find_billable(x):
    words=x.split()
    for i in range(len(words)):
        if (words[i] == '*BILLABLE*' and i +1 < len(words)) or (words[i] == '*NON-BILLABLE*' and i +1 < len(words)):
            return (words[i])  
    return None


def label_billable(x):
    words=x.split()
    billable = []
    i=0
    while i < len(words):
        if words[i].lower() == 'description' and i < len(words) - 2 and words[i + 1] == ':':
            xytech_location = get_words_after_description(' '.join(words[i:]))
            label_name = get_word_after_convention(' '.join(words[i:]))
            label_status = get_word_after_label(' '.join(words[i:]))
            billable_status = find_billable(' '.join(words[i:]))
            if billable_status:
                billable.append((xytech_location, label_name, label_status, billable_status))
            else:
                billable.append((xytech_location, label_name, label_status, ''))
        i+=1
    return billable 


def make_big_array(x):
    big_array = []
    for array in x:
        big_array.extend(array)
    return big_array
x=[[1,2,3,4],[2,2,2,2],[2,3,2,4]]

def combine_strings(texts):
    combined_text = ""
    for text in texts:
        combined_text += text
    return combined_text

def combine_strings_with_commas(texts):
    combined_text = ""
    for i, text in enumerate(texts):
        combined_text += text
        if i < len(texts) -1:
            combined_text+= ", "
    return combined_text


pdf_dir  = r"C:\Users\sworthington\OneDrive - Warner Bros. Discovery\IQ Vision\Vendor Spreadsheet checks\NamingConventionStages"

def process_pdfs(pdf_dir):
    for filename in os.listdir(pdf_dir):   
        if filename.endswith('.pdf'):
            pdf_file = open(os.path.join(pdf_dir, filename), 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for i in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[i]
                text += page.extract_text()
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_file = open(os.path.join(pdf_dir, txt_filename), 'w')
            txt_file.write(text)
            pdf_file.close()
            txt_file.close()
    

process_pdfs(pdf_dir)

def process_files(directory):
    xytech_locations = []
    label_names = []
    statuses = []
    words_after_labels = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                content = file.read()
                billable = label_billable(content)
                for xytech_location, label_name, word_after_label, status in billable:
                    xytech_locations.append(xytech_location)
                    label_names.append(label_name)
                    words_after_labels.append(word_after_label)
                    statuses.append(status)
                        
    return {'Xytech_locations': xytech_locations, 'label_name': label_names, 'Words_After_Labels': words_after_labels, 'Statuses': statuses}


                
combined_data = process_files(pdf_dir)


df = pd.DataFrame(combined_data)

excel_file = 'new_file.xlsx'
df.to_excel(excel_file)
print(f"Data has been written to {excel_file}.")






        



        





        

