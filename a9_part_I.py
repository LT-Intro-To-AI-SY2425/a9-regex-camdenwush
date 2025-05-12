import re

# Assignment 9 Part I
# in each of the problems below the first parameter to re.compile is "REPLACE ME" your
# job is to replace this text with a regular expression that behaves as described by the
# comment and accompanying prints/tests

# problem 1
# should extract a match where the first group is the month, the second group the day
# and the third group the year
date_string = "November 9, 1982"

pat_date = re.compile(r"([a-z]+)\s+(\d{1,2}),\s+(\d{4})", re.IGNORECASE)
date_matches = pat_date.match(date_string)

# problem 2
# should extract a match where the first group is the number, the second the street, the
# third the city, the fourth the state and the fifth the zip code
address_string = "2501 Addison Street\nChicago, IL 60618"

pat_address = re.compile(r"(?P<number>\d+)\s+(?P<street>[^\n]+)\n(?P<city>[^,]+),\s+(?P<state>[A-Za-z]{2})\s+(?P<zip>\d{5})", re.IGNORECASE)
address_matches = pat_address.match(address_string)

# problem 3
# should match all hashtags
tweet_string = "hi everyone! #cs #python #LT #champions"

pat_hashtag = re.compile(r"#(\w+)", re.IGNORECASE)
hashtag_matches = pat_hashtag.findall(tweet_string)

# until you uncomment any code line below you'll get an EOF linting error feel free to
# ignore it
if __name__ == "__main__":
    print("<<<<< Date Problem >>>>>\n")
    # uncomment the following prints to see date results and asserts to test
    if date_matches:
        print(f"month is: {date_matches.group(1)}!") # should print "month is: November"
        print(f"day is: {date_matches.group(2)}!")   # should print "day is: 9"
        print(f"year is: {date_matches.group(3)}!")  # should print "year is: 1982"
        assert date_matches.group(1).lower() == 'november', "Incorrect month" # Use .lower() for robust comparison with IGNORECASE
        assert date_matches.group(2) == '9', "Incorrect day"
        assert date_matches.group(3) == '1982', "Incorrect year"
        print('\n<<<< Date extraction tests passed >>>>\n')
    else:
        print("Date pattern did not match.")

    print("<<<<< Address Problem >>>>>\n")
    # uncomment the following prints to see results and asserts to test
    if address_matches:
        print(f'number is: {address_matches.group("number")}!') # should print "number is: 2501"
        print(f'street is: {address_matches.group("street")}!') # should print "street is: Addison Street"
        print(f'city is: {address_matches.group("city")}!')     # should print "city is: Chicago"
        print(f'state is: {address_matches.group("state")}!')   # should print "state is: IL"
        print(f'zip is: {address_matches.group("zip")}!')       # should print "zip is: 60618"
        assert address_matches.group('number') == '2501', "Incorrect address number"
        assert address_matches.group('street') == 'Addison Street', "Incorrect street"
        assert address_matches.group('city') == 'Chicago', "Incorrect city"
        assert address_matches.group('state').upper() == 'IL', "Incorrect state" # Use .upper() for robust comparison
        assert address_matches.group('zip') == '60618', "Incorrect zip"
        print('\n<<<< Address extraction tests passed >>>>\n')
    else:
        print("Address pattern did not match.")

    print("<<<<< Hashtag Problem >>>>>\n")
    # uncomment the following prints to see results and asserts to test
    print(f"hashtags are: {hashtag_matches}") # should be ['cs', 'python', 'LT', 'champions']"
    expected_hashtags = ['cs', 'python', 'lt', 'champions']
    # Make the comparison robust to case from IGNORECASE if original tweet had mixed case tags
    assert [tag.lower() for tag in hashtag_matches] == expected_hashtags, "Incorrect hashtags"
    print('\n<<<< Hashtag extraction tests passed >>>>\n')

    if date_matches and address_matches and ([tag.lower() for tag in hashtag_matches] == expected_hashtags) :
        print('\n<<<< All tests passed! >>>>')
    else:
        print('\n<<<< Some tests failed. >>>>')
