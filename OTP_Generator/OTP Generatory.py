import time
# For Generating Random Numbers
import random

# Create Function Which Returns Random OTP's
def Generate_OTP():
    # Use random.randint(from,to) for generating random integer numbers
    return random.randint(100000,999999)

# Create Main Function
if __name__ == "__main__":
    for i in range(0,3):
        print(f"Your OTP Is : {Generate_OTP()}\n")
        # time.sleep(seconds) is Optional 
        # time.sleep(0.6)
# Done Thanks For Watching.
# Like, Share, Subscribe For More 
# https://www.youtube.com/@undeniablehack
