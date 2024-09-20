def reverseCamel(text):
    result = ''
    
    for i in text:
        
        if i.isupper() and result:
            result += ' ' + i.lower()
        else:
            result += i.upper()
    
    return result



if __name__ == "__main__":
    text = input("Text: ")
    
    result = reverseCamel(text)
    print(result)
    
