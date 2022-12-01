from hashlib import sha256

#test SHA256 function
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()
# define mine function
def mine(block_number,transactions, previoius_hash, prefix_zeros):
    prefix_str = '0'* prefix_zeros
    MAX_NONCE = 1000000
    for nonce in range (MAX_NONCE):
        text = str(block_number) + transactions + previoius_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(" Congratulations! You mined bitcoins with nonce value", nonce)
            return new_hash
    
transactions = ''' # Multi-lines string

David -> Jhon-> 200,
Carla-> Steve -> 150

'''
difficulty = 4

# calculate time it vtakes to mine one bitcoin
import time
start = time.time()
print("start mining")
      
new_hash = mine(2,transactions,"0000045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78",difficulty )

total_time = str((time.time() - start))
print(f" mining took: {total_time}, seconds ")

print(new_hash)