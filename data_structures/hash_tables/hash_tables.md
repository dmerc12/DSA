# Hash Tables:

A hash table is a data structure that stores unordered items by mapping (or hashing) each item to a location in an array (or vector).
A hash table's main advantage is that searching (or inserting / removing) an item may require only O(1), in contrast to O(N) for searching a list or to O(log N) for binary search.

In a hash table, an item's key is the value used to map an index.
For all items that might possibly be stored in the hash table, every key is ideally unique, so that the hash table's algorithms can search for a specific item by that key.

Each hash table array element is called a bucket.
A hash function computes a bucket index from the item's key.

A common hash function uses the modulo operator (%).
A hash table's operations of insert, remove, and search each use the hash function to determine an item's bucket.

A collision occurs when an item being inserted into a hash table maps to the same bucket as an existing item in the hash table.
Various techniques are used to handle collisions during insertions, such as chaining or open addressing.
- Chaining is a collision resolution technique where each bucket hass a list of items.
- Open addressing is a collision resolution technique where collisions are resolved by looking for an empty bucket elsewhere in the table.

## Chaining:
Chaining handles hash table collisions by using a list for each bucket, where each list may store multiple items that map to the same bucket.
The insert operation first uses the item's key to determine the bucket, and then inserts the item in that bucket's list.
Searching also first determines the bucket, and then searches the bucket's length.
Likewise for removes.

## Linear Probing:
A hash table with linear probing handles a collision by starting at the key's mapped bucket, and then linearly searches subsequent buckets until an empty bucket is found.

Actually, linear probing distinguishes two types of empty buckets:
- An empty-since-start bucket has been empty since the hash table was created.
- An empty-after-removal bucket had an item removed that caused the bucket to now be empty.

The distinction will be important during searches, since searching only stops for empty-since-start, not for empty-after-removal.

### Inserts Using Linear Probing:
Using linear probing, a hash table insert algorithm uses the item's key to determine the initial bucket, linearly probes (or checks) each bucket, and inserts the item in the next empty bucket (the empty kind doesn't matter).
If the probing reaches the last bucket, the probing continues at bucket 0.
The insert algorithm returns true if the item was inserted, and returns false if all buckets are occupied.

### Removals Using Linear Probing:
Using linear probing, a hash table remove algorithm uses the sought item's key to determine the initial bucket.
The algorithm probes each bucket until either a matching item is found, an empty-since-start bucket is found, or all buckets have been probed.
If the item is found, the item is removed, and the bucket is marked empty-after-removal.

Note that if the algorithm encounters an empty-after-removal bucket, the algorithm keeps probing, because the sought item may have been placed in a subsequent bucket before this bucket's item was removed.

### Searches Using Linear Probing:
In linear probing, a hash table search algorithm uses the soughht item's key to determine the initial bucket.
The algorithm probes each bucket until either the matching item is found (returning the item), an empty-since-start bucket is found (returning null), or all buckets are probed without a match (returning null).
If an empty-after-removal bucket is found, the search algorithm continues to probe the next bucket.

## Quadratic Probing:
A hash table with quadratic probing handles a collision by starting at the key's mapped bucket, and then quadratically searches subsequent buckets until an empty bucket is found.
If an item's mapped bucket is H, the formula <i>(H + C1 * i + C2 * i<sup>2</sup>) mod(tablesize)</i> is used to dettermine the item's index in the hash table.
C1 and C2 are programmer-defined constants for quadratic probing.
Inserting a key uses the formula, starting with i = 0, to repeatedly search the hash table until an empty bucket is found.
Each time an empty bucket is not found, i is incremented by 1.
Iterating through sequential i values to obtain the desired table index is called the <b>probing sequence</b>

### Searching and Removal with Quadratic Probing:
The search algorithm uses the probing sequence until the key being searched for is found or an empty-since-start bucket is found.
The removal algorithm searchess for the key to remove and, if found, marks the bucket as empty-after-removal.

## Double Hashing:
Double hashing is an open-addressing collision resolution technique that uses two different hash functions to compute bucket indicies.
Using hash functions H1 and H2, a key's index in the table is computed with formula <i>(H1(key) + i * H2(key))mod(tablesize)</i>.
Inserting a key uses the formula, starting with i = 0, to repeatedly search hash table buckets until an empty bucket is found.
Each time an empty bucket is not found, i is incremented by 1.
Iterating through sequential i values to obtain the desired table index is called the probing sequence.

### Insertion, Search, and Removal:
Using double hashing, a hash table search algorithm probes (or checks) each bucket using the probing sequence defined by the two hashing functions.
The search continues until either the matching item is found (returning the item), an empty-since-start bucket is found (returning null), or all buckets are probed without a match (returning null).

A hash table insert algorithm probes each bucket using the probing sequence, and inserts the item in the next empty bucket (the empty kind doesn't matter).

A hash table removal algorithm first searches for the item's key.
If the item is found, the item is removed, and the bucket is marked empty-after-removal.

## Hash Table Resizing:
A hash table resize operation increases the number of buckets, while preserving all existing items.
A hash table with N buckets is commonly resized to the next prime number &ge; N * 2.
A new array is allocated, and all items from the old array are re-inserted into the new array, making the resize operation's time complexity O(N).

A hash table's load factor is the number of items in the hash table divided by the number of buckets.
The load factor may be used to decide when to resize the hash table.
An implementation may choose to resize the hash table when one or more of the following values exceeds a certain threshold:
- Load factor.
- When using open-addressing, the number of collisions during an insertion.
- When using chaining, the size of a bucket's linked-list.

## Common Hash Functions:
A hash table is fast if the hash function minimizes collisions.

A perfect hash function maps items to buckets with no collisions.
A perfect hash function can be created if the number of items and all possible item keys are known beforehand.
The runtime for insert, search, and remove is O(1) with a perfect hash function.

A good hash function should uniformly distribute items into buckets.
With chaining, a good hash function results in short bucket lists and fast inserts, searches, and removes.
With linear probing, a good hash function will avoid hashing multiple times to consectutive buckets and thus minimize the average linear probing length to achieve fast inserts, searches, and removes.
On average, a good hash function will achieve O(1) inserts, searches, and removes, but in the worst-case may require O(N).

A hash function's performance depends on the hash table size and knowledge of the expected keys.

### Modulo Hash Function:
A modulo hash usses the remainder from division of the key by hash table size N.

### Mid-Square Hash Function:
A mid-square hash squares the key, extracts R digits from the result's middle, and returns the remainder of the middle digits divided by hash table size N.
For N buckets, R must be &ge; [log<sub>10</sub> N] to index all buckets.
The process of squaring and extracting middle digits reduces the liklihood of keys mapping to just a few buckets.

The mid-square hash function is typically implemented using binary (base 2), and is not decimal, because a binary implementation is faster.
A decimal implementation requires converting the square of the key to a string, extracting a substring for the middle digits, and converting that substring to an integer.
A binary implementation only requires a few shifts and bitwise AND operations.

A binary mid-square hash function extracts the middle R bitss, and returns the remainder of the middle bits divided by hash table size N, where R is &ge; [log<sub>2</sub> N].
The extracted middle bits depend on the maximum key.

### Multiplicative String Hash Function:
A multiplicative string hash repeatedly multiplies the hash value and adds the ASCII (or Unicode) value of each character in the string.
A multiplicative hash function for strings starts with a large initial value.
For each character, the hash function multiplies the current hash value by a multiplier (often prime) and adds the character's value.
Finally, the function returns the remainder of the sum divided by the hash table size N.

## Direct Hashing:
A direct hash function uses the item's key as the bucket index.
A hash table with a direct hash function is called a direct access table.
Given a key, a direct access table search algorithm returns the item at index key if the bucket is not empty, and returns null (indicating item not found) if empty.

A direct access table has the advantage of no collisions: Each key is unique (by definition of a key), and each gets a unique bucket, so no collisions can occur.
However, a direct access table has two main limitations:
1. All keys must be non-negative integers, but for some applications keys may be negative.
2. The hash table's size equals the largest key value plus one, which may be very large.

## Hashing Algorithms:
### Cryptography:
Cryptography is a field of study focused on transmitting data securely.
Secure data transmission commonly starts with encryption: alteration of data to hide the original meaning.
The counterpart to encryption is decryption: reconstruction of original data from encrypted data.

### Hashing Functions for Data:
A hash function can be used to produce a hash value for data in contexts other than inserting the data into a hash table.
Such a function is commonly used for the purpose of verifying data integrity.
The hash value cannot be used to reconstruct the original data, but can be used to help verify that data isn't corrupt and hasn't been altered.

### Cryptographic Hashing:
A cryptographic hash function is a hash function designed specifically for cryptography.
Such a function is commonly used for encrypting and decrypting data.

A password hashing function is a cryptographic hashing function that produces a hash value for a password.
Databases for online services commonly store a user's password hash as opposed to the actual password.
When the user attempts a login, the supplied password is hashed, and the hash is compared against the database's hash value.
Because the passwords are not stored, if a database with password hashes is breaches, attackers may still have a difficult time determining a user's password.
