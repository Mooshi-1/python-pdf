
import sequence_init


# [('2025-00048', 'BLOOD - HEART', '2301182', '50ML RED TOP', 'SCGEN', '12821', '25-00048_HBBRT'),
# ('2025-00053', 'BRAIN', '2301269', 'FRESH SPECIMEN CUP', 'SCGEN', '12821', '25-00053_BRNCUP'),
# ('2025-00099', 'BLOOD - HEART', '2302145', '50ML RED TOP', 'SCGEN', '12821', '25-00099_HBBRT'),
# ('2025-00115', 'BLOOD - AORTA', '2302625', '50ML RED TOP', 'SCGEN', '12821', '25-00115_AOBBRT'),
# ('2025-00118', 'BLOOD - ANTEMORTEM', '2303301', 'PURPLE TOP TUBE', 'SCGEN', '12821', '25-00118_AMBPRPT'),
# ('2025-00119', 'BLOOD - AORTA', '2302775', '50ML RED TOP', 'SCGEN', '12821', '25-00119_AOBBRT'),
# ('2025-00120', 'BLOOD - AORTA', '2302815', '50ML RED TOP', 'SCGEN', '12821', '25-00120_AOBBRT')]

def main():
    seq_dir = r'C:\Users\e314883\Desktop\python pdf\sequence_gen'

    #create sequence objects, stored in list samples
    samples = sequence_init.read_sequence(seq_dir)

    method = samples[0].method
    batch_num = samples[0].batch
    print(f"{len(samples)} samples found, method = {method}, batch number = {batch_num}")

    if method == "SCRNZ":
        pass
    elif method == "SCGEN":
        pass
    elif method == "SCLCMSMS":
        pass
    else:
        pass


if __name__ == '__main__':
    main()
