
#Program is to whether the two lines overlap

def overlaps(line1,line2):
    if (((line2[0]>=line1[0]) and (line2[0]<=line1[1])) or ((line2[1]>=line1[0]) and (line2[1]<=line1[1]))):
        return True
    else:
        return False

