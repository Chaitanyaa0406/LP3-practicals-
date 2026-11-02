import heapq

# Node class
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Generate Huffman Codes
def generate_codes(root, code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = code
        return

    generate_codes(root.left, code + "0", huffman_codes)
    generate_codes(root.right, code + "1", huffman_codes)


# Input characters and frequencies
n = int(input("Enter number of characters: "))

heap = []

for i in range(n):
    char = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    heapq.heappush(heap, (freq, i, Node(char, freq)))

# Build Huffman Tree
while len(heap) > 1:
    freq1, i1, left = heapq.heappop(heap)
    freq2, i2, right = heapq.heappop(heap)

    new_node = Node(None, freq1 + freq2)
    new_node.left = left
    new_node.right = right

    heapq.heappush(heap, (new_node.freq, n + i1 + i2, new_node))

root = heap[0][2]

# Generate and Display Codes
huffman_codes = {}
generate_codes(root, "", huffman_codes)

print("\nHuffman Codes:")
for char, code in huffman_codes.items():
    print(char, ":", code)