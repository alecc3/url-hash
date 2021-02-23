## How to Use

In command line:

`python3 shorten.py <your URL here>`

## About

Used SHA256 hash

## Limitations

Chance of collision can be calculated similar to the Birthday Attack Probability.
To ensure absolute URL uniqueness, we can check it against a database and rehash with a different method if there is a collision.

    if hashed_url in DB:
      // collision - rehash
    return rehashed_url

In hopes of preventing collisions, I XOR the truncated netloc with the rest of the URL (query, scheme, etc.), but from some research it appears that XORing hashes only reduces collision chance on a case by case basis, and may in some cases make it more collison prone.

Source:
https://crypto.stackexchange.com/questions/12021/can-the-xor-of-two-non-collision-resistant-hashes-be-collision-resistant#:~:text=The%20either%20of%20HA,0%20for%20all%20x!)&text=In%20some%20cases%2C%20XORing%20two,might%20even%20make%20it%20worse.
