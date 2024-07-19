from hash_table import HashTable


def main():
    hash_table = HashTable(3)
    hash_table.insert("hello", "world")
    hash_table.insert("foo", "bar")
    hash_table.insert("fooz", "baz")
    hash_table.insert("john", "doe")
    hash_table.insert("jane", "doe")
    hash_table.insert("jastin", "poe")

    print(hash_table.get("hello"))
    print(hash_table.get("foo"))

    result = hash_table.remove("foo")
    print(result)
    print(hash_table.get("foo"))

    result = hash_table.remove("foo")
    print(result)


if __name__ == "__main__":
    main()
