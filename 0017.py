#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
#The use of "and" when writing out numbers is in compliance with British usage.

def main():
	


def f(x):
    return {
        1: 'ONE',
        2: 'TWO',
        3: 'THREE',
        4: 'FOUR',
        5: 'FIVE',
        6: 'SIX',
        7: 'SEVEN',
        8: 'EIGHT'
        9: 'NINE'
        10:'TEN',
        11:'ELEVEN',
        12:'TWELVE',
        13:'THIRTEEN',
        14:'FOURTEEN',
        15:'FIFTEEN',
        16:'SIXTEEN',
        17:'SEVENTEEN',
        18:'EIGHTEEN',
        19:'NINETEEN',
        20:'TWENTY',
        30:'THIRTY',
        40:'FOURTY',
        50:'FIFTY',
        60:'SIXTY',
        70:'SEVENTY',
        80:'EIGHTY',
        90:'NINETY',
        100:'HUNDRED',
        1000: "ONETHOUSAND",
        }.get(x, 0) 
main()