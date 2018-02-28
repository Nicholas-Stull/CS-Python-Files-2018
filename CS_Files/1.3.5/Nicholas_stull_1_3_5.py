#if input('One character: ') == '!':
   # print('Wow', end='!')


def how_eligible(essay):
    score=0
    if '?' in essay:
        score +=1 
        if ',' in essay:
            score +=1
            if '"' in essay:
                score +=1
                if '!' in essay:
                    score +=1
    return score
    