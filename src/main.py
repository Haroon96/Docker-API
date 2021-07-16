import os
from argparse import ArgumentParser
from selenium.webdriver import Chrome, ChromeOptions
from pyvirtualdisplay import Display

def init_webdriver():
    # start a virtual display so Chrome can render
    Display(size=(1920, 1080)).start()
      
    # required options for Chrome to run in a docker container
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    return Chrome(options=options)

def main(args):
    # create page url
    url = 'https://reqres.in/api/users/%s' % args.userId

    # load selenium driver
    driver = init_webdriver()
    driver.get(url)

    # dump json to outputDir/userId
    with open(os.path.join(args.outputDir, args.userId), 'w') as f:
        f.write(driver.page_source)

def parse_args():
    # program takes two args
    #   -> userId for which user to get data for
    #   -> outputDir where to write result to
    parser = ArgumentParser()
    parser.add_argument('userId')
    parser.add_argument('outputDir')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    main(args)