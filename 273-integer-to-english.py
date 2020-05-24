class Solution:
    def numberToWords(self, num: int) -> str:
        base = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }

        # Edge cases: Straightforward
        if num in base:
            return base[num]
        elif num == 0:
            return 'Zero'
        
        def construct(num):
            result = ""
            hundreds = num // 100
            if hundreds >= 1:
                result += base[hundreds] + ' ' + 'Hundred'
                num %= 100
            if num in base:
                result += ' ' + base[num]
            else:
                tens = num // 10 * 10
                if tens >= 1:
                    result += ' ' + base[tens]
                    num %= 10
                if num in base:
                    result += ' ' + base[num]
            return result
                
        
        result = ""
        
        billion = num // 1000000000
        if billion >= 1:
            result += base[billion] + ' ' + 'Billion'
            num %= 1000000000
            
        million = num // 1000000
        if million >= 1:
            if len(result) > 0:
                result += " "
            result += construct(million) + ' ' + 'Million'
            num %= 1000000
            
        thousand = num // 1000
        if thousand >= 1:
            if len(result) > 0:
                result += " "
            result += construct(thousand) + ' ' + 'Thousand'
            num %= 1000
            
        if len(result) > 0:
            result += " "
        result += construct(num)
        
        res = ' '.join(result.split())
        
        return res