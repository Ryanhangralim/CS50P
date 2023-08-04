from validator_collection import validators, checkers
import validators
   
def main():
    print(is_valid(input("What's your email address? ")))


def is_valid(s):
    if(".com.com" in s):
        return "Invalid"
    if(checkers.is_email(s)):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()