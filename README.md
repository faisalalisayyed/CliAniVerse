![Logo](https://raw.githubusercontent.com/C0DE-SLAYER/CliAniVerse/master/img/logo.png)

#### Cli Tool To Watch and Download anime. This tool scrapes the site [Gogoplay](https://gogoplay5.com) using beautifulsoup module

## About BeautifulSoup
* This project is made using "BeautifulSoup" which can be install using pip.
* Beautiful Soup is a Python package for parsing HTML and XML documents 
* It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

## Installation

#### For Android Install termux [(Guide)](https://termux.com/)

```python
git clone https://github.com/C0DE-SLAYER/CliAniVerse
cd CliAniverse
pip install -r requirement.txt
python CliAniVerse.py
```

## Usage/Examples

#### 1. Manual search

1. Run using `python CliAniVerse.py`. Type the anime name you want to watch.
2. Select the anime from the list like which season, dub or sub, etc.
3. Select the episode to be watch.
4. The episode will start playing in your default browser where you can download and watch the anime.
5. You can use option for playing next episode or previous episode or search new anime.
6. Demo/Example : 
![Demo](https://raw.githubusercontent.com/C0DE-SLAYER/CliAniVerse/master/img/CliAniVerse_demo.gif)
![Demo](https://raw.githubusercontent.com/C0DE-SLAYER/CliAniVerse/master/img/browser_demo.png)

#### 2. Using history
1. Run using `python CliAniVerse.py -hist`. Select the anime to watch and it will be player in you default browser.
2. To delete history file. `python CliAniVerse.py -del`
3. Demo/Example : 
![Demo](https://raw.githubusercontent.com/C0DE-SLAYER/CliAniVerse/master/img/CliAniVerse_hist_demo.gif)
![Demo](https://raw.githubusercontent.com/C0DE-SLAYER/CliAniVerse/master/img/browser_demo.png)

## License

[MIT](https://github.com/C0DE-SLAYER/CliAniVerse/blob/master/LICENSE.txt)
