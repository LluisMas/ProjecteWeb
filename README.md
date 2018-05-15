LRL Distributors

# Testing with Ubuntu  

To be able to use *behave* in Ubuntu you must download the latest version of Firefox Browser. 

``` 
sudo apt-get update
sudo apt-get install firefox
``` 
Then download Geckodriver and unpack it wherever you want.

https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz

Then geckodriver to the path:

```
export PATH:$PATH:/your/path/to/geckodriver
```


