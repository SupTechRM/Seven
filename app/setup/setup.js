const { app, BrowserWindow } = require('electron')

function createWindow() {
    const win = new BrowserWindow({
        width: 1366,
        height: 780
    })

    win.loadFile('setup/presentationUI_Main/index.html')
}

app.whenReady().then(() => {
    createWindow()
})