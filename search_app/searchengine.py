# search_app serachengine.py

def check_subsequence(S, s): #function to check if the item is subsequence of String or not
    index = 0
    for i in range(len(s)):
        if i==0:
            if s[i] in S:
                index = S.find(s[i])
            else:
                return False
        else:
            if s[i] in S[index+1:]:
                index += S[index+1:].find(s[i])
            else:
                return  False
    return True

def check_match(item , element):
    item = item.split()
    element = element.split()
    index =0

    # print(item)
    # print(element)
    if len(item)>0:
        for i in element:

            # print('----------')
            # print(item)
            # print(element)
            # print('----------')
            if check_subsequence(item[index], i):
                index+=1
                if index>=len(item):
                    return False
        if index == len(element):
            return True
    return False


def search_element(element, products_list):
    result_count = 0
    results =[]
    for product in products_list:
        if check_match(product.lower(), element.lower()):
            result_count+=1
            results.append(product)
            if result_count>=20:
                results.sort()
                return results
    results.sort()
    return results.sort()

