if __name__ == '__main__':
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
    
    sorted_records = sorted(set(score for name, score in records))
    
    print(sorted_records)
        
        