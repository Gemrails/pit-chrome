class Selection {
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
    const hole_page_text = document.documentElement.outerHTML? document.documentElement.outerHTML:$("html").html()
    const url = window.location.href
    const message = {
      method: text? 'get_selection' : 'get_page',
      data: {
          text: text? text : hole_page_text,
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
    const message = this._getSelectionMessage()
    this._sendSelectionMessage(message)

    window.onmouseup = (e) => {
      if (!e.button === 2) {
        return;
      }
      const message = this._getSelectionMessage()
      this._sendSelectionMessage(message)
    };
    return this;
  }
}

export default Selection
