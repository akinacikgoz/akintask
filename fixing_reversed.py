INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

def fix_text(mystr):
    words = mystr.split()
    fixed_words = []
    for word in words:
        # Eğer kelime parantez içinde ise, parantezleri kaldır
        if word.startswith("(") and word.endswith(")"):
            word = word[1:-1]
        # Eğer kelime ters çevrilmişse, düzelt
        if word[::-1] in words:
            word = word[::-1]
        fixed_words.append(word)
    # Düzeltilmiş kelimeleri bir araya getir ve boşluklarla birleştir
    fixed_str = " ".join(fixed_words)
    return fixed_str

if __name__ == "__main__":
    result = fix_text(INPUT)
    print("Correct!" if result == CORRECT_ANSWER else f"Sorry, it does not match with the correct answer.\nResult: {result}\nExpected: {CORRECT_ANSWER}")