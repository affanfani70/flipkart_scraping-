import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = Options()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--headless")

service_obj = Service()
driver = webdriver.Edge(service=service_obj, options=edge_options)

watch_name = []
current_price = []
mrp_price = []
discount = []
delivery_charge = []
stars = []
rating = []
review = []

try:
    # Outer loop for the first two pages
    for page in range(1, 3):
        driver.get(f"https://www.flipkart.com/q/smart-watches?otracker=undefined_footer_footer&page={page}")
        driver.maximize_window()
        driver.implicitly_wait(10)

        for i in range(2, 12):
            for j in range(1, 5):
                try:
                    watch_name_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[1]')
                        )
                    )
                    watch_name.append(watch_name_element.text)
                except:
                    watch_name.append("")

                try:
                    current_price_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[1]')
                        )
                    )
                    current_price.append(current_price_element.text)
                except:
                    current_price.append("")

                try:
                    mrp_price_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[2]')
                        )
                    )
                    mrp_price.append(mrp_price_element.text)
                except:
                    mrp_price.append("")

                try:
                    discount_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[2]/div/div[3]/span')
                        )
                    )
                    discount.append(discount_element.text)
                except:
                    discount.append("")

        original_window = driver.current_window_handle
        for i in range(2, 12):
            for j in range(1, 5):
                driver.find_element(
                    By.XPATH,
                    f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div/a[1]'
                ).click()
                all_windows = driver.window_handles
                driver.switch_to.window(all_windows[1])

                try:
                    delivery_charge_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[5]/div/div/div[2]/div[1]/ul/div/div[1]/span[3]')
                        )
                    )
                    delivery_charge.append(delivery_charge_element.text)
                except:
                    delivery_charge.append("")
                try:
                    stars_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[1]/div')
                        )
                    )
                    stars.append(stars_element.text)
                except:
                    stars.append("")
                try:
                    rating_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[1]')
                        )
                    )
                    rating.append(rating_element.text)
                except:
                    rating.append("")
                try:
                    review_element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[3]')
                        )
                    )
                    review.append(review_element.text)
                except:
                    review.append("")
                finally:
                    driver.close()
                    driver.switch_to.window(original_window)

except Exception as e:
    print(e)
finally:
    driver.quit()
    # print(watch_name)
    # print(current_price)
    # print(mrp_price)
    # print(discount)
    # print(delivery_charge)
    # print(stars)
    # print(rating)
    # print(review)
    data_records = {
        "Watch_Name": watch_name,
        "Current_price": current_price,
        "MRP_Price": mrp_price,
        "Discount": discount,
        "Delivery_Charge": delivery_charge,
        "Stars": stars,
        "Rating": rating,
        "Review": review,
    }
    df = pd.DataFrame(data_records)
    df.to_csv("Output_records.csv", index=False)
