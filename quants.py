# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:20:55 2024

@author: e314883
"""

#quants
#exceptions to think about
#name casefiles 1 and 2 like LCMSMS
#sometimes single injections

#spiked recovery (3 files, +%R pdf)
#L0 - L6 on 

import fitz  # PyMuPDF
import os
import re

from objects import QCTYPE, QC, Sample, table_converter


def SHIMADZU_SAMPLEINIT(batch_dir):
    samples = [] #will hold sample objects created here
    # Iterate through directory defined by filepath
    for filename in os.listdir(batch_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(batch_dir, filename)        
            doc = fitz.open(pdf_path)

            # Extract text from the first page
            page = doc[0]
            text = page.get_text()
            #print(text)
            lines = text.split('\n')
            
            case_number = None
            
            quant_method = lines[3]
            # Currently storing "ABUSE PANEL QUANTITATION BY LC-MS/MS"
            try:
                # Find case number using sample name index + 1
                sample_name_index = lines.index("Sample Name")
                case_number = lines[sample_name_index + 1]
                # Trim characters off case number string
                case_number = case_number[2:]
                print(f"{case_number}")

                # Extract table data
                ISTDs_data = []
                analytes_data = []
                capture_ISTDs = False
                capture_analytes = False

                for line in lines:
                    #alternate collection windows
                    if "Quantitative Results: ISTDs" in line:
                        capture_ISTDs = True
                        capture_analytes = False
                    elif "Quantitative Results: Analytes" in line:
                        capture_ISTDs = False
                        capture_analytes = True
                    #stop collecting here
                    elif (capture_ISTDs or capture_analytes) and line.strip() == "":
                        capture_ISTDs = False
                        capture_analytes = False
                    #if capture = true, append the data
                    elif capture_ISTDs:
                        ISTDs_data.append(line.strip())
                    elif capture_analytes:
                        analytes_data.append(line.strip())
                print(f"Extracted table data: {len(ISTDs_data)} and {len(analytes_data)}")

                format_ISTDs = table_converter(ISTDs_data)
                format_analytes = table_converter(analytes_data)

                case_number = Sample(case_number, pdf_path, None, format_ISTDs, format_analytes)
                print(f"Created sample: {case_number}")
                if case_number in samples:
                    case_number.ID += "_2"
                    print(f"recognized duplicate")
                samples.append(case_number)

            except Exception as e:
                print(f"FAILED TO INIT SAMPLE {filename}: {e}")

            if "SHIMADZU 8060 SEQUENCE" in lines:
                case_number = "sequence"
                case_number = Sample(case_number, pdf_path, QCTYPE.SEQ, None)
            if "QTABUSE CAL REPORT" in lines:
                case_number = "curve"
                case_number = Sample(case_number, pdf_path, QCTYPE.CUR, None)


            doc.close()  

    #return list of sample objects        
    return samples
            
# class Sample:
#     def __init__(self, ID, type, results, path):
#         self.ID = ID
#         self.type = type
#         self.results = results
#         self.path = path

            
def pdf_rename(samples):
    for sample in samples:
        # Define the new filename
        new_filename = f"{sample.ID}.pdf"
        new_path = os.path.join(os.path.dirname(sample.path), new_filename)

        # Rename the file
        try:
            os.rename(sample.path, new_path)
            print(f"{sample.ID} has been renamed to {new_filename}")

        except PermissionError as e:
            print(f"PermissionError: {e}")
            continue
        except FileExistsError as e:
            print(f"File Exists Error: {e}")
            continue
        except FileNotFoundError as e:
            print(f"File Not Found Error: {e}")
            continue

        # Rename the sample object
        sample.path = new_path

    print("naming complete")


if __name__ == "__main__":
    batch_dir = r"C:\Users\e314883\Desktop\python pdf\PDF DATA\2024"

    samples = SHIMADZU_SAMPLEINIT(batch_dir)
    pdf_rename(samples)
