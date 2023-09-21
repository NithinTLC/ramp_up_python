## Author: NITHIN
## Random Username Generator

This Python script generates random usernames for your application. It's a useful tool when you need to create unique usernames for users.

### Usage

To use this script, follow these steps:

1. **Function `namegen`**:
    - The `namegen` function takes one argument, `no_of_names`, which specifies the number of usernames to generate.
    - Inside the function, a list of uppercase letters of the English alphabet is defined.

2. **Username Generation Loop**:
    - The script uses a loop to generate the specified number of usernames.
    - For each username, it randomly selects 8 letters from the alphabet list to create a list of characters.

3. **Uniqueness**:
    - To ensure uniqueness, the script converts the list of characters into a set, automatically removing any duplicate letters.

4. **Username Composition**:
    - The unique characters are then joined together to form a random string of letters.
    - A random number is generated and appended to the string to create a unique username.

5. **Username Yielding**:
    - The `yield` statement is used to produce usernames one at a time as an iterable when the `namegen` function is called.

6. **Usernames Printing**:
    - To obtain usernames, you can use a `for` loop to iterate through the generator and print each generated username.

### Example

Here's an example of how you can use the script to generate 10 random usernames:

```python
# To get 10 random usernames
for username in namegen(10):
    print(username)

