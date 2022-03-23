"""booklogサイトの本棚に書籍を登録する"""
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import click


@click.command()
@click.option('--booklist',
              help="本の一覧ファイル（テキスト形式 または ISBNコード（10,13両方可） または ASINコード）",
              required=True)
def register_booklog(booklist):
    options = Options()
    options.binary_location = (
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    )
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(2)

    driver.get("https://booklog.jp/login")

    # ユーザーIDとパスワードは環境変数から取得して入力する
    id = driver.find_element(By.ID, "account")
    id.send_keys(os.environ.get("BOOKLOG_ID"))
    pswd = driver.find_element(By.ID, "password")
    pswd.send_keys(os.environ.get("BOOKLOG_PASSWORD"))

    # ログインを行う
    login = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login.click()

    # ISBNのリストを取得する
    with open(booklist, mode='r') as f:
        for line in f:

            # 改行コード
            keyword = line.strip()

            try:

                # 本を検索する
                driver.get(f"https://booklog.jp/search?keyword={keyword}")

                # 検索が完了するのを待つ
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "itemListArea"))
                    )
                # 結果が1件の場合で、かつ、本棚に未登録の場合は登録する
                booklist = driver.find_elements(By.CLASS_NAME, 'itemListArea')
                if len(booklist) >= 1:
                    titles = booklist[0].find_elements(By.CLASS_NAME, 'b10M')
                    title = titles[0].text
                    books = booklist[0].find_elements(By.CLASS_NAME, 'add-item-btn')
                    if len(books) >= 1:
                        books[0].click()
                        print(f"[◎登録完了]検索キーワード={keyword}")
                    else:
                        print(f"[△登録済み]検索キーワード={keyword}")
                else:
                    print(f"[×エラー発生]想定外 検索キーワード={keyword}")
            except:
                print(f"[×例外発生]想定外 検索キーワード={keyword}")

            slice(1)

    print("登録完了")


if __name__ == '__main__':
    register_booklog()
