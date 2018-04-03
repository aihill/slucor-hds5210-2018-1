def region(description):
    m = 1.0
    description = description.lower()
    
    if 'america' in description:
        m += 0.05
    elif 'united states' in description:
        m += 0.05
    elif 'usa' in description:
        m += 0.05
        
    if 'midwest' in description:
        m += 0.05
    elif 'northwest' in description:
        m -= 0.05
    elif 'northeast' in description:
        m -= 0.05
    
    if 'small' in description:
        m *= 1.1
    if 'rural' in description:
        m *= 1.1
        
    return m