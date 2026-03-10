from typing import List

from heapq import heappop, heappush, heapreplace

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcode_freqs = dict()
        for barcode in barcodes:
            if barcode in barcode_freqs:
                barcode_freqs[barcode] += 1
            else:
                barcode_freqs[barcode] = 1

        heap_freqs = []
        for barcode in barcode_freqs:
            heappush(heap_freqs, (-barcode_freqs[barcode], barcode))
        
        answer = []
        while len(heap_freqs) > 0:
            most_freq_barcode = heap_freqs[0][1]
            max_freq = heap_freqs[0][0]
            if len(answer) == 0 or most_freq_barcode != answer[-1]:
                answer.append(most_freq_barcode)
                if max_freq < -1:
                    heapreplace(heap_freqs, (max_freq+1, most_freq_barcode))
                else:
                    heappop(heap_freqs)
            else:
                max_freq, most_freq_barcode = heappop(heap_freqs)
                if len(heap_freqs) == 0:
                    print("This method does not work.")
                    print(answer)
                    exit()
                
                second_max_freq, second_most_freq_barcode = heap_freqs[0]
                answer.append(second_most_freq_barcode)

                if second_max_freq < -1:
                    heapreplace(heap_freqs, (second_max_freq+1, second_most_freq_barcode))
                else:
                    heappop(heap_freqs)
                
                answer.append(most_freq_barcode)

                if max_freq < -1:
                    heappush(heap_freqs, (max_freq+1, most_freq_barcode))
                else:
                    continue
        
        return answer
        

if __name__ == '__main__':
    sol = Solution()
    barcodes = [1,1,1,1,2,2,3,3]
    print(sol.rearrangeBarcodes(barcodes))