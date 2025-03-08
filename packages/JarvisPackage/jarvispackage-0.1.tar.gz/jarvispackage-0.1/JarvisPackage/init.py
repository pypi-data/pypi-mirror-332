import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd
# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
# Temporarily remove headless mode for debugging
chrome_options.add_argument("--headless=new")  # Run browser in the background

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Website URL
website = "https://allorizenproject1.netlify.app/"
driver.get(website)

# Output file location
rec_file = f"{getcwd()}\\input.txt"


# Function to listen for changes in output
def listen():
    try:
        # Wait for the start button to be clickable and start listening
        start_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'startButton')))
        start_button.click()
        print("Listening..")
        output_text=""
        is_second_click=False
        while True:
            try:
                # Wait for the output element to be available and capture its text
                output_element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, 'output')))
                current_text = output_element.text.strip()

                # Debugging: Print current output and start button text


                # Check if the button text indicates listening has stopped
                if "Start Listening" in start_button.text and is_second_click:
                    if output_text:
                        is_second_click=False
                elif "listening..." in start_button.text:
                    is_second_click = True

                # Only write to the file if the text has changed significantly
                if current_text != output_text:
                    output_text = current_text
                    with open(rec_file,"w") as file:  # Use "a" to append text
                        file.write(output_text.lower())  # Write without newline to keep the text on one line
                        print("User:" +output_text)

            except Exception as e:
                print(f"Error in inner try block: {e}")
                continue
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)


# Start the listening process
listen()
