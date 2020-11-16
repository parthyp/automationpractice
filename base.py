this would house set up/tear down classes


def launch_browser(caps, executor=EXECUTORS[EV['executor']]):
    """
    Launches a new browser session based on the desired capabilities passed in as a parameter at the executor
    specified in the configuration file.
    :param caps: Desired capabilities object containing webdriver capabilities
    :param executor: Determines the server that will be connected to (assuming we have a grid somewhere)
    :return: Selenium webdriver for the new browser session
    """
    if 'app_device' in caps:
        driver = app_webdriver.Remote(command_executor=executor, desired_capabilities=caps)
    elif 'mobile' in caps:
        driver = sel_webdriver.Remote(command_executor=executor, desired_capabilities=caps)
        driver.set_window_size(400, 900)
    else:
        #selenium
        driver = sel_webdriver.Remote(command_executor=executor, desired_capabilities=caps)
    return driver


def teardown_func(drivers, router, success, test_name):
    if not isinstance(drivers, list):
        drivers = [drivers]
    for driver in drivers:
        if driver is not None:
            if not success:
                save_screenshot(driver, test_name)
            else:
                pass_test_function()
            try:
                driver.quit()
            except WebDriverException as e:
                if "has already finished" in e.msg:
                    print 'Selenium session has already closed'
                else:
                    raise e
