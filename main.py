__author__ = 'James Patton'


def bucketify(words, size_of_bucket):
    words = words.strip(' ').split(' ')
    buckets = []
    for word in words:

        # if can add to bucket do so else return []
        if len(word) <= size_of_bucket:
            # buckets empty add first word
            if len(buckets) == 0:
                buckets.append(word)

            # if current bucket can fit the new word and the space
            elif len(buckets[-1]) + len(word) + 1 <= size_of_bucket:
                buckets[-1] += " " + word

            # must be added to new bucket
            else:
                buckets.append(word)

        # cannot be added to any bucket
        else:
            return []

    return buckets


def main():
    words = input("Enter the phrase you want to bucketize: ")
    size_of_bucket = int(input("Enter the size of the buckets: "))
    bucketfied = bucketify(words, size_of_bucket)
    if len(bucketfied) == 0 and len(words) > 0:
        print("Could not fit into the buckets so result is: []")
    else:
        print("Result is ", bucketfied)


if __name__ == '__main__':
    main()

