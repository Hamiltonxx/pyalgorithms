alias ll="ls -lGafh"
alias proxy="export https_proxy=http://127.0.0.1:58591 http_proxy=http://127.0.0.1:58591 all_proxy=socks5://127.0.0.1:51837"

function sipsdim(){
    sips -g pixelHeight -g pixelWidth "$@"
}

