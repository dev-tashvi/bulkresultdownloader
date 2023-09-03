# Bulk Student Result Downloader using Selenium and WebDriver

This Python script automates the process of downloading student results in bulk from your college's website using Selenium and WebDriver. The script is specifically designed for a college result page with the given HTML structure. Please follow the instructions below to use the script effectively.

## Prerequisites

Before using this script, ensure that you have the following prerequisites installed:

- Python 3.x
- Selenium
- WebDriver for Google Chrome (Make sure ChromeDriver executable is in your PATH)
- The Chrome web browser

You can install Selenium using pip:

```bash
pip install selenium
```

## Usage

1. Clone this repository to your local machine or download the script directly.

2. Open the Python script (`bulk_result_downloader.py`) in a text editor or Python IDE of your choice.

3. Modify the `roll_numbers` list with the roll numbers for which you want to download results.

```python
roll_numbers = ['22BCA50265', '22BCA50266', '22BCA50267', ...]
```

4. Update the `url` variable with the URL of your college's result page.

```python
url = "https://jnvuiums.in/(S(utngqx2epnkpvwjwsas1y12w))/Results/ExamResultDeclare.aspx"
```

5. Save the changes to the script.

6. Open your terminal or command prompt and navigate to the directory where the script is located.

7. Run the script using the following command:

```bash
python bulk_result_downloader.py
```

8. The script will automate the process of downloading results for each roll number provided in the `roll_numbers` list.

9. It will open Google Chrome, navigate to the specified college URL, enter the roll number, click the submit button, and wait for the result to load.

10. After a brief pause (configured with `time.sleep(8)`), it will close the browser window and repeat the process for the next roll number.

## Notes

- Ensure that you have the necessary permissions to access and download student results from your college's website.
- Make sure the script handles any login/authentication requirements if your college's website requires it.
- Be respectful of your college's policies and guidelines when using this script.

Please feel free to reach out if you encounter any issues or need further assistance with using this script. Happy result downloading using Selenium and WebDriver!
