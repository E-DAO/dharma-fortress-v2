from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_ui_simulation():
    # Step 1: Set up Chrome WebDriver (this will automatically 
download the correct ChromeDriver)
    driver = 
webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Step 2: Update this line with the path to your `index.html` 
file
    driver.get("file:///path/to/your/project/templates/index.html")  
# <-- Update this with your correct file path

    # Step 3: Simulate user clicking a button
    attack_button = driver.find_element(By.ID, 
"simulate_attack_button")
    attack_button.click()

    # Step 4: Wait for the simulation to complete
    time.sleep(5)

    # Step 5: Verify that the result is displayed
    result_text = driver.find_element(By.ID, "simulation_result")
    assert "Simulation Complete" in result_text.text, "Simulation did 
not complete successfully"

    # Step 6: Check if the report section is displayed
    report_section = driver.find_element(By.ID, "report_section")
    assert report_section.is_displayed(), "Report section is not 
displayed"

    # Step 7: Clean up - close the browser
    driver.quit()

if __name__ == "__main__":
    test_ui_simulation()

