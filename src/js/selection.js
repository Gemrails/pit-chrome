

class Selection {
    constructor() {
        this.tag_con_style = `
        background-color: #fff;
        border-radius: 6px;
        z-index: 1000;
        height: 150px;
        min-width: 280px;
        position: fixed;
        top: 10px;
        right: 20px;
        border: 2px #f00 solid;`

        this.tag_style = `
        display: inline-block;
        margin: 11px 15px 10px;
        height: 28px;
        width: auto;
        font-size: 14px;
        font-weight: 600;
        line-height: 28px;
        float: left;`
    }

    getFullPageMixTag(tags) {
        let page_dom = document.documentElement
        let tagStr = tags.length? `<style> #tag_Adder:hover {opacity: 0;}</style><div id="tag_Adder" style="${this.tag_con_style}">${tags.reduce((pre, next, index) => `${(index === 1)?`<span style="${this.tag_style}">${pre}</span>`:pre}<span style="${this.tag_style}">${next}</span>`)}</div>` : ''
        page_dom.getElementsByTagName("body")[0].insertAdjacentHTML('beforeend',tagStr)
        const data = {
            text: page_dom.outerHTML,
            title: `${window.location.host}_${JSON.stringify(new Date().getTime())}`,
            url: window.location.href,
            tags: tags.join(',')
        }
        let tagDom = document.getElementById("tag_Adder")
        page_dom.getElementsByTagName("body")[0].removeChild(tagDom)
        return data
    }

    _getSelectedText() {
        if (window.getSelection) {
            return window.getSelection().toString()
        } else if (document.getSelection) {
            return document.getSelection()
        } else if (document.selection) {
            return document.selection.createRange().text
        }
    }

    _getSelectionMessage() {
        const text = this._getSelectedText()
        const url = window.location.href
        const message = {
            method: 'get_selection',
            data: {
                text: text,
                title: `${window.location.host}_${JSON.stringify(new Date().getTime())}`,
                url: url
            }
        };
        return message
    }

    _sendSelectionMessage(message) {
        chrome.runtime.sendMessage(message, (response) => {})
    }

    listenMouseUp() {
        this._sendSelectionMessage(this._getSelectionMessage())
        window.onmouseup = (e) => {
            if (!e.button === 2) {
                return;
            }
            this._sendSelectionMessage(this._getSelectionMessage())
        };
        return this;
    }
}

export default Selection
